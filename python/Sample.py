
finallist=[]

f=open("cap_II.txt","rt")

for x in range(0,100):
    list1=f.readline()
    finallist.append(list1)

for i in range(0,100):
    name=""
    marks=""
    sarname=""
    settype=""

    row=finallist[i]
    word=row.split(" ",11)

    sarname=word[4]
    name=word[5]
    marks=marks+word[2]
    settype=word[10]

    print(str(i+1)+" "+name+" "+sarname+" = "+marks)    

f.close()
