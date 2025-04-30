import os
import subprocess
from typing import List
from .base_adapter import CloudStorageAdapter

class CloudStorageManager:
    def __init__(self):
        self.adapters: List[CloudStorageAdapter] = []

    def register_adapter(self, adapter: CloudStorageAdapter):
        self.adapters.append(adapter)

    def authenticate_all(self):
        for adapter in self.adapters:
            adapter.authenticate()

    def upload_to_all(self, file_path: str):
        for adapter in self.adapters:
            adapter.upload(file_path)

    def list_all(self):
        all_files = {}
        for adapter in self.adapters:
            all_files[adapter.__class__.__name__] = adapter.list_files()
        return all_files

    def delete_from_all(self, file_id: str):
        for adapter in self.adapters:
            try:
                adapter.delete(file_id)
            except Exception:
                continue  # Skip errors from missing files

    def mount_all(self):
        for adapter in self.adapters:
            adapter.mount()

    def unmount_all(self):
        for adapter in self.adapters:
            adapter.unmount()

    def add_to_gluster(self, volume_name: str):
        for adapter in self.adapters:
            brick_path = os.path.join(adapter.mount_point, "gluster-brick")
            os.makedirs(brick_path, exist_ok=True)
            subprocess.run(
                ["gluster", "volume", "add-brick", volume_name, f"localhost:{brick_path}", "force"],
                check=True
            )

    def remove_from_gluster(self, volume_name: str):
        for adapter in self.adapters:
            brick_path = os.path.join(adapter.mount_point, "gluster-brick")
            subprocess.run(
                ["gluster", "volume", "remove-brick", volume_name, f"localhost:{brick_path}", "force"],
                check=True
            )
