import re

f = open("input.txt", "r")
s = f.read()
s = re.sub("[^0-9a-zA-Z']+", ' ', s).rstrip()
f.close()
f1 = open("output.txt", "w")
f1.write(s)
f1.close()
