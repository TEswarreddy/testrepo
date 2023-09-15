names=["eswar","rukesh","hemanth","ramjashwanth","rosi","vamsi"]
import random

student_scores={student:random.randint(1,100) for student in names}

print(student_scores)

passed_students={student:scores for (student,scores) in student_scores.items() if scores>=60}
print(passed_students)
