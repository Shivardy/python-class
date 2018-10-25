import csv
file = open("/Users/shivareddy/Desktop/python/work/files/facultyindb.csv","rb")
reader = csv.reader(file)
dbheader = next(reader)
dbdata = [row for row in reader]

file = open("/Users/shivareddy/Desktop/python/work/files/facultyfromhr.csv","rb")
reader = csv.reader(file)
hrheader = next(reader)
hrdata = [row for row in reader]

dbnames=[]
for row in dbdata:
    dbnames.append(row[5])

return_path = "output/add_these_faculty_to_raisersedge.csv"
file = open(return_path,'w')
writer = csv.writer(file)
writer.writerow(hrheader)

for row in hrdata:
    if (row[5] not in dbnames):
        writer.writerow(row)








