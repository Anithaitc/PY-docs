import re
str="anithapoluruani@gmail.com"
a=["anithapoluruani","@","gmail",".","com"]
for i in a:
    print(i)
    result=re.search(i,str)
    if result!=None:
        print("Matching...")
    else:
        print("Not Matching..")