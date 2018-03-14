#!/bin/bash
# Jim McKibben
# AutoShun.org IPTables Blocklist Importer

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin

wget -O /tmp/shunlist.csv https://www.autoshun.org/download/?api_key=fd6b5f8e6cfb26d1d9220c5&format=csv

cat /tmp/shunlist.csv | egrep -o '^([0-9]{1,3}\.){3}[0-9]{1,3}' > /tmp/blocklist.txt

while read IP; do
	ipset add blacklist $IP
done < /tmp/blocklist.txt

rm /tmp/shunlist.csv
rm /tmp/blocklist.txt

