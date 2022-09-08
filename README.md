# threaded-ia-downloader
Threaded Internet Archive Downloader with Web interface.
<br>**Install instructions**
<br>This requires some basic linux knowledge!!!

Upload the python script including the views folder to /home/$USER/iathreaded/

cd /home/$USER/

sudo chmod 777 -R /home/$USER/iathreaded

cd iathreaded/

pip install -r requirements.txt

sudo mv iathreaded.service /etc/systemd/system

sudo systemctl daemon-reload

sudo systemctl enable --now iathreaded


Now navigate to your server ip.

**ONLY REQUIRED IF UFW IS INSTALLED:**

ufw allow 80

For other firewalls, view their manual.
