import numpy as np

marks = np.random.randint(0, 101, size=(10, 5))
student_totals = np.sum(marks, axis=1)
student_avgs = np.mean(marks, axis=1)
subject_avgs = np.mean(marks, axis=0)
best_student_idx = np.argmax(student_avgs)
pass_count = np.sum(student_avgs >= 50)
status = np.where(student_avgs >= 50, "Pass", "Fail")

print("Student Averages:", student_avgs)
print("Pass/Fail Status:", status)
