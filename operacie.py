operacia = input("zadaj rdo kalkulacky:")
def uprav():
    global operacia
    celk =0
    for i in range(len(operacia)):
            if operacia[i] in "/*-+":
                celk += 1

    print(operacia,"\n")
    for nic in range(celk):

            naj_znam = "+"
            poc_znam = 0


            i = 0
            while i < len(operacia):
            
                if operacia[i] in "/*-+":
                    if operacia[i-1] == "-" and operacia[i] == "-":
                        
                        operacia=operacia[:i-1]+"+"+operacia[i+1:]
                    elif (operacia[i-1] == "+" and operacia[i] == "-") or (operacia[i-1] == "-" and operacia[i] == "+"):
                        operacia=operacia[:i-1]+"-"+operacia[i+1:]
                        


                i +=1

        
            for p in range(len(operacia)):
            
                if operacia[p] in "/*-+":
                
                    if  "/*-+".index(operacia[p]) <= "/*-+".index(naj_znam):
                        
                        naj_znam = operacia[p]
                        poc_znam = p

                        
                else:
                    minule_znam = ""
            def najdenie_cisla(pocet):
                global operacia
                c1 = ""
                c2 = ""
                do = -1
                od = -1
                for p in range(pocet):

                    if operacia[p] in "0123456789.":
                        c1 += operacia[p]
                        if do == -1:
                            do = p
                    else:
                        do = -1
                        c1 = ""
                for p in range(pocet+1,len(operacia),1):
                        print(p,operacia[p],od)
                        if operacia[p] in "0123456789.":
                            c2 += operacia[p]
                            
                            od = p
                        else:
                            break
                return c1,c2,do-1,od


            def spocitanie(znamienko,c1,c2,od,do):
                global operacia
                if znamienko == "/":
                    print(operacia[:od+1],"  a  ",str(round(c1/c2,4))," a  ",operacia[do+1:])
                    operacia=operacia[:od+1]+str(round(c1/c2,4))+operacia[do+1:]
                if znamienko == "*":
                        print(operacia[:od+1],"  a  ",str(round(c1*c2,4))," a  ",operacia[do+1:])
                        operacia=operacia[:od+1]+str(round(c1*c2,4))+operacia[do+1:]
                if znamienko == "+":
                        print(operacia[:od+1],"  a  ",str(round(c1+c2,4))," a  ",operacia[do+1:])
                        operacia=operacia[:od+1]+str(round(c1+c2,4))+operacia[do+1:]
                if znamienko == "-":
                        print(operacia[:od+1],"  a  ",str(round(c1-c2,4))," a  ",operacia[do+1:])
                        operacia=operacia[:od+1]+str(round(c1-c2,4))+operacia[do+1:]


            c1,c2,od,do =najdenie_cisla(poc_znam)
            print(naj_znam,poc_znam,c1,c2,od,do,":")
            spocitanie(naj_znam,float(c1),float(c2),od,do)


            print(operacia)
            print("")




uprav()