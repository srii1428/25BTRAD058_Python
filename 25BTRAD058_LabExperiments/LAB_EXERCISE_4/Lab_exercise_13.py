# CSV-based payroll management system.
# * CSV-Based Payroll Management System: Develop a Python program to read employee records from a
# CSV file, calculate gross salary and applicable deductions, and generate salary summaries
# * Analyze payroll requirements, design calculation logic, process CSV records, validate data, and verify
# salary calculations. (CT)
# * Apply the program to a sample organization&#39;s payroll process and interpret the generated salary summaries. (RWE)

import csv
data = [
["Priya", 20000, 5000],
["Rahul", 30000, 10000],
["Anu", 25000, 5000]
]
with open("employees.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Name", "Basic", "HRA"])
    w.writerows(data)
    with open("employees.csv", "r") as f:
        for emp in csv.DictReader(f):
            gross = int(emp["Basic"]) + int(emp["HRA"])
            net = gross - gross * 0.10
            print(emp["Name"], "Gross:", gross, "Net:", net)