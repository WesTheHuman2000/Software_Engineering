total_number = int(input("Enter a number "))

number_list =[]
total_num = 0
for i in range(total_number):
    new_number = int(input(f"Enter number {i+1} "))
    number_list.append(new_number)
    total_num+=new_number

print(total_num / len(number_list))
print(number_list)
