s = "Python ist sooo eine tolle Programmiersprache!"
t = set()
d = { }
for v in s:
  t.add(v)

for x in t:
  if x != ' ':
    d[x]=s.count(x)

print(list(d))
