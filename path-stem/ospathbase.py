import os

file = os.path.basename("/path/to/file.txt")
base = os.path.splitext(file)

print(base[0])
