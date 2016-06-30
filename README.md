# har2csv

This simple python script can be used to parse a HAR File (http archive file) and list all the urls which took greater than certain time and also dump into a csv file, result.csv, 

How to run

python har2csv.py <harfilename> <time>

e.g. : python har2csv.py abc.har 5 
This will dump all the requests which took graeter than 5 seconds to load

Re-running the script will append the exsitng result.csv with the new data
