try:
    i=1
    j=10/i
    values=[1,2]
    sum(values)
except TypeError:
    print("Type Error")
except ZeroDivisionError:
    print("ZeroDivisionError")
    j=0
else:print("Else")
finally:print("Final block will be excuted")
print(j)
print("End")