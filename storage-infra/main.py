from cloud_storage.google_drive_adapter import GoogleDriveAdapter
from cloud_storage.mega_adapter import MegaAdapter
from cloud_storage.pcloud_adapter import PCloudAdapter
from cloud_storage.cloud_storage_manager import CloudStorageManager

def main():
    manager = CloudStorageManager()

    # Initialize adapters with local mount points
    gdrive = GoogleDriveAdapter("/mnt/gdrive")
    mega = MegaAdapter("email@example.com", "yourpassword", "/mnt/mega")
    pcloud = PCloudAdapter("username", "yourpassword", "/mnt/pcloud")

    # Register adapters
    manager.register_adapter(gdrive)
    manager.register_adapter(mega)
    manager.register_adapter(pcloud)

    # Authenticate all cloud accounts
    manager.authenticate_all()

    # Mount all cloud drives locally
    manager.mount_all()

    # Add their paths as GlusterFS bricks
    manager.add_to_gluster("gv0")

    # Example operations
    manager.upload_to_all("test.txt")
    files = manager.list_all()
    print(files)

    # Optional: unmount everything after use
    # manager.unmount_all()

if __name__ == "__main__":
    main()
