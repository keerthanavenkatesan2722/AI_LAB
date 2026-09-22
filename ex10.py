# AI-Based Student Stress-Free Study Planner
# and Performance Predictor
from sklearn.tree import DecisionTreeClassifier
# -----------------------------------------
# TRAINING DATA
# -----------------------------------------
# Features:
# [Study Hours, Attendance, Assignment Completion, Previous Marks]
X = [
    [1, 60, 50, 40],
    [2, 65, 60, 45],
    [3, 70, 70, 55],
    [4, 75, 75, 60],
    [5, 80, 85, 70],
    [6, 85, 90, 78],
    [7, 90, 95, 85],
    [8, 95, 100, 92]
]
# Performance categories
y = [
    "Needs Improvement",
    "Needs Improvement",
    "Average",
    "Average",
    "Good",
    "Good",
    "Excellent",
    "Excellent"
]
# -----------------------------------------
# TRAIN THE AI MODEL
# -----------------------------------------
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)
# -----------------------------------------
# STUDENT DETAILS
# -----------------------------------------
print("==============================================")
print(" AI-BASED STUDENT STUDY PLANNER")
print(" AND PERFORMANCE PREDICTOR")
print("==============================================")
name = input("Enter student name: ")
study_hours = float(
    input("Enter daily study hours: ")
)
attendance = float(
    input("Enter attendance percentage: ")
)
assignment = float(
    input("Enter assignment completion percentage: ")
)
previous_marks = float(
    input("Enter previous average marks: ")
)
# -----------------------------------------
# PERFORMANCE PREDICTION
# -----------------------------------------
student_data = [[
    study_hours,
    attendance,
    assignment,
  previous_marks
]]
prediction = model.predict(student_data)[0]
# -----------------------------------------
# SUBJECT DETAILS
# -----------------------------------------
subjects = [
    "Artificial Intelligence",
    "Data Structures",
    "Object-Oriented Programming",
    "Operating Systems",
    "Fundamentals of Internet of Things"
]
marks = []
print("\n----------------------------------------------")
print(" ENTER SUBJECT MARKS")
print("----------------------------------------------")
for subject in subjects:
    mark = float(
        input("Enter " + subject + " marks: ")
    )
    marks.append(mark)
# -----------------------------------------
# CALCULATE AVERAGE
# -----------------------------------------
total = sum(marks)
average = total / len(marks)
# -----------------------------------------
# IDENTIFY WEAK AND STRONG SUBJECTS
# -----------------------------------------
weak_subjects = []
strong_subjects = []
for i in range(len(subjects)):
    if marks[i] < 50:
        weak_subjects.append(subjects[i])
    elif marks[i] >= 75:
        strong_subjects.append(subjects[i])
# -----------------------------------------
# DETERMINE STRESS LEVEL
# -----------------------------------------
if study_hours < 2 or len(weak_subjects) >= 3:
    stress = "High"
elif study_hours < 4 or len(weak_subjects) == 2:
    stress = "Moderate"
else:
    stress = "Low"
# -----------------------------------------
# STUDENT PERFORMANCE REPORT
# -----------------------------------------
print("\n==============================================")
print(" STUDENT PERFORMANCE REPORT")
print("==============================================")
print("Student Name    :", name)
print("Average Marks   :", round(average, 2))
print("Predicted Level :", prediction)
print("Stress Level    :", stress)
# -----------------------------------------
# WEAK SUBJECT ANALYSIS
# -----------------------------------------
print("\n----------------------------------------------")
print(" WEAK SUBJECT ANALYSIS")
print("----------------------------------------------")
if weak_subjects:
    print("Subjects needing improvement:")
    for subject in weak_subjects:
        print("-", subject)
else:
    print("No weak subjects found.")
# -----------------------------------------
# STRONG SUBJECTS
# -----------------------------------------
print("\n----------------------------------------------")
print(" STRONG SUBJECTS")
print("----------------------------------------------")
if strong_subjects:
    for subject in strong_subjects:
        print("-", subject)
else:
    print("Keep practicing all subjects.")
# -----------------------------------------
# PERSONALIZED STUDY PLAN
# -----------------------------------------
print("\n==============================================")
print(" PERSONALIZED STUDY PLAN")
print("==============================================")
if weak_subjects:
    print("\nFocus more on weak subjects:")
    for subject in weak_subjects:
        print("-", subject)
    if study_hours >= 4:
        print("\nDaily Study Schedule:")
        print("1.5 Hours - Weak Subjects")
        print("1 Hour   - Other Subjects")
        print("1 Hour   - Revision")
        print("0.5 Hour - Practice / Quiz")
    elif study_hours >= 2:
        print("\nDaily Study Schedule:")
        print("1 Hour   - Weak Subjects")
        print("0.5 Hour - Other Subjects")
        print("0.5 Hour - Revision")
    else:
        print("\nDaily Study Schedule:")
        print("30 Minutes - Weak Subjects")
        print("20 Minutes - Revision")
        print("10 Minutes - Practice")
else:
    print("Maintain your current study routine.")
    print("Spend time on revision and practice.")
# -----------------------------------------
# STRESS-FREE STUDY TIPS
# -----------------------------------------
print("\n==============================================")
print(" STRESS-FREE STUDY TIPS")
print("==============================================")
if stress == "High":
    print("• Take short breaks between study sessions.")
    print("• Focus on one subject at a time.")
    print("• Avoid studying continuously for long hours.")
    print("• Give priority to weak subjects.")
elif stress == "Moderate":
    print("• Follow a fixed study timetable.")
    print("• Take regular short breaks.")
    print("• Practice weak subjects daily.")
else:
    print("• Continue your regular study routine.")
    print("• Revise important topics regularly.")
    print("• Practice previous questions.")
# -----------------------------------------
# FINAL RESULT
# -----------------------------------------
print("\n==============================================")
print(" FINAL RESULT")
print("==============================================")
print("Student         :", name)
print("Performance     :", prediction)
print("Average Marks   :", round(average, 2))
print("Stress Level    :", stress)
print("\nPersonalized study plan generated successfully!")
print("==============================================")
