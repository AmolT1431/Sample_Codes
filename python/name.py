finallist=[]
s=0
filename="test.txt"

f=open(filename,"rt")
s=len(f.readlines())
f.close()

f=open(filename,"rt")
student=open("student.txt","w")

for x in range(0,s):
    list1=f.readline()
    finallist.append(list1)

for i in range(0,len(finallist)):
    name=""
    marks=""
    sarname=""

    row=finallist[i]
    word=row.split(" ",10)

    sarname=word[2]
    name=word[3]
    marks=word[6]

    print(str(i+1)+" "+name+" "+sarname+" = "+marks)    
    student.write(sarname+" "+name+" = "+marks+"\n")

f.close()
