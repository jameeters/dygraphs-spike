import json
import csv
from pprint import pprint

filename = "test_data"
output_filename = filename + ".csv"


with open(filename, 'r') as data_file:
	data = json.load(data_file)
# cut down to only the part I use
data =  data["value"]["timeSeries"][0]
readings = data["values"][0]["value"]
noVal = int(data["variable"]["noDataValue"])
# Get the description of what the values represent
varDescription = data["variable"]["variableDescription"]

for r in readings:
	# Delete field I'm not using
	del r["qualifiers"]
	# Treat values as ints instead of unicode
	r["value"] = int(r["value"])
	# Set bad data to the string "null" instead of -99999. This is a hack.
	if r["value"] == noVal:
		r["value"] = "null"
	# Rename value to the description provided with the data
	r[varDescription] = r.pop("value")
	

with open(output_filename, 'w+') as out_file:
	# Use ; as the delimiter because varDescription may contain a comma, and dygraphs seems to 		# have problems with quoting in csv files. Must specify headers beacause otherwise time ends
	# up on the y-axis.
	writer = csv.DictWriter(out_file, ["dateTime", varDescription], delimiter=';', quoting=csv.QUOTE_MINIMAL)
	writer.writeheader()
	writer.writerows(readings)
	
print("done")
