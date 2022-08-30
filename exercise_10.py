#split string into words
#split words into lists of three


user_input = input('Enter a string: ')

#user_string_list = user_input.split()
char_list = []
short_char_list =[]


for letter in user_input:
    char_list.append(letter)
print(char_list)

list_length = len(char_list)


normal_run= list_length // 3
remainder = list_length % 3
current_index=0
for j in range(len(char_list)):
    print("The character for index ", j, " is ", char_list[j])

for i in range(normal_run):
    temp = []
    x=0
    while x<3:
    #    print('Current index is: ',current_index, ' and x is: ', x)
        temp.append(char_list[current_index])
    #    print(char_list[current_index])
        current_index+=1
        x+=1
    short_char_list.append(temp)
temp = []    
for y in range(remainder):
    
    print('The current index is ', current_index)
    temp.append(char_list[current_index])
    current_index+=1
short_char_list.append(temp)
print(short_char_list); 

#while list_length % 3 == 0:
#    for i in range(3):
#        short_char_list.append(char_list[i])
#    list_length+=3
#    print('hi')   
#maybe run the program by 3s until there is less than 3 left 
#add the different 3s to a list
