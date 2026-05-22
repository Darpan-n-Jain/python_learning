import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
samples = 5000

study_hours = np.random.randint(1, 10, samples)
marks = np.random.randint(35, 100, samples)
attendance = np.random.randint(50, 100, samples)

unique_hours = np.unique(study_hours)
avg_marks = [marks[study_hours == h].mean() for h in unique_hours]

plt.figure()
plt.bar(unique_hours, avg_marks)
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.title("Bar Plot: Average Marks vs Study Hours")
plt.show()

sorted_marks = np.sort(marks)

plt.figure()
plt.plot(sorted_marks)
plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.title("Line Plot: Marks Distribution")
plt.show()

plt.figure()
plt.scatter(study_hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Scatter Plot: Study Hours vs Marks")
plt.show()

plt.figure()
plt.hist(marks, bins=20)
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.title("Histogram: Marks Distribution")
plt.show()

grades = ['A', 'B', 'C', 'D', 'F']
grade_counts = [
    np.sum(marks >= 85),
    np.sum((marks >= 70) & (marks < 85)),
    np.sum((marks >= 55) & (marks < 70)),
    np.sum((marks >= 40) & (marks < 55)),
    np.sum(marks < 40)
]

plt.figure()
plt.pie(grade_counts, labels=grades, autopct='%1.1f%%')
plt.title("Pie Chart: Grade Distribution")
plt.show()
