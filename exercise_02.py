user_entry = input("Enter a string: ")
user_entry2= input("Enter another string: ")

if user_entry.endswith(user_entry2):
    print("True")
elif user_entry2.endswith(user_entry):
    print("True")
else:
    print("False")