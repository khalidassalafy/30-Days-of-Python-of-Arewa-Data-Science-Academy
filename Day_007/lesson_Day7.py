#removing items from a set
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)
fruits.discard("apple")
fruits.discard("lemon")
poped_item=fruits.pop()
print(fruits)
print(poped_item)

#clearing a set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
