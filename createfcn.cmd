rem See https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=azure-cli%2Ccmd%2Cbrowser

rem 
rem Set global environment variables
call setenvvars.cmd

rem Create  function project
func init function --python
cd function

rem Publish app to Azure 
func azure functionapp publish %FCNAPPNAME% --python
