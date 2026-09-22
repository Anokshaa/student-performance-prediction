# Student Performance Prediction

name = input("Enter student name: ")
marks = float(input("Enter previous marks: "))
attendance = float(input("Enter attendance percentage: "))

if marks >= 75 and attendance >= 75:
    performance = "Excellent"
elif marks >= 50 and attendance >= 60:
    performance = "Good"
else:
    performance = "Needs Improvement"

print("\n--- Student Performance Result ---")
print("Student Name:", name)
print("Previous Marks:", marks)
print("Attendance:", attendance, "%")
print("Performance:", performance)
