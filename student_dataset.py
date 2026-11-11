import pandas as pd
import random

random.seed(42)

num_students = 100
departments = ['Computer Science', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Accounting', 'Mass Communication', 'Business Administration']
levels = ['100', '200', '300', '400']

data = []
matric_start = 14632  # to start from 24/14632

for i in range(num_students):
    matric_number = f"24/{matric_start + i}"  # e.g., 24/14632, 24/14633...
    department = random.choice(departments)
    level = random.choice(levels)
    attendance = round(random.uniform(45.0, 100.0), 2)
    avg_score = round(random.uniform(35.0, 98.5), 2)

    data.append([matric_number, department, level, attendance, avg_score])

df = pd.DataFrame(data, columns=['Matric Number', 'Department', 'Level', 'Attendance Percentage', 'Average Examination Score'])

df.to_csv('fictional_student_dataset.csv', index=False)

print("Dataset created successfully!")
print(df.head(10))