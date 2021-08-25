
call setenvvars.cmd 

rem Connect to the Azure Database for PostgreSQL server by using psql
"C:\Program Files\PostgreSQL\13\bin\psql.exe" --host=%PGHOST% --port=5432 --username=%PGADMIN%@%PGHOST% --dbname=%PGDBNAME%
