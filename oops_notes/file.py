class Report:
    def __init__(self,filename):
        self.file = open(filename,"w")
        print("File opened")

    def write_data(self,text):
        self.file.write(text)

    def __del__(self):
        self.file.close()
        print("Close")

r1 = Report("report.txt")
r1.write_data("Python constur ec")
with open("report.txt","r") as f:
    print(f.read())

del r1