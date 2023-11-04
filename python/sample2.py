
finallist=[]
lenth=[]
f=open("cap_3.txt","rt")

for x in range(0,100):
    list1=f.readline()
    finallist.append(list1)

for i in range(0,100):
    name=""
    marks=""
    sarname=""
    seat="^"

    row=finallist[i]
    word=row.split(" ",11)

    if seat in row:
        name=word[5]
        sarname=word[4]
        marks=word[10]
        print(str(i)+" "+name)
        lenth.append(name)

print(len(lenth))
f.close()
