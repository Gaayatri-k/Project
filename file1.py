import os
import csv
Filename="studentsmanagement.csv"
if not os.path.exists(Filename):
    with open(Filename,mode="w",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["ID","Name","Age","Department"])