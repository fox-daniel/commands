import sys
import json


# ingest data from stdin as a string
# run $ cat json_data.json | python python_in_out.py
def ingest_as_string():
	data = ""
	for line in sys.stdin:
	  data = data + line.rstrip()
	# now data is a Python string
	print(data)

def ingest_as_json():
	# ingest data from stdin as json
	# run $ cat json_data.json | python python_in_out.py
	data = json.load(sys.stdin)
	print(data)

def ingest_with_sys_stdin():
	# Run: $ echo "some text" | python python_in_out.py
	lines = sys.stdin.readlines()
	sys.stdout.write(" ".join(lines))

def ingest_with_input():
	"""Catch multiple inputs from multiple prompts."""
	text = input("Enter something, please:")
	more_text = input("Enter something else, please:")
	sys.stdout.write(text + "\n" + more_text + "\n")

if __name__ == "__main__":
	# I tried to run the command as below, but it created an infinite loop
	# os.system("cat json_data.json | python python_in_out.py")
	# Test this fn:
	# ingest_as_string()
	# or this fn:
	# ingest_as_json()
	# or this
	ingest_with_input()
	# or this
	# ingest_with_sys_stdin()
	