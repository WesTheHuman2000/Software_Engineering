number_list = []

for i in range(10):
    user_input = int(input(f'Enter number {i+1}: '))
    number_list.append(user_input)

#for x in range(number_list):
#    if user_input[x] %2 == 0:

print(set(number_list))