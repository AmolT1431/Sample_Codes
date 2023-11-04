f = open("ips.txt", "a")
for x in range(255):
    v=str(x)
    f.write("192.168.1."+v+"\n")

f.close()