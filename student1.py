import csv
import os
import sys
import statistics
Filename="studentsmanagement.csv"
Deletedfile="students_deleted.csv"
Reportfolder="reports"
def read_students():
    if not os.path.exists():
        with open(Filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Roll_No","Name","Branch","Year","Gender","Age",
                             "Attendance","Mid1","Mid2","Quiz","Final"])
    with open(Filename, newline="") as f:
        return list(csv.DictReader(f))
