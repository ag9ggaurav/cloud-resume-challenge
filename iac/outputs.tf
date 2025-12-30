output "static_website_url" {
  value = azurerm_storage_account.frontend.primary_web_endpoint
}

output "function_endpoint" {
  value = "https://${azurerm_linux_function_app.function.default_hostname}"
}
