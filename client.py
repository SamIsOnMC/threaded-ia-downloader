import requests
import tkinter as tk
root = tk.Tk()
frm = tk.Frame(root)
root.geometry("400x200")
argTxt = tk.Label(root, text="Arguments")

arguments = tk.Text(root, width=20, height=1)
maxThrTxt = tk.Label(root, text="Max threads")

maxThr = tk.Text(root, width=20, height=1)
dirText = tk.Label(root, text="Save directory")

direc = tk.Text(root, width=20, height=1)
dirText = tk.Label(root, text="URL")

direc = tk.Text(root, width=20, height=1)
def sendRq():
  maxThr.get("1.0",'end-lc')
  requests.get("")

tk.Button(root, text="Run", command=root.destroy).grid(column=1, row=0)

argTxt.pack()
arguments.pack()
maxThrTxt.pack()
maxThr.pack()
dirText.pack()
direc.pack()


root.mainloop()
