import json
import csv
from pprint import pprint

filename = "test_data"
output_filename = filename + ".csv"


with open(filename, 'r') as data_file:
	data = json.load(data_file)

readings = data["value"]["timeSeries"][0]["values"][0]["value"]

# data = data["value"]["timeSeries"][0]
# info = {}
# info["siteCode"] = data["sourceInfo"]["siteCode"][0]["agencyCode"] + " " + data["sourceInfo"]["siteCode"][0]["value"]
# info["siteName"] = data["sourceInfo"]["siteName"]
# info["varDescription"] = data["variable"]["variableDescription"]
# info["varName"] = data["variable"]["variableName"]
# info["unit"] = data["variable"]["unit"]["unitCode"]


noVal = int(data["variable"]["noDataValue"])

for r in readings:
	del r["qualifiers"]
	r["value"] = int(r["value"])
	if r["value"] == noVal:
		r["value"] = "null"

	r[info["varDescription"]] = r.pop("value")
	

with open(output_filename, 'w+') as out_file:
	writer = csv.DictWriter(out_file, ["dateTime", info["varDescription"]], delimiter=';', quoting=csv.QUOTE_MINIMAL)
	writer.writeheader()
	writer.writerows(readings)

	
print("done")
