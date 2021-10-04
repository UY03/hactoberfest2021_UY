import csv
lis=[]
def entercsv(filename):
    infile=open(filename,"w",newline='')
    while True:
        lis=[]
        name_=input("Enter friend's Name: ")
        if name_=="":
            break
        ph_=input("Enter friend's Phone Number: ")
        lis.append(name_.capitalize())
        lis.append(ph_)
        csv.writer(infile).writerow(lis)
    infile.close()
entercsv("myfile.csv")