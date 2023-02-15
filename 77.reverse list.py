
lst = [10, 11, 12, 13, 14, 15]

l = []


for i in lst:
	
	l.insert(0, i)

print(l)
print("---")
alst = [10, 11, 12, 13, 14, 15]
alst.reverse()
print("Using reverse() ", alst)

print("Using reversed() ", list(reversed(lst)))

