. setenvvars.sh

CMD="az postgres db delete -g $RESOURCEGP -s $PGSERVER -n $PGDBNAME" #--subscription $AZSUB
echo $CMD
eval $CMD