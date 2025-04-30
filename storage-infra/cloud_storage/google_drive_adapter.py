import os
import subprocess
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from .base_adapter import CloudStorageAdapter

class GoogleDriveAdapter(CloudStorageAdapter):
    def __init__(self, mount_point: str = "/mnt/gdrive"):
        self.drive = None
        self._mount_point = mount_point
        self.remote_name = "gdrive"  # must match rclone config

    def authenticate(self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(gauth)

    def upload(self, file_path: str):
        file = self.drive.CreateFile({'title': os.path.basename(file_path)})
        file.SetContentFile(file_path)
        file.Upload()

    def list_files(self):
        return self.drive.ListFile({'q': "'root' in parents"}).GetList()

    def delete(self, file_id: str):
        file = self.drive.CreateFile({'id': file_id})
        file.Delete()

    @property
    def mount_point(self) -> str:
        return self._mount_point

    def mount(self):
        os.makedirs(self._mount_point, exist_ok=True)
        subprocess.run([
            "rclone", "mount", f"{self.remote_name}:", self._mount_point,
            "--daemon", "--vfs-cache-mode", "writes"
        ], check=True)

    def unmount(self):
        subprocess.run(["fusermount", "-u", self._mount_point], check=True)
