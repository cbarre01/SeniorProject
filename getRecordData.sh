#!/bin/bash



OUTPUT=$(<dates.txt)

IFS=', ' read -r -a datesList <<< "$OUTPUT"

for curDate in "${datesList[@]}"
do
    csv=".csv"
    curDateCSV=$curDate$csv
    scrapy crawl BRSpiderBroken -a fulldate=$curDate -o $curDateCSV -t csv
done
