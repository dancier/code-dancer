# variables.tf

# Required variables
variable "hcloud_token" {
  description = "Hetzner Cloud API Token"
  type        = string
  sensitive = true
}

variable "ssh_public_key" {
  description = "SSH Public Key"
  type        = string
}

variable "manager" {
  type        = map(any)
  description = "Server configuration map"
  default = {
    name        = "docker-host"
    server_type = "cx11"
    image       = "ubuntu-22.04"
    location    = "nbg1"
    backups     = false

  }
}

variable "data" {
  type        = map(any)
  description = "Server configuration map"
  default = {
    name        = "docker-host"
    server_type = "cx11"
    image       = "ubuntu-22.04"
    location    = "nbg1"
    backups     = false

  }
}
variable "runner" {
  type        = map(any)
  description = "Server configuration map"
  default = {
    name        = "docker-host"
    server_type = "cx11"
    image       = "ubuntu-22.04"
    location    = "nbg1"
    backups     = false

  }
}
variable "worker" {
  type        = map(any)
  description = "Server configuration map"
  default = {
    name        = "docker-host"
    server_type = "cx11"
    image       = "ubuntu-22.04"
    location    = "nbg1"
    backups     = false

  }
}
variable "server" {
  type        = map(any)
  description = "Server configuration map"
  default = {
    name        = "docker-host"
    server_type = "cx11"
    image       = "ubuntu-22.04"
    location    = "nbg1"
    backups     = false

  }
}


# Optional variables
variable "ssh_public_key_name" {
  description = "Name of public key"
  type = string
  default = "default"
}

variable "docker_compose_version" {
  type        = string
  description = "Docker compose version to install"
  default     = "2.17.3" # https://github.com/docker/compose/releases/latest
}


//variable "server" {}
//variable "volume_size" {}
//variable "volume_filesystem" {}