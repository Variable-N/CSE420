

def web_or_email(string):
    state = 0
    for char in string:
        if state == 0:
            if char == 'w': state = 6
            elif char == 'h': state = 14
            elif char.isalpha(): state = 1
            else: state = 13
        elif state == 1:
            if char.isalpha() or char.isdigit(): state = 2
            else: state = 13
        elif state == 2:
            if char == "@": state = 3 
            elif char.isalpha() or char.isdigit(): state = 2
            elif char == '.': state = 1
            else: state = 13
        elif state == 3:
            if char.isalpha(): state = 22
            else: state = 13
        elif state == 4:
            if char.isalpha(): state = 5
            elif char == '.': state = 13
            else: state = 13
        elif state == 5:
            if char.isalpha(): state = 5
            elif char == '.': state = 4
            else: state = 13
        elif state == 6:
            if char == "@": state = 3  
            elif char == 'w': state = 7
            elif char.isalpha() or char.isdigit(): state = 1
            else: state = 13
        elif state == 7:
            if char == "@": state = 3  
            elif char == 'w': state = 8
            elif char.isalpha() or char.isdigit(): state = 1
            else: state = 13
        elif state == 8:
            if char == "@": state = 3  
            elif char == '.': state = 9
            elif char.isalpha() or char.isdigit(): state = 1
            else: state = 13
        elif state == 9:
            if char.isalpha() or char.isdigit(): state = 10
            else: state = 13
        elif state == 10:
            if char.isalpha() or char.isdigit(): state = 10
            elif char == '.': state = 11
            elif char == '@': state = 3
            else: state = 13
        elif state == 11:
            if char.isdigit(): state = 10
            elif char.isalpha(): state = 12
            else: state = 13
        elif state == 12:
            if char == '.': state = 11
            elif char.isdigit(): state = 10
            elif char.isalpha() or char == '/': state = 12
            else: state = 13
        elif state == 13:
            #DEAD State
            break
        elif state == 14:
            if char == 't': state = 15
            elif char.isalpha() or char.isdigit(): state = 2
            elif char == "@": state = 3
            else: state = 13
        elif state == 15:
            if char == 't': state = 16
            elif char.isalpha() or char.isdigit(): state = 2
            elif char == "@": state = 3
            else: state = 13
        elif state == 16:
            if char == 'p': state = 17
            elif char.isalpha() or char.isdigit(): state = 2
            elif char == "@": state = 3
            else: state = 13
        elif state == 17:
            if char == ":": state = 19
            elif char == "s": state = 18
            elif char.isalpha() or char.isdigit(): state = 2
            elif char == "@": state = 3
            else: state = 13
        elif state == 18:
            if char == ":": state = 19
            elif char.isalpha() or char.isdigit(): state = 2
            elif char == "@": state = 3
            else: state = 13
        elif state == 19:
            if char == "/": state = 20
            else: state = 13
        elif state == 20:
            if char == "/": state = 21
            else: state = 13
        elif state == 21:
            if char == 'w': state = 6
            elif char.isalpha() or char.isdigit(): state = 9
            else: state = 13
        elif state == 22: 
            if char.isalpha(): state = 22
            elif char == '.': state = 4
            else: state = 13
        
    if state == 5:   return "Email"
    if state == 12: return "Web"
    return "Invalid"

f = open("input.txt")
string = f.read().split('\n')
f.close()
for i in range(1,len(string)):
    print(web_or_email(string[i]),i)
    

