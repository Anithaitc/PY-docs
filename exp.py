#lists
a=[19,75,80,83,102]
print(type(a))
print(len(a))
print(max(a))
print(min(a))
print("")

#tuples
b= ("s", 19, "r", 18, "a", 1,"h",0.8,"p",0.16)
print(type(b))
print(b)
print(b[4])
#b[3]="ani"
print("")

#sets
c={1,2,3,4}
print(type(c))
#c.discard()
#c.remove()
#c.pop()
#c.clear()
print(c)
print("")

#dict
d={"name":"ani","num":80,"code":3.43}
print(type(d))
print(d)
print(d.get("name"))
d.update({"num":20})
print(d)

