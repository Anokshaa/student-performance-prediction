# Student Performance Prediction

print("===== Student Performance Prediction =====")

name = input("Enter student name: ")
marks = float(input("Enter previous marks: "))
attendance = float(input("Enter attendance percentage: "))
study_hours = float(input("Enter study hours per day: "))

# Predict performance
if marks >= 75 and attendance >= 75 and study_hours >= 5:
    performance = "Excellent"
    suggestion = "Maintain your current study habits and performance."
    target_marks = min(marks + 5, 100)

elif marks >= 50 and attendance >= 60 and study_hours >= 3:
    performance = "Good"
    suggestion = "Increase study hours and maintain regular attendance."
    target_marks = min(marks + 10, 100)

else:
    performance = "Needs Improvement"
    suggestion = "Improve attendance, marks and study regularly."
    target_marks = min(marks + 15, 100)

# Display result
print("\n===== Student Performance Result =====")
print("Student Name:", name)
print("Previous Marks:", marks)
print("Attendance:", attendance, "%")
print("Study Hours:", study_hours, "hours/day")
print("Performance:", performance)
print("Improvement Suggestion:", suggestion)
print("Target Marks:", target_marks)
