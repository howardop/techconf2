call setenvvars.cmd 

pg_restore --clean -h %PGHOST% -U %PGADMIN%@%PGHOST% -d %PGDBNAME% C:\Users\IBM_ADMIN\Documents\Courses\BertelsmanScholarship\Project3\Code\Migrating-Apps\data\techconfdb_backup.tar