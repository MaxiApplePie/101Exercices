class Path():
	pass

s = Path("/Users/thibh/Documents/test.txt")
print(s.dirname().dirname())
print(s.name)
print(s.ext)