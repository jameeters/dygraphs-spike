import json
import csv

filename = "test_data"
output_filename = filename + ".csv"
with open(filename, 'r') as data_file:
	data = json.load(data_file)

readings = data["value"]["timeSeries"][0]["values"][0]["value"]

for r in readings:
	del r["qualifiers"]

with open(output_filename, 'w+') as out_file:
	writer = csv.DictWriter(out_file, readings[0].keys())
	writer.writeheader()
	writer.writerows(readings)
	

