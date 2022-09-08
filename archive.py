import time,threading,os
from internetarchive import search_items, download
from flask import *
sessionInfo = {
  "totalFiles" : 0
}
app = Flask(__name__)
def downloadid(id, toDir, threadingInfo, items):
  #debug: print(threadingInfo['threads'])
  threadingInfo['threads'] += 1
  items.remove(id)
  print(threadingInfo['threads'])
  try:
    download(id, verbose=True, destdir=toDir, ignore_existing=True, ignore_errors=True, retries=3)
  except:
    print("Exception.")
    threadingInfo['threads'] -= 1
    return
  sessionInfo['totalFiles'] += 1
  print(threadingInfo['threads'])
  threadingInfo['threads'] -= 1


@app.route("/api/files")
def filesApi():
  return str(sessionInfo['totalFiles'])
@app.route("/")
def mainF():
  return open('views/index.html').read()
@app.route("/index.css")
def mainFcss():
  return open('views/index.css').read()
@app.route("/api/download")
def downloadApi():
  args = request.args.get('args').replace("%20", "")
  toDir = request.args.get('toDir')
  maxThr = request.args.get('maxThreads')
  x = threading.Thread(target=downloadSt, args=(args,toDir,maxThr,))
  time.sleep(0.2)
  x.start()
  return "success"

def downloadSt(args, toDir, maxThreads):
  items = []
  threadingInfo = {
    'maxThreads': maxThreads,
    'threads': 0
  }
  
  print(args, toDir)
  for i in search_items(args):
    items.append(i['identifier'])
  for i in items:
    if os.path.exists(toDir + "/" + i):
      print("removed " + i)
      items.remove(i)
  for i in items:
    while True:
      if threadingInfo['threads'] == threadingInfo['maxThreads']:
        return
      else:
        x = threading.Thread(target=downloadid, args=(i,toDir, threadingInfo,items))
        time.sleep(0.2)
        x.start()
        break
app.run(port=80)