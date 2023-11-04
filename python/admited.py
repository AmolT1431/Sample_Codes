
finallist=[]

f=open("cap_3_ecs.txt","rt")

for x in range(0,100):
    list1=f.readline()
    finallist.append(list1)

for i in range(0,100):
    name=""
    marks=""
    sarname=""
    seat="&"

    row=finallist[i]
    word=row.split(" ",11)
    if seat in row:
        sarname=word[4]
        name=word[5]
        marks=word[2]

        print(str(i+1)+" "+name+" "+sarname+" = "+marks)
    

f.close()
