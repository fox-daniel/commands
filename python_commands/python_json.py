# notes on the Python json library.
# Based on https://realpython.com/python-json/#python-supports-json-natively
import json

"""
The built-in json library encodes (serializes) and decodes json files.

Serialize/Encode:
.dump() - write serialized data to file
.dumps() - write serialized data to Python string

Deserialize/Decode:
.load() -  loads json data to a Python object
.loads() - loads json data to a Python string
"""

# Example: Serialize/Encode: Write data in memory to disk

# This data is a python object:
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

# This writes the data (a Python object) to (serialized) json in a file.
with open("json_data.json", "w") as write_file:
	json.dump(data, write_file, indent = 4)

# To use _serialized_ JSON data in a program:
json_string = json.dumps(data, indent = 4)

print(json_string)


# Examples: Decode

# Example: tuple to list

tuple_data = (8,"eight")
tuple_encoded = json.dumps(tuple_data)
tuple_decoded = json.loads(tuple_encoded)
round_trip = tuple_data == tuple_decoded
print(round_trip)
print(tuple_data)
print(tuple_decoded)

# Example: Deserialize a json file to a Python object; in this case a dict.

with open("json_data.json", "r") as read_file:
	# data is a Python object (a dict in this case)
	data = json.load(read_file)
	print(data)
	print(type(data))

# Example: Deserialize an in-memory json object (str, bytes, or bytearray instance) to a Python object

data_string = """
{
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    },
    "vice president": {
        "name": "Zaphod",
        "species": "Betel"
    }
}
"""
# Create a Python object (a dict in this case)
data = json.loads(data_string)
print(type(data))
# Can use structure of the Python object
for item in data.values():
	print(item)

# Example: read json from stdin

from io import StringIO
io = StringIO('[{"hi": "hola"},{"bye": "ciao"}]') 
data = json.load(io)
for item in data:
	print(item	)

# Example:






