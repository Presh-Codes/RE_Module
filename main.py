import re

txt = "My name is Precious Okeypraise"
x = re.search("^My.*Okeypraise$", txt)
print(x)
y = re.findall("y", txt)
print(y)
v = re.split("\s", txt)
print(v)
b = re.sub("\s", "0", txt, 2)
print(b)
