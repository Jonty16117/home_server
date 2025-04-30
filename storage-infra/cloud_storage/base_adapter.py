from abc import ABC, abstractmethod

class CloudStorageAdapter(ABC):
    @abstractmethod
    def authenticate(self):
        """Authenticate with the cloud provider."""
        pass

    @abstractmethod
    def upload(self, file_path: str):
        """Upload a file to the cloud provider."""
        pass

    @abstractmethod
    def list_files(self):
        """List all files from the cloud provider."""
        pass

    @abstractmethod
    def delete(self, file_id: str):
        """Delete a file from the cloud provider."""
        pass

    @property
    @abstractmethod
    def mount_point(self) -> str:
        """Return the local mount point of the cloud provider."""
        pass

    @abstractmethod
    def mount(self):
        """Mount the cloud storage to the local filesystem."""
        pass

    @abstractmethod
    def unmount(self):
        """Unmount the cloud storage from the local filesystem."""
        pass
