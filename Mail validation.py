#MAIL VALIDATIONS

email=input("enter your email :")#g@g.in
""" @ should be only once,no uppercase,first letter alphabet,
   dot position from ending is 3 rd or 4th


                """
k,j,d=0,0,0
if len(email)>=6:
    #first element is always alphabet
    if email[0].isalpha():
        #will use membership operator to check @ is present or not
        if ("@" in email) and (email.count("@")==1):
            #it should no space in between
            for i in email:
                if i==i.isspace():
                    k=1
                #if it's not space will check alphabet hai kya
                elif i.isalpha():
                    if i==i.upper():
                        #it will convert it into upper and check with original 
                        #if original is in uppercase then that will be detected
                        j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                        
            if k==1 or j==1 or d==1:
                print("Wrong Email 5")
        else:
            print("wrong Email 4")


            """ (Dot is not at both positions 3rd and 4 th)
            if it's .in then dot position is at 3rd place from last 
           #and if it's .com then dot position is at 4 th place from end
            #ex-or =TT:F,FF:F,TF OR FT:T"""
            if (email[-4]==".")^(email[-3]=="."):
                pass
            else:
                print('wrong Email 3')
    else:
        print('wrong email 2')
else:
    print("wrong Email 1 ")
