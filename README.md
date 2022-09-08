# threaded-ia-downloader
Threaded Internet Archive Downloader with Web interface.
#Install instructions
This requires some basic linux knowledge!!!

Upload the python script including the views folder to /home/$USER/iathreaded/
cd /home/$USER/
sudo chmod 777 -R /home/$USER/iathreaded
cd iathreaded/
pip install -r requirements.txt
cd /etc/systemd/system/
nano iathreaded.service
Put this in:

[Unit]
Description=Threaded internet archive downloader.
After=network.target

StartLimitIntervalSec=0
[Service]
Type=simple
Restart=always
RestartSec=1
User=[PUT USERNAME HERE]
WorkingDirectory=/home/[put username here]/iathreaded
ExecStart=python3 archive.py

[Install]
WantedBy=multi-user.target

sudo systemctl daemon-reload
sudo systemctl enable --now iathreaded

Now navigate to your server ip.

#ONLY REQUIRED IF UFW IS INSTALLED:
ufw allow 80
For other firewalls, view their manual.
