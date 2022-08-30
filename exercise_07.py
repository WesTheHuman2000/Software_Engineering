user_input= input('Enter a number or QUIT to quit ')
even_numbers = []
odd_numbers = []

while user_input != 'QUIT':
    if int(user_input) % 2 ==1:
        odd_numbers.append(int(user_input))
    else:
        even_numbers.append(int(user_input))
    user_input=input('Enter a number or QUIT to quit ')

print(even_numbers)
print(odd_numbers)