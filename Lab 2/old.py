
def is_website(url):
    # For this assignment I am spliting a url to 5 parts. for example: https://www.bracu.ac.bd/academics/departments
    #        https://         www.          bracu.ac    .bd         /academics/departments
    #      1. Protocol   2. Host name     3.  SLD      4.TLD          5.   Path 
    # 
    # Although it is not necessary to have all this 5 parts in an URL. But for being a valid URL, 
    # it must have either a protocol, SLD and TLD  [1,3,4] or  Host name, SLD and TLD. [2,3,4]
    # 

    conditions = {"Protocol" : False , 
                      "Host" : False, 
                       "SLD" : False, 
                       "TLD" : False, 
                      "Path" : False, }
    
    protocols = ["http://", "https://", "ftp://", "file://", "mailto://"]
    pointer = 0
    for p in protocols:
        if url.startswith(p):
            conditions["Protocol"] = True
            pointer = len(p)
            break
    
    not_valid= "!@#$%^&*();:,?/\=+<>ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    splited_url = url[pointer:].split(".")
    for c in splited_url:
        if len(c) < 1:
            return False                   # consecutive dots are not valid in domain name
        if '/' in c:
            d = c.split('/')
            if len(d[1]) > 0:
                conditions["Path"] = True
            if len(d[0]) > 0:
                if d[0].isdigit():
                    conditions["TLD"] = False
                else:
                    for char in d[0]:
                        if char in not_valid:
                            conditions["TLD"] = False
                            break
                        else:
                            conditions["TLD"] = True
                        
        if c == "www":
            conditions["Host"] = True
        elif conditions["SLD"] != True:
            for char in c:
                if char in not_valid:
                    conditions["SLD"] = False
                    break
                else:
                    conditions["SLD"] = True
        elif conditions["TLD"] != True:
            if c.isdigit():
                conditions["TLD"] = False
            else:
                for char in c:
                    if char in not_valid:
                        conditions["TLD"] = False
                        break
                    else:
                        conditions["TLD"] = True
    
    
    if conditions["Protocol"] and conditions["SLD"] and conditions["TLD"]: 
        return True
    if conditions["Host"] and conditions["SLD"] and conditions["TLD"]: 
        return True
    # print(conditions)
    return False

def is_email(email):
    # Assuming, An email must have an @ sign
    # The first letter can't be number or any special characters
    # Domain must have two part. a domain name and a top level domain. Such as, gmail is domain name, .com is TLD.
    if "@" not in email:
        return False
    if email[0].isdigit() or not email[0].isalpha():
        return False
    email = email.split("@")
    valid = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789."
    for characters in email[0]:
        if characters not in valid:
            return False
    if '.' not in email[1]:
        return False
    domain = email[1].split(".")
    valid = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    for d in domain:
        if len(d) < 1:
            return False
        for char in d:
            if char not in valid:
                return False

    return True

f = open("input.txt")
string = f.read().split('\n')
f.close()
for i in range(1,len(string)):
    if is_website(string[i]):
        print("Web",i,sep = ', ')
    elif is_email(string[i]):
        print("Email",i,sep = ', ')
    else:
        print("Invalid",i,sep = ', ')
    

