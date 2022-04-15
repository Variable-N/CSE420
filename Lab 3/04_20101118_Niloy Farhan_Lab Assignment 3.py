import re
f = open("input.txt")
inp = f.read()
inp = inp.split("\n")
regex_list = inp[1:(int(inp[0]) + 1)]
string_list = inp[(int(inp[0]) + 2):]
for string in string_list:
    match = "NO"
    index = 0
    c = 0
    for regex in regex_list:
        c += 1
        if re.fullmatch(regex, string, 0):
            match = "YES"
            index = c
            break
    if match == "YES":
        print("YES, {}".format(index))
    else:
       print("NO, {}".format(index))