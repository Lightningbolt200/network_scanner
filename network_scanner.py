import subprocess
import os
flag=0
for ping in range(0,255):
    if(flag==3):
        print("\n\t----------no more host available----------")
        exit()
    address = "192.168.1." + str(ping) 
    res = subprocess.call(['ping','-n','1', address])
    if res == 0:
        os.system("ping -n 1 "+address+" > your_txt_file_path\ip.txt")
        f=open("your_txt_file_path\ip.txt","r")
        x=f.readline()
        x=f.readline()
        x=f.readline()
        b=x[41:-2]
        if(b=="unreachable"):
            flag=flag+1
        f.close()
        print( "\nping to", address, "OK")
        proc = subprocess.Popen(["nslookup", address], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        c=out.decode().split()
        print(c)
        if(c[5]==address):
            print("no device found")
        else:
            print("host name: "+c[5])
    elif res == 2: 
        print("no response from", address) 
    else: 
        print("\nping to", address, "failed!")
        print("host offline")
    
