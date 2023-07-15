# main.tf
terraform {
  required_providers {
    hcloud = {
      source = "hetznercloud/hcloud"
    }
  }
}

provider "hcloud" {
  token = var.hcloud_token
}

resource "hcloud_ssh_key" "ssh-key" {
  name       = var.ssh_public_key_name
  public_key = file("~/.ssh/id_rsa.pub")
}

resource "hcloud_network" "dancier-network" {
  name     = "dancier-network"
  ip_range = "10.0.0.0/16"
}

resource "hcloud_network_subnet" "dancier-subnet" {
  network_id   = hcloud_network.dancier-network.id
  type         = "cloud"
  network_zone = "eu-central"
  ip_range     = "10.0.0.0/24"
}

resource "hcloud_network_route" "network-route" {
  network_id  = hcloud_network.dancier-network.id
  destination = "0.0.0.0/0"
  gateway     = "10.0.0.2"
}

resource "hcloud_server" "manager" {
  name        = "manager"
  image       = var.server.image
  server_type = var.server.server_type
  location    = var.server.location
  backups     = var.server.backups
  ssh_keys    = [var.ssh_public_key_name]
  user_data = templatefile("${path.module}/user_data/manager.yaml", {
    docker_compose_version = var.docker_compose_version
  })
  network {
    network_id = hcloud_network.dancier-network.id
    ip = "10.0.0.2"
  }
}

# create worker server
#hcloud server create --name worker-01 --ssh-key swarm --image ubuntu-20.04 --type cx21 --location nbg1 --network network-01

resource "hcloud_server" "worker" {
  name        = "worker"
  image       = var.server.image
  server_type = var.server.server_type
  location    = var.server.location
  backups     = var.server.backups
  ssh_keys    = [var.ssh_public_key_name]
  user_data = templatefile("${path.module}/user_data/worker.yaml", {
    docker_compose_version = var.docker_compose_version
  })
  network {
    network_id = hcloud_network.dancier-network.id
    ip = "10.0.0.3"
  }
  public_net {
    ipv4_enabled = false
    ipv6_enabled = false
  }
}


# create runner server
#hcloud server create --name runner-01 --ssh-key swarm --image ubuntu-20.04 --type cpx11 --location nbg1 --network network-01

# resource "hcloud_server" "runner" {
#   name        = "runner"
#   image       = var.server.image
#   server_type = var.server.server_type
#   location    = var.server.location
#   backups     = var.server.backups
#   ssh_keys    = [var.ssh_public_key_name]
#   user_data = templatefile("${path.module}/user_data/runner.yaml", {
#     docker_compose_version = var.docker_compose_version
#   })
#   network {
#     network_id = hcloud_network.network.id
#     ip = "10.0.0.4"
#   }
#   public_net {
#     ipv4_enabled = false
#     ipv6_enabled = false
#   }
# }


# # create data server
# #hcloud server create --name data-01 --ssh-key swarm --image ubuntu-20.04 --type cx21 --location nbg1 --network network-01

# resource "hcloud_server" "data" {
#   name        = "data"
#   image       = var.server.image
#   server_type = var.server.server_type
#   location    = var.server.location
#   backups     = var.server.backups
#   ssh_keys    = [var.ssh_public_key_name]
#   user_data = templatefile("${path.module}/user_data/data.yaml", {
#     manager_ip_addr = tolist(hcloud_server.manager.network)[0].ip
#   })
#   network {
#     network_id = hcloud_network.network.id
#     ip = "10.0.0.5"
#   }
#   public_net {
#     ipv4_enabled = false
#     ipv6_enabled = false
#   }

# }

# resource "hcloud_volume" "master_volume" {
#   name      = "master-volume"
#   size      = 11
#   server_id = hcloud_server.data.id
#   automount = true
#   format    = "xfs"
#   delete_protection = false
# }


# create the volume that will be used by gluster and automount it to the data server (fstab will be already setted)
#hcloud volume create --name volume-01 --size 20 --server data-01 --automount --format ext4

