rem Set global environment variables
call setenvvars.cmd

rem Function App cannot be in the other resource group for some reason
az functionapp create --resource-group %FCNRG% --consumption-plan-location %LOCATION% --runtime python --functions-version 3 --runtime-version 3.8 --name %FCNAPPNAME% --storage-account %FCNSTGACCT% --os-type linux