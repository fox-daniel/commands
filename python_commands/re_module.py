import re

# ^ is negation in a set only if it is first: [^a] is not "a"; [a^b] means match "a", "^", or "b"
# (?i) means case insensitive
# \b word boundary
# (?!...) matches if ... doesn't match the immediate next characters
# (?:...) the parentheses are for grouping, not tagging
# (?=...) look ahead: ... must match immediate next characters
astring = "ab,467755-5545_456 $555 ,755555222555"

# to find a single pattern. returns match obj or None
# re.search(r"...", "some string")

# re.match requires that pattern matches beginning of string
# re.search allows pattern to start anywhere

single_match =  re.search(r"545", astring)
print(single_match.group())

# for multiple searches with the same pattern it is faster to compile once:
p = re.compile(r"545")
m = p.search(astring)
print(f"The pattern {m.group()} is in {astring}")

# find a particular pattern repeating a range of times
repeated = re.search(r"[57]{2}", astring)
print("exactly two 5's or two 7's, whichever comes first:", repeated.group())

# find all groups of digits separated by something else; re.findall returns a list of matches
digit_groups = re.findall(r"\d+", astring)
for group in digit_groups:
	print("group of digits:", group)

# find a general pattern repeating a range of times
repeats = re.findall(r"(\d)\1{1,20}", astring)
for group in repeats:
	print("all repeats of a digit:", group)

# find the _first_ repeating general pattern using groupdict (e.g. first consecutively repeating digit)
print("\n Find Repeats with groupdict \n")
match = re.search(r"(?P<first_repeat>(\d))(?P=first_repeat){1,30}", astring)
if not match:
	print("No consecutively repeating digits")
else:
	print(f"The first repeating digit is {match.groupdict()['first_repeat']}.")

print("\n")

# To check the validity of a regular expressiong, the exception is re.error:
print("Test syntax of a regex:")
try:
	print(re.search(".*+", "hi"))
except re.error as e:
	print(f"Error {e}\n")

print("searching for excluded characters")
# Two approaches: explicit or with \W.
# result = re.search(r"[^a-zA-Z0-9-_]+", astring) 
result = re.search(r"[\W]+", astring) 

if result:
	print(f"found excluded characters: {result.group(0)}")

print("\nFind the first group of 4-16 digits.")
reps = re.search(r"\d{4,16}", astring)
if reps is not None:
	print(reps.group())


print("\nDetect Float (From HackerRank)")

astring = "+0.43453"
# astring = "+a.43453"

def is_float(astring):
    try:
        float(astring)
    except ValueError or OverflowError:
        return False
    if astring.lower() == "inf" or astring.lower() == "infinity":
        return True
    match = re.match(r"[-+]{0,1}\d*.\d+", astring)
    if match and match.group() == astring:
        return True
    else:
        return False

print(f"{astring} is a float: {is_float(astring)}")





# Find pattern with overlap
# e.g. 2 or more vowels between consonants
print("\n Patterns with overlap \n ***NOT WORKING*** \n")
# This string should return ee, ee, uu
astring = "diiidAageebeaeYtuuHeEEr" 
print(f"The string: {astring}\n")
# use the r"(?=(...))" syntax so that overlaps in pattern instances are allowed
# p = re.compile(r"(?:(?!(eiou)[b-z]))(?=([aeiou])\1{1,3})(?:(?!(eiou)[b-z]))")
# # p = re.compile(r"(?!(aeiou))"))
# matches = p.finditer(astring)
# matches = re.finditer(r"(?=([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][aeiouAEIOU][aeiouAEIOU]+[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]))",astring)
# p = re.compile(r"(?!(aeiou)[b-z])(?=([aeiou]))\2{1,20}(?!(aeiou)[b-z])")
p = re.compile(r"(?i)(?!(aeiou)[b-z])(?P<vowels>([aeiou]))(?P=vowels){1,20}(?!(aeiou)[b-z])")
matches = p.findall(astring)


