@echo off
rem Global configuration variables for Project 3

set AZSUB=5d449df0-189e-4834-b692-e23333010cfa

set RESOURCEGP=p3-rg
set LOCATION=eastus
set STGACCT=hlostgact3

set FWRNAME=AllowAllIP
set FWRSTART_IP=0.0.0.0
set FWREND_IP=255.255.255.255

rem Postgres Related
set PGSERVER=hlopgserver
set PGADMIN=hloadmin
set PGADMINPW=P@ssw0rd
set PGSKU=B_GEN5_1
rem Minimum size on Azure is 5120
set PGSTORAGE=5120  
set PGHOST=%PGSERVER%.postgres.database.azure.com
set PGDBNAME=techconfdb  

rem Service Bus Related
set SBNAME=howiesb2
set SBCONNECTIONSTRING=Endpoint=sb://howiesb2.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=7swZ0NCBYsVTg0+ap8jmHWrj03zuk5DOhDZBV3f+UpU=

rem App Service Related
set APPPLAN=ASP-p3rg-9cb4
set APPSKU=Free
set APPNAME="hlotechconf"

rem Azure Function related
set FCNAPPNAME=hlofcnapp3
set FCNNAME=hlosbqclient
set FCNRG=p3-fcnapp-rg
set FCNSTGACCT=hlofcnappstgacct

@echo on