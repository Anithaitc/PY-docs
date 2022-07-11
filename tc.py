try:
    fileptr=open("newOne.txt")
except:
    print("pass")
finally:
    fileptr.close()
    print("done")