if matches:
    print(matches)
        # match_list = []
        # for match in matches:
        #     # match_list.append(match.group()[1:-1])
        #     match_list.append(match.group())

        # if match_list:
        #     print("matches:")
        #     for match in match_list:
        #         print(match)
else:
    print(-1)


# Match an entire expression
print("\nMatch Entire String\n")
astrings = ['9333333333', '3333333333', '22222222222', '8888888888'] 

def validate(phone_number: str) -> str:
    match = re.search(r"^[789][0-9]{9}$", phone_number)
    if match:
        return 'YES' + " for " + match.group()
    else:
        return 'NO' + "  for " + phone_number

for astring in astrings:
    print(validate(astring))


print("\n START and END \n")
astring = "aaaabbaa"
substring = "aa"
p = re.compile(substring)
indices = (0,0)
matched = False
for i in range(len(astring)):
    m = p.search(astring[i:])
    if m:
        matched = True
        new_indices = (i+m.start(),i+m.end()-1)
        if new_indices != indices:
            print(new_indices)
            indices = new_indices
if matched == False:
    print((-1,-1))


print("\n---Match Group & Allow Overlap----\n")
astring = " &&& && && 8765 || "
print(astring)
# p = re.compile(r"(?=(?:\s)(\&\&|\|\|)(?:\s))")
p = re.compile(r"((?:\s)(\&\&|\|\|)(?:\s))")
m = p.finditer(astring)
for match in m:
    print(match.group(1), match.start(), match.end())


print("\n----Sub-Allow-Overlap--\n")
# astring = "6&&y && || && && |||\& &&& "
astring = "x&& &&& && && x || | ||\|| x"
print(astring)
astring = re.sub(r"(\s)(\&\&)(?=\s)", r" and", astring)
print(astring)

print("\n----Sub-With-Function-Allow-Overlap-\n")
# astring = "6&&y && || && && |||\& &&& "
astring = "x&& &&& && && x || | ||\|| x"
print(astring)
def replace(substring):
    if substring.group(2) == '&&':
        return ' and'
    if substring.group(2) == '||':
        return ' or'

astring = re.sub(r"(\s)(\&\&|\|\|)(?=\s)", replace, astring)
print(astring)

print("\n Sub \n")
s = "This$#is% Matrix#  %!"
print(s)
s = re.sub(r"([a-zA-Z0-9])(([$#\%&*!]|\s)+)(?=([a-zA-Z0-9]))", r"\1 ", s)
print(s)


print("\n---Non-Repeating-Pairs----\n")
P = "137370"
regex_integer_in_range = r"[1-9]\d{5}$"
regex_alternating_repetitive_digit_pair = r"(?=(?P<first_digit>\d)([0-9])(?P=first_digit))"

print(P)
print(bool(re.match(regex_integer_in_range, P)))
print((len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2))



print("\n Find HexCode")
s = """
#BED
{
    hi: #ADC657, no: #BBB5 heft=#576
}
#CD5
{
    (val: #6576F8, wei: #adc)
}
#546
{
    bei: #acf,
}
"""
print(s)
hex_list = []
re1 = r'\{(.+?)\}'
# The following regex returned empty strings which would have been more cumbersome to filter out than the current approach.
# re2 = r'(\#[0-9a-fA-F]{6}(?![0-9a-fA-F]))|(\#[0-9a-fA-F]{3}(?![0-9a-fA-F]))'
re2 = r'\#[0-9a-fA-F]{3,}'
p = re.compile(re1, flags = re.DOTALL)
matches = p.findall(s)
# print(matches)
p = re.compile(re2, flags = re.DOTALL)
for match in matches:
    # print(match)
    for code in p.findall(match):
        # print(code)
        if len(code) == 4 or len(code) == 7:
            hex_list.append(code)
print(hex_list)


print("HTML Parsing")
print("<![endif]-->")
p = re.compile(r"\<\!\[endif\]--\>$")
match = p.search("<!--[if IE 9]>IE9-specific content<![endif]-->")
print(match.group())
