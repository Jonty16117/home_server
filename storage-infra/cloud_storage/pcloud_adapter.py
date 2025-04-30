import os
import subprocess
import pcloud
from .base_adapter import CloudStorageAdapter

class PCloudAdapter(CloudStorageAdapter):
    def __init__(self, username: str, password: str, mount_point: str = "/mnt/pcloud"):
        self.username = username
        self.password = password
        self.mount_point_path = mount_point
        self.client = None
        self.remote_name = "pcloud"  # Must match your rclone remote name

    def authenticate(self):
        self.client = pcloud.PCloudApi(self.username, self.password)

    def upload(self, file_path: str):
        self.client.upload(file_path, '/')

    def list_files(self):
        return self.client.listfolder('/')

    def delete(self, file_id: str):
        self.client.delete(file_id)

    @property
    def mount_point(self) -> str:
        return self.mount_point_path

    def mount(self):
        os.makedirs(self.mount_point_path, exist_ok=True)
        subprocess.run([
            "rclone", "mount", f"{self.remote_name}:", self.mount_point_path,
            "--daemon", "--vfs-cache-mode", "writes"
        ], check=True)

    def unmount(self):
        subprocess.run(["fusermount", "-u", self.mount_point_path], check=True)
