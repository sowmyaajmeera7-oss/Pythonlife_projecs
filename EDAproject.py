import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create Student Dataset
data = {
    "Student": ["A", "B", "C", "D", "E",
                "F", "G", "H", "I", "J"],
    "Age": [18, 19, 18, 20, 19, 18, 20, 19, 18, 20],
    "Gender": ["Male", "Female", "Male", "Female",
               "Male", "Female", "Male", "Female",
               "Male", "Female"],
    "Maths": [85, 90, 65, 70, 95, 55, 80, 75, 60, 88],
    "Science": [80, 85, 70, 75, 90, 60, 85, 80, 65, 92],
    "English": [75, 88, 60, 72, 85, 55, 78, 82, 68, 90],
    "Attendance": [90, 95, 80, 85, 98, 70, 88, 92, 75, 96]
}

df = pd.DataFrame(data)

# 2. Display Dataset
print("\nSTUDENT DATASET")
print(df)

# 3. Dataset Information
print("\nDATASET INFORMATION")
df.info()

# 4. Statistical Analysis
print("\nSTATISTICAL SUMMARY")
print(df.describe())

# 5. Check Missing Values
print("\nMISSING VALUES")
print(df.isnull().sum())

# 6. Calculate Average Marks
df["Average"] = df[
    ["Maths", "Science", "English"]
].mean(axis=1)

# 7. Calculate Total Marks
df["Total"] = df[
    ["Maths", "Science", "English"]
].sum(axis=1)

# 8. Pass or Fail
df["Result"] = np.where(
    (df["Maths"] >= 35) &
    (df["Science"] >= 35) &
    (df["English"] >= 35),
    "Pass",
    "Fail"
)

# 9. Final Dataset
print("\nFINAL STUDENT ANALYSIS")
print(df)

# 10. Subject Average
print("\nSUBJECT AVERAGE")
print(df[["Maths", "Science", "English"]].mean())

# 11. Highest Marks
print("\nHIGHEST MARKS")
print(df[["Maths", "Science", "English"]].max())

# 12. Lowest Marks
print("\nLOWEST MARKS")
print(df[["Maths", "Science", "English"]].min())

# 13. Pass and Fail Count
print("\nPASS AND FAIL COUNT")
print(df["Result"].value_counts())

# 14. Bar Chart
df[["Maths", "Science", "English"]].mean().plot(
    kind="bar",
    title="Average Marks by Subject"
)
plt.ylabel("Average Marks")
plt.show()

# 15. Student Performance Chart
plt.figure(figsize=(10, 5))
plt.bar(df["Student"], df["Average"])
plt.title("Student Average Performance")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()

# 16. Attendance Analysis
plt.figure(figsize=(10, 5))
plt.bar(df["Student"], df["Attendance"])
plt.title("Student Attendance")
plt.xlabel("Students")
plt.ylabel("Attendance Percentage")
plt.show()

# 17. Correlation Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(
    df[["Maths", "Science", "English",
        "Attendance", "Average"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Student Performance Correlation")
plt.show()

# 18. Save Final Dataset
df.to_csv("student_analysis.csv", index=False)

print("\nEDA PROJECT COMPLETED SUCCESSFULLY!")
print("CSV File Saved Successfully!")