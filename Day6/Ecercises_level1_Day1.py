#Create an empty tuple
empty_tuple1=tuple()
empty_tuple2=()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters=('Firdausi','Jamila','Khadija')
brothers=('Muhammad','Jafar','Khalid')

#Join brothers and sisters tuples and assign it to siblings
siblings=sisters+brothers
print(siblings)

#How many siblings do you have?
print(len(siblings))

#Modify the siblings tuple
#and add the name of your father and mother and assign it to family_members
family_members=list(siblings)
family_members.append("Abubakar")
family_members.append("Aisha")
family_members=tuple(family_members)
print(family_members)