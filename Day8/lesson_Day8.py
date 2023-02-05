person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person.get('address'))
print(person.get('city'))
#print(person['city'])       # Error

#Changing dictionary to list of items
print(person.items())

#copying a dictionary to avoid mutation
person_copy=person.copy()
#person_copy[first_name]='Auwal'
print(person_copy)

keys=person.keys()
values=person.values()
print(keys)
print(values)