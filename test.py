def makenew(mystr):
    newstr = " " 
    count = 0
    for i in mystr:
        if count%2 !=0:
            newstr = newstr+str(count) 
        else:
            if i.islower():
                newstr = newstr+i.upper()
            else:
                newstr = newstr+i 
        count +=1
    newstr = newstr+mystr[:1]
    print ("The new string is :",newstr)
#makenew('sTUdeNT')


