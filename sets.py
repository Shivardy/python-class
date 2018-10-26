s1 = set ('spam')
s2 = {'h','a','m'}
s3 = set()
print type(s2)
print s1 & s2 # intersection
print s1 | s2 # union
print s1 - s2 
print s1 > s2 # is s2 subset of s1
print {n**2 for n in [1,2,3,4]}

print list (set([1,2,1,3,1,4])) # set is used to remove duplicates
print set('spam') - set('ham')
print set('spam') == set('asmp')
s1.add('alot')
s1.remove('alot')

print {1,2,3,4}.union([3,4])
print {1,3,4,5}.union({3,4})
print {1,2,4,5}.union((3,4))
print {1,2,3,5}.intersection([3,4])
print {1,2,3,4}.issubset(range(-5,5))
s={1.44}
s.add((1,2,3))