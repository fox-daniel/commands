import xml.etree.ElementTree as ET

# access root with .getroot()
# access tag with .tag (e.g. <data>...</data>)
# access text with .text
# access attributes with .attrib


tree = ET.parse("xml_example_data.xml")
root = tree.getroot()
print(root.tag)
print(root.attrib)

# iterate over children
for child in root:
	print(child.tag, child.attrib)

# iterate over elements that are not necessarily children but are further descendents
for neighbor in root.iter('neighbor'):
	print(neighbor.attrib) 

# find children with a particular tag
print("\nFind country names and ranks.\n")
for country in root.findall('country'):
	rank = country.find('rank').text
	name = country.get('name')
	print(name, rank)

print("\nFind state names and ranks.\n")
# find children with a particular tag
for country in root.findall('state'):
	rank = country.find('rank').text
	name = country.get('name')
	attr = country.attrib
	print(name, rank, attr)

print("\nCount the number of attributes in the entire file.\n")
score = 0
for element in root.iter():
	print(element)
	for attr in element.attrib:
		print(attr)
		score += 1
print(score)

print("\nFind the max depth\n")
# max_depth = 0 
# element_level = {}

# def depth(element, level):
# 	# global max_depth
# 	level += 1
# 	element_level[element]=level
# 	for child in element:
# 		depth(child, level)

max_depth = 0
def depth(element, level):
	global max_depth
	level += 1
	if level > max_depth:
		max_depth = level
	# element_level[element]=level
	for child in element:
		print(child.tag, level, max_depth)
		depth(child, level)
	
tree = ET.parse("xml_test.xml")
root = tree.getroot()

depth(root, -1)
# print(element_level)

# for key, value in element_level.items():
# 	if value > max_depth:
# 		max_depth = value
print(max_depth)


