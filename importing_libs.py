import re
text="Welcome to python"
a=re.search("to",text)
if a:
    print("Word is there")
else:
    print("word is not there")