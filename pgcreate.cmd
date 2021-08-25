# Taken from Quickstart: https://docs.microsoft.com/en-us/azure/postgresql/quickstart-create-server-database-azure-cli

call setenvvars.cmd

az postgres server create --resource-group %RESOURCEGP% --name %PGSERVER%  --location %LOCATION% --admin-user %PGADMIN% --admin-password %PGADMIBPW% --sku-name %PGSKU% --storage-size %PGSTORAGE%


rem Configure a server-level firewall rule
echo *** Creating firewall rule allowing all IPs to connect to server
az postgres server firewall-rule create --resource-group %RESOURCEGP% --server %PGSERVER% --name %FWRNAME% --start-ip-address %FWRSTART_IP% --end-ip-address %FWREND_IP%


# Get the connection information
echo *** Getting Postgres Server connect information
az postgres server show --resource-group %RESOURCEGP% --name %PGSERVER%

