import re
txt="rashad"
x=re.search("rash?.d",txt)
if x:
    print("found")
else:
    print("not found")