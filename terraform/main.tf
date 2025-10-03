terraform {
  required_providers {
    proxmox = {
      source = "Telmate/proxmox"
      version = "3.0.2-rc04"
    }
  }
}

provider "proxmox" {
 pm_api_url   = "https://pm02:8006/api2/json"
 pm_tls_insecure = true
}

variable "k8_control_plane_count" {
  default = 1
}

variable "k8_worker_node_count" {
  default = 2
}

resource "proxmox_vm_qemu" "k8_control_plane" {
  count       = var.k8_control_plane_count
  name        = "k8-cp-${count.index + 1}" 
  target_node = "xyz"
  clone       = "k8-base-template-02"
  ciuser = "root"
  cipassword = "12345"
  ipconfig0 = "ip=192.168.100.${10 + count.index}/24,gw=192.168.100.1"
  full_clone  = false

  cpu { 
    cores   = 4
    sockets = 1
  }
  
  memory  = 16000

  # Disks
  disk {
    size    = "20G"
    storage = "local-lvm"
    slot  = "scsi0"
    type = "disk"
  }

  disk {
    storage = "local-lvm"
    slot  = "ide2"
    type = "cloudinit"
  }

  network {
    id     = 0
    model  = "virtio"
    bridge = "vmbr0"
  }
}


resource "proxmox_vm_qemu" "k8_worker_node" {
  count       = var.k8_worker_node_count
  name        = "k8-wk-${count.index + 1}"
  target_node = "xyz"
  clone       = "k8-base-template-02"
  ciuser = "root"
  cipassword = "12345"
  ipconfig0 = "ip=192.168.200.${10 + count.index}/24,gw=192.168.200.1"
  full_clone  = false

  cpu { 
    cores   = 4
    sockets = 1
  }
  
  memory  = 16000

  # Disks
  disk {
    size    = "20G"
    storage = "local-lvm"
    slot  = "scsi0"
    type = "disk"
  }

  disk {
    storage = "local-lvm"
    slot  = "ide2"
    type = "cloudinit"
  }

  network {
    id     = 0
    model  = "virtio"
    bridge = "vmbr0"
  }
}
