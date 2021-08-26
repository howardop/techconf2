rem  This CLI call is needed to pass the Service Bus Queue connection string up to Azure.  It has to be done this way because it is referenced in function.json file for ServiceBusQueueTrigger1 which has not executable code.

call setenvvars.cmd

az functionapp config appsettings set --name %FCNAPPNAME% --resource-group %FCNRG% --settings POSTGRES_PW=%PGADMINPW%
az functionapp config appsettings set --name %FCNAPPNAME% --resource-group %FCNRG% --settings SENDGRID_API=%SENDGRIDAPI%"
az functionapp config appsettings set --name %FCNAPPNAME% --resource-group %FCNRG% --settings howiesb2_SERVICEBUS=%SBCONNECTIONSTRING%



