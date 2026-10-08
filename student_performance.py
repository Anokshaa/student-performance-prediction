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
