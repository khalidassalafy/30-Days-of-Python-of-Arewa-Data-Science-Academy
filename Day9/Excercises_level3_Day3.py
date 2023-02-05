person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript','React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

    #Check if the person dictionary has skills key, 
    #if so print out the middle skill in the skills list.
if 'skills' in person:
    skills_length=len(person['skills'])
    if skills_length%2==0:
        middle_element=person['skills'][int(((skills_length/2)-1)) : int(((skills_length/2))+1)] 
        print('The middle element(s) :',middle_element)
    else:
        middle_element2=person['skills'][skills_length//2] 
        print('The middle element(s) :',middle_element2)

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill
# and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print(person['skills'])
    else:
        print('Not proficient in python')

#If a person skills has only JavaScript and React, print('He is a front end developer'),
#if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
#if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
# else print('unknown title') - for more accurate results more conditions can be nested!
if 'JavaScript' in person['skills'] and 'React' in person['skills']:
       print('He is a front end developer')
elif 'Node' in person['skills'] and 'python' in person['skills'] and 'MangoDB' in person['skills']:
    print('He is a backend developer')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MangoDB' in person['skills']:
    print('He is a fullstack developer')
else:
    print('Unknown title!')

 #If the person is married and if he lives in Finland, 
 # print the information in the following format:
if person['is_married']==True and person['country']=='Finland':
    print('{} {} is married. He lives in {}'.format(person['first_name'],person['last_name'],person['country']))

print("Alhamdulillah! Done with day 9 challenge")
print("This challenge is cool")