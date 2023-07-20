s=input("Nhap S: ")
if not(s.endswith("!!!")):
    if(s.endswith("!!")):
        s=s+'!'
    elif(s.endswith("!")):
        s=s+"!!"
    else:
        s=s+("!!!")
print("Chuoi S sau khi xu ly:",s)