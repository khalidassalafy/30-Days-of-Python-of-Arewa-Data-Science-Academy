#Excercise 1
score=int(input('Enter the student\'s score: '))

if score<=100:
    if score>=80:
        print('A')
    elif score>=70:
        print('B')
    elif score>=60:
        print('C')
    elif score>=50:
        print('D')
    else:
        print('F')
else:
    print('No score morethan 100')

##Excercise 2
Autumn=['September', 'October', 'November']
Winter=['December', 'January', 'February']
Spring=['March', 'April', 'May']
Summer=['June', 'July', 'August']

month=(input('Enter the month: ')).capitalize()
if month in Autumn:
    print(' Hi! It is Autumn')
elif month in Winter:
    print(' Hi! It is Winter')
elif month in Spring:
    print(' Hi! It is Spring')
elif month in Summer:
      print(' Hi! It is Summer')
else:
    print('Invalid month')


##Excercise 3
fruits = ['banana', 'orange', 'mango', 'lemon']
add_fruit=input('Add a fruit you like into the list of fruits: ').lower()
if add_fruit in fruits:
    print('The fruit already exists in the list')
else:
    fruits.append(add_fruit) 
    print(fruits)