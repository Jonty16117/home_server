import os
import subprocess
from mega import Mega
from .base_adapter import CloudStorageAdapter

class MegaAdapter(CloudStorageAdapter):
    def __init__(self, email: str, password: str, mount_point: str = "/mnt/mega"):
        self.email = email
        self.password = password
        self.mount_point_path = mount_point
        self.client = None
        self.remote_name = "mega"  # must match your rclone config name

    def authenticate(self):
        self.client = Mega().login(self.email, self.password)

    def upload(self, file_path: str):
        self.client.upload(file_path)

    def list_files(self):
        return self.client.get_files()

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
