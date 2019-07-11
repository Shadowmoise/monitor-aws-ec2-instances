import csv
import json
from salut import salut

print (salut)
with open("aws-all-instance-details.csv","w",newline='') as file:
	csv_writer = csv.writer(file,delimiter=",")
	with open("test.json","r") as file1:
		jsonfile = json.loads(file1.read())
		csv_writer.writerow(jsonfile)