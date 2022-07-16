#!/bin/bash

RIA_DIR=/home/ubuntu/git/ua-ria-counter
LOG=$RIA_DIR/log.out

echo "XXXXXXXXXXXXXXXXXXXXXXXXX" > $LOG
echo `date` >> $LOG
#cd $RIA_DIR
python $RIA_DIR/ria.py >> $LOG
echo "XXXXXXXXXXXXXXXXXXXXXXXXX" >> $LOG

#echo "XXXXXXXXXXXXXXXXXXXXXXXXX"
#date
#echo "*************************"
#python $RIA_DIR/ria.py
#echo "XXXXXXXXXXXXXXXXXXXXXXXXX"


