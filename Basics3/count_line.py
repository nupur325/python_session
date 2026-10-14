with open("file.txt") as f:
    line=f.readlines()
print("Total number lines ",len(line))
print("2nd line",line[1])
print("3rd line",line[2])