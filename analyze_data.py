# Student Data Analysis

import csv

with open("student_data.csv", "r") as file:
    data = list(csv.DictReader(file))

print("--- Student Performance Dataset ---")

for student in data:
    print(
        student["Name"],
        "- Marks:", student["Previous_Marks"],
        "- Attendance:", student["Attendance"],
        "- Performance:", student["Performance"]
    )

print("\nTotal Students:", len(data))

excellent = sum(1 for student in data if student["Performance"] == "Excellent")
good = sum(1 for student in data if student["Performance"] == "Good")
needs_improvement = sum(
    1 for student in data if student["Performance"] == "Needs Improvement"
)

print("Excellent:", excellent)
print("Good:", good)
print("Needs Improvement:", needs_improvement)
