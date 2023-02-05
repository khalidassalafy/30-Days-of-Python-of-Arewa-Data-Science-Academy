A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#Join A and B
A_and_B= A.union(B)
print('A joined with B is: ',A_and_B)

#Find A intersection B
print('The common elements in both A and B: ',A.intersection(B))

#Is A subset of B
print('Is A subset of B? : ', A.issubset(B))

#Are A and B disjoint sets
print('Are A and B disjoint sets? : ',A.isdisjoint(B))

#Join A with B and B with A
print(A.union(B))
print(B.union(A))

#What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#Delete the sets completely
del A
del B
