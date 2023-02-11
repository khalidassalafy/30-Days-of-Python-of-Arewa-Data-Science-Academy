#Level1
#Excercise 1
age=int(input('Enter your age: '))
if age<=0:
    print('Invalid age!')
elif age>=18:
    print('Your are old enough to drive')
else:
    print('You need {} more years to learn to drive'.format(18-age))

#Excercise 2
my_age=20
your_age=int(input('Enter your age: '))

if your_age>0:
   if your_age>my_age:
    diff=your_age-my_age
    if diff==1:
        print('You are one year older than me')
    else:
        print('You are {} years older than me'.format(diff))

   elif your_age==my_age:
    print('We are age mates')
   else:
    diff2=my_age-your_age
    if diff2==1:
        print('I am one year older than you')
    else:
        print('I am {} years older than you'.format(diff2))

else:
    print('Invalid age')


#Excercise 3
a=int(input('Enter number one:'))
b=int(input('Enter number two:'))

if a>b:
    print('{} is greater than {}'.format(a,b))
elif a<b:
      print('{} is smaller than {}'.format(a,b))
else:
       print('{} is eqauals to {}'.format(a,b))
