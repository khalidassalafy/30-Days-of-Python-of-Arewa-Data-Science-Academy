#Let's get the intercepts
x=float(input('Enter the intercept x: '))
slope1=2*x-2
print("the slope 1 is: ",slope1)

#another slope 
x1=2
x2=6
y1=2
y2=10
slope2=(y2-y1)/(x2-x1)
print("the slope 2 is: ",slope2)

#comparing the two slopes
print(slope1 is slope2)

#Euclidean distance
import math
euclidean_dist=math.sqrt((x1-y1)**2+(x2-y2)**2)
print('the euclidean distance is : ',euclidean_dist)
