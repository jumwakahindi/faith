#operations on sets
my_set={1,2,3,4,4,5,7,8,9,}
print("Original set:",my_set)
#add values to the set
my_set.add(6)
print("Updated set:",my_set)
#set operations
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
#set difference-values that are found in each set only
print("set difference:", set1.difference(set2))
print("symmetric  difference:", set1.symmetric_difference(set2))
#combine both sets
print("Union:",set1.union(set2))
#set intersection-print on both sets
print("Intersection:",set1.intersection(set2))