## Reload systemd and enable the service:
sudo ln -s /opt/mockload/mockcpuload.service /etc/systemd/system/mockcpuload.service
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable mockcpuload
sudo systemctl start mockcpuload


## To Monitor:
htop       # live view
ps aux | grep mockcpuload
systemctl status mockcpuload
