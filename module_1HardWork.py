grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
A = sorted(list(students))
B = sum((grades [0]))/len(grades[0])
C = sum((grades [1]))/len(grades[1])
D = sum((grades [2]))/len(grades[2])
E = sum((grades [3]))/len(grades[3])
F = sum((grades [4]))/len(grades[4])
C = {A[0]:B, A[1]:C, A[2]:D, A[3]:E, A[4]:F}
print('Средний бал', C[input("Напишите имя студента: ")])    # усложнил готовое решение
print('Cредний балл каждого ученика:', C)

