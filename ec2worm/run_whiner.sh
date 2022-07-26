#!/bin/bash

RIA_DIR=/home/ubuntu/git/ua-ria-counter/ec2worm
LOG=$RIA_DIR/log.out

echo "XXXXXXXXXXXXXXXXXXXXXXXXX" > $LOG
echo `date` >> $LOG
#cd $RIA_DIR
python $RIA_DIR/whiner.py >> $LOG
echo "XXXXXXXXXXXXXXXXXXXXXXXXX" >> $LOG
cat $LOG


#echo "XXXXXXXXXXXXXXXXXXXXXXXXX"
#date
#echo "*************************"
#python $RIA_DIR/ria.py
#echo "XXXXXXXXXXXXXXXXXXXXXXXXX"
#cat $LOG


