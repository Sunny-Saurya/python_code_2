l1 = [1,2,3,4,5,20]
l2 = [5,6,7,89,20,21,45]
l3 = [5,20, 34,45,56,784,12]

s1 = set(l1)
s2 = set(l2)
s3 = set(l3)


s1s2 = s1.intersection(s2)
final_set = s1s2.intersection(s3)
print(list(final_set))
