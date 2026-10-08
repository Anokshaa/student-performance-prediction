# Student Performance Prediction and Analysis

print("===== Student Performance Prediction =====")

name = input("Enter student name: ")
marks = float(input("Enter previous marks: "))
attendance = float(input("Enter attendance percentage: "))
study_hours = float(input("Enter study hours per day: "))

# Predict performance
if marks >= 75 and attendance >= 75 and study_hours >= 5:
    performance = "Excellent"
    recommendation = "Maintain your current study habits and performance."

elif marks >= 50 and attendance >= 60 and study_hours >= 3:
    performance = "Good"
    recommendation = "Increase study hours and maintain regular attendance."

else:
    performance = "Needs Improvement"
    recommendation = "Improve attendance, marks and study regularly."

# Display result
print("\n===== Student Performance Result =====")
print("Student Name:", name)
print("Previous Marks:", marks)
print("Attendance:", attendance, "%")
print("Study Hours:", study_hours, "hours/day")
print("Performance:", performance)
print("Recommendation:", recommendation)
# Student Dataset Analysis

import csv

print("\n===== Student Dataset Analysis =====")

total_students = 0
total_marks = 0
total_attendance = 0
total_study_hours = 0

excellent = 0
good = 0
needs_improvement = 0

with open("student_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_students += 1
        total_marks += float(row["Previous_Marks"])
        total_attendance += float(row["Attendance"])
        total_study_hours += float(row["Study_Hours"])

        if row["Performance"] == "Excellent":
            excellent += 1
        elif row["Performance"] == "Good":
            good += 1
        else:
            needs_improvement += 1

print("Total Students:", total_students)
print("Average Marks:", round(total_marks / total_students, 2))
print("Average Attendance:", round(total_attendance / total_students, 2), "%")
print("Average Study Hours:", round(total_study_hours / total_students, 2))

print("\nPerformance Count:")
print("Excellent:", excellent)
print("Good:", good)
print("Needs Improvement:", needs_improvement)
