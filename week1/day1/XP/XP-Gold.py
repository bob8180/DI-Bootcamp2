print('Hello World' * 5)
print('I love python' * 5)

#2
month = int(input('Please, enter a month'))
if month < 1 or month >12:
    print('Enter a correct month!')
else:
    if month >=3 and month <=5:
        print('It is a spring')    
    elif month >=6 and month <=8:
        print('It is a summer')  
    elif month >=9 and month <=11:
        print('It is an autumn')    
    elif month ==12 or month <=2:
        print('It is a winter')    