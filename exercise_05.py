print('Hello world')

number_list =[]
number_list2=[]
common_list=[]

for i in range(5):
    user_input= int(input('Enter a number for the first list: '))
    number_list.append(user_input)

for i in range(5):
    user_input= int(input('Enter a number for the second list: '))
    number_list2.append(user_input)

for i in number_list:
    for x in number_list2:
        if i == x:
            common_list.append(i)
    


print('First list: ',number_list)
print('Second list: ',number_list2)
print('Common list: ', common_list)