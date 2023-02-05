# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
multiple_it_companies=['Linkedin', 'Instagram','Telegarm']
it_companies.update(multiple_it_companies)
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('Apple')
it_companies.discard('Microsoft')
it_companies.pop()
print(it_companies)

#What is the difference between remove and discard:
#remove returns an error if the specified item does not exist in the set
#while, discard does not return error if the item does not exist in the set

#
