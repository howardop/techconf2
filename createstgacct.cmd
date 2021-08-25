
rem Set global environment variables
call setenvvars.cmd

az storage account create --resource-group %FCNRG%  --name %FCNSTGACCT% --kind StorageV2 --location %LOCATION%

