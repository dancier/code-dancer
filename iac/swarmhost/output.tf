output "manager_ip_addr" {
  value = tolist(hcloud_server.manager.network)[0].ip
}