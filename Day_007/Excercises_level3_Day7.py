age = [22, 19, 24, 25, 26, 24, 25, 24]

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set=set(age)
print('Is the list age greater than the set age_set? : ',len(age)>len(age_set))

#Explain the difference between the following data types: string, list, tuple and set:
# A string is a data type that consists of one or more characters.
# A list is an ordered collection of different data types which is modifiable and allows duplicates.
# A tuple is an ordered collection of different data types which is not modifiable and allows duplicates.
# A set is an unordered and un-indexed collection items that does not allows duplicates.

#I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence?
#  Use the split methods and set to get the unique words.
sentence=['I','am','a','teacher','and','I','love','to','inspire','and', 'teach','people']
sentence_set=set(sentence)
print('The unique words used in the sentence {}. are:  {}\nAnd their number is: {}'.format(sentence,sentence_set,len(sentence_set)))

print("ALHAMDULILLAH. done with day 7 !!")