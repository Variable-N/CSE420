f = open("input.txt")
keywords_found = []
identifier_found = []
math_operator_found = []
logical_operator_found = []
numerical_values_found = []
others_found = []

keywords = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
math_operator = ["+", "-", "*", "/", "%", "++", "--", "="]
logical_operator = ["<", ">", ">=", "<=", "==", "!=", "&&", "||"]
others = [";", ",", "(", ")", "[", "]", "{", "}", "!", "$", "&", "?", ":", "~", "^", chr(34), chr(39)] #chr 34 is " and chr 39 is '

def isfloat(value):
    try: 
        float(value)
        return True
    except ValueError:
        return False


for line in f:
    string = line
    for s in string:
        if s in others:
            if s not in others_found:
                others_found.append(s)
            string = string.replace(s," ")

        if s in logical_operator:
            if s not in logical_operator_found:
                logical_operator_found.append(s)
            string =string.replace(s," ")

        if s in math_operator:
            if s not in math_operator_found:
                math_operator_found.append(s)
            string = string.replace(s," ")
        
    for key in keywords:
        if key in string:
            if key not in keywords_found:
                keywords_found.append(key)
            string = string.replace(key," ")

    string = string.replace('\n', "")
    string = string.replace('\t', "")
    token = string.split()
    for t in token:
        if t.isnumeric() or isfloat(t):
            if t not in numerical_values_found:
                numerical_values_found.append(t)
        else:
            if t not in identifier_found:
                identifier_found.append(t)
        

print( "Keywords: ", end = "")
print(*keywords_found, sep = ", ")
print( "Identifier: ", end = "")
print(*identifier_found, sep = ", ")
print( "Math Operators: ", end = "")
print(*math_operator_found, sep = ", ")
print( "Logical Operators: ", end = "")
print(*logical_operator_found, sep = ", ")
print( "Numerical Values: ", end = "")
print(*numerical_values_found, sep = ", ")   
print( "Others: ", end = "")
print(*others_found, sep = " ")