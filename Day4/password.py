def valid_password(password):
    
    #print(password, len(password))
    
    if  len(password) < 8 or len(password) > 12:
        #print("length bad", len(password) )
        return "bad"
    
    #print("continuing ", len(password))

    lcnt = 0
    ucnt = 0
    ncnt = 0
    
    for mychar in password:
    #    print(mychar, mychar.lower(), mychar.upper(), mychar.isnumeric())
        
        if mychar.isnumeric():
            ncnt+=1
            continue
        
        if mychar == mychar.lower():
            lcnt+=1
        
        if mychar == mychar.upper():
            ucnt+=1
            
    #print(lcnt, ucnt, ncnt)
            
    if lcnt >= 2 and ucnt >= 3 and ncnt >= 2:
        print("Good Password")
        return "good"
    else:
        print("Bad Password")
        return "bad"

valid_password('z3F9Si8I')
valid_password('DbaBAcC231')
valid_password('leZ3eippn8')
valid_password('el38ppnEZi')     # bad not enough uppercase letters
valid_password('zB3E8ZOO')
valid_password('oaLvD1lyey')
valid_password('IzFIS8z338SiFi') # bad too many characters
valid_password('8iIzS3F')        # bad not enough characters


### 
def check_password(password):
    print(password, len(password))
    
    if  len(password) < 6 or len(password) > 12:
        return False

    lcnt = 0
    ucnt = 0
    ncnt = 0
    scnt = 0
    
    for mychar in password:
    #    print(mychar, mychar.lower(), mychar.upper(), mychar.isnumeric())
        
        if mychar.isnumeric():
            ncnt+=1
            continue
        
        if mychar.isalpha():
            if mychar.islower():
                lcnt+=1
        
            if mychar.isupper():
                ucnt+=1
        else:
            scnt+=1
        
    print(lcnt, ucnt, ncnt, scnt)
            
    if lcnt >= 1 and ucnt >= 1 and ncnt >= 1 and scnt >= 1:
        print("Good Password")
        return True
    else:
        print("Bad Password")
        return False
    