fileptr=open("newOne.txt")
if fileptr:
    print("Success")
else:
    print("fail")
with open("newOne.txt") as m:
    p=m.write("java document added now")
    print(p)