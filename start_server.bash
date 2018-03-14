#!/bin/bash

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin

cd /home/Andr0meda/DESENV/d2

$fpid=/tmp/pid-$$

ps -efl | grep runsslserver | grep -v grep > $fpid

if [ -s $fpid ]
then
     python manage.py runsslserver 0.0.0.0:443
fi
sleep 10

rm $fpid
     
exit 0



