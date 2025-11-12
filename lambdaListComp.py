import math

#===> lambda

add = lambda nb1=0, nb2=0, nb3=0: nb1 + nb2 + nb3
getPowFunc = lambda nb: (lambda power: nb**power) # a vérifier

#===> list comprehension

list1 = [4, 5, 8]
list2 = [10, 28, 32]

#=> 1
mergedLists = [(i, j) for i, j in zip(list1, list2)]

#=> 2
allPossibilities = [(i, j) for i in list1 for j in list2] + [(j, i) for i in list1 for j in list2]

#=> 3
primeNumbers = [n for n in range(2, 41) if all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))]

if __name__ == "__main__":

    #===> lambda tests

    print(add(1, 2))
    print(add(1, 2, 3))

    print(getPowFunc(5)(2))
    print(getPowFunc(2)(4))

    #===> list comprehension tests
    print(mergedLists)
    print(allPossibilities)
    print(primeNumbers)