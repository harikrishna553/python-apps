evenNumbers={2, 4, 6, 8, 8, 4, 10}
oddNumbers={1, 3, 5, 7, 9}
powersOf2={1, 2, 4, 8, 16}

unionOfSets = evenNumbers|oddNumbers
intersectionOfSets = evenNumbers&powersOf2
differenceBetweenSets = evenNumbers-powersOf2
copyOfSet = evenNumbers.copy()

print("unionOfSets : ", unionOfSets)
print("intersectionOfSets : ", intersectionOfSets)
print("differenceBetweenSets : ", differenceBetweenSets)
print("copyOfSet : ", copyOfSet)