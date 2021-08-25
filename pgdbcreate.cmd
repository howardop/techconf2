call setenvvars.sh

az postgres db create -g %RESOURCEGP% -s %PGSERVER% -n %PGDBNAME% --subscription %AZSUB%
