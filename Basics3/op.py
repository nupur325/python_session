with open("file.txt") as f:
    s = f.read()
    words = s.split()
    print("Total words",len(words))
    print("Unique words",set(words))