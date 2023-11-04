# From the Python course in 1ITF
from ast import Dict
import itertools


students = ["Ann","Bert","Chris","Dave"]
for student in students:
     print(student)
for i in range(len(students)):
    print (i, students[i])
for i in range(len(students)):
    print (i+1, students[i])
#more Pythonic way to add a counter is using built-in enumerate() function
for i, student in enumerate(students):
    print(i, student)
#by default the index counter starts at 0 --> can be changed
for i, student in enumerate(students, start=1):
    print(i, student)
#enumerate returns list of tuples
print(list(enumerate(students)))

grades=["A","B","A","C"]
# From the Python course in 1ITF
for i in range(len(students)):
    print(i+1, students[i],grades[i])
#more Pythonic way to achieve this is by using built-in zip() function
for student, grade in zip(students,grades):
    print(student,grade)
#zip returns list of tuples
print(list(zip(students, grades)))
#in case of unequal length, shortest iterable is used
print(list(zip(students, grades, range(2))))
#with index
for i,(student, grade) in enumerate(zip(students,grades)):
    print(i,student,grade)

#example map
#function to transform grade in mark
def transform(grade):
    lookup_dict = {"A":8,"B":6,"C":4,"D":2} 
    return lookup_dict.get(grade)

# From the Python course in 1ITF
marks=[]
for grade in grades:
    marks.append(transform(grade))
print(marks)

#more Pythonic way to call function by using map() 
marks = list(map(transform,grades))
print(marks)

#example map & filter
#function returns true in case of A,B
def passed(grade):
    return grade in ("A", "B")

# From the Python course in 1ITF
results = []
for grade in grades:
    results.append(passed(grade))
print(results)
#more Pythonic way to achieve this is by using built-in map() function
results = list(map(passed,grades))
print(results)
# Filter example
passed_grades = list(filter(passed,grades))
print(passed_grades)

#lambda functions in combination with map and filter
grades=["A","B","A","C"]
passed_grades = list(filter(lambda grade:grade in("A","B"),grades))
print(passed_grades)
marks = list(map(lambda grade:{"A":8,"B":6,"C":4,"D":2}.get(grade),grades))
print (marks)

#lambda functions
print((lambda x,y:x+y)(2,3))
print((lambda x,y,z=3:x+y+z)(2,3))
print((lambda *args:sum(args))(1,2,3,4))


#list comprehension replacing map()
grades=["A","B","A","C"]
marks = [{"A":8,"B":6,"C":4,"D":2}.get(grade) for grade in grades]
print(marks)
results = ["Pass" if grade in("A","B") else "Fail" for grade in grades]
print(results)
#list comprehension replacing filter()
passed_grades = [ grade for grade in grades if grade in ("A","B") ]
print (passed_grades)


#list comprehension
list = [i*i for i in range(1,6)]
squares = [i**2 for i in range(1,11)]
print(squares)
even_numbers = [i for i in range(1,11) if i%2==0]
print(even_numbers)








