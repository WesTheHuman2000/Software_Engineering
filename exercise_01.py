#Worked with Vishag, Riley, Ajay, and Pasi

number_grade = input('Enter a grade from 0 to 100: ')
print(number_grade)
if int(number_grade) >=90:
    print('You got an A')
elif int(number_grade)>=80:
    print('You got a B')
elif int(number_grade)>=70:
    print("You got a C")
elif int(number_grade):
    print('You got a D')
else:
    print('You got an F')
