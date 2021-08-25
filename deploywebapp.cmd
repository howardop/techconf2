call setenvvars.cmd

cd .\web
az webapp up --name %APPNAME% --resource-group %RESOURCEGP% --plan %APPPLAN% --sku %APPSKU% --location %LOCATION%