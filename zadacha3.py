import random
number = int(random.randrange(100000,1000000))
print(number)
firsttree = number%1000
print(firsttree)
lasttree = int(number/1000)
print(lasttree)
first1 = firsttree%10
print (first1)
second1 = (firsttree//10)%10
print (second1)
third1 = int(firsttree/100)
print (third1)
first2 = lasttree%10
print (first2)
second2 = (lasttree//10)%10
print (second2)
third2 = int(lasttree/100)
print (third2)
if first1+second1+third1 == first2+second2+third2:
    print('You are lucky')
else:
    print('Good luck next time')
