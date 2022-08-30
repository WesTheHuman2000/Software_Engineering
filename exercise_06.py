
row = int(input('Enter a row: '))
row_store = row
column = int(input('Enter a column: '))
table_row =0
table_column =0

for x in range(5):
    table_row+=1
    for y in range(5):
        if table_row == row and y+1 == column:
            if x+1 != row:
                print(0, end=' ')
            else:
                print(1, end=' ')
        else:
            print(0, end=' ')
    print('')    
   # print('This is the current row:', table_row)
    
        
    
#    for y in range(5):
#        print('hi')
# create columns next, rows working right now?
