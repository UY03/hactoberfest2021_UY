import time
def copyfile(filename):
    infile=open(filename)
    for line in infile:
        print(line,end="")
        time.sleep(0.5)
    infile.close()
copyfile("HumptyDumpty.txt")