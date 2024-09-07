grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_sort=sorted(students)

grades_a=[]
for num in grades:
    s=sum(num)/len(num)
    grades_a.append(s)
dict=dict(zip(students_sort,grades_a))
print(dict)
