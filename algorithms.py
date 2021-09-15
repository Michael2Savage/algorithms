# Excersize 1
# Reverse the list below in-place using an in-place algorithm.
# For extra credit: Reverse the strings at the same time.
print("Excersize 1")

words = ['this' , 'is', 'a', 'sentence', '.']

def swapper(a_list, index_a, index_b):
    a_list[index_a], a_list[index_b] = a_list[index_b], a_list[index_a]

swapper(words, 0, 4)
swapper(words, 1, 3)

def revtext(a_list):
    for word in a_list: 
        newtxt = word[::-1]
        print(newtxt)

print(f'{revtext(words)} \n')

# Excersize 2
# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
# 'array': 2, ... etc...

# create a function that creates a list and splits the string into a list of words.
# Conditionally add unique word to key value of list with value equal to 1
# Add 1 to that value when word already in dict

print('Excersize 2')

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'


def distinct(a_string):
    my_dict = {}
    wordslist = a_string.split()
    for word in wordslist:
        if word not in my_dict:
            my_dict[word] = 1
        elif word in wordslist:
            my_dict[word] += 1
    return my_dict


print(f'{distinct(a_text)} \n')


# Excersize 3
# Write a program to implement a Linear Search Algorithm. Also in a comment, 
# write the Time Complexity of the following algorithm.
# Hint: Linear Searching will require searching a list for a given number.
# If number is not present return -1

print("Excersize 3")

nums_list = [10,23,45,70,11,15]
target = 70

def lin_search(numlist, num):
    in_list = False
    while in_list == False:
        ticker = 0
        for i in range(len(numlist)):
            if numlist[i] != num:
                ticker += 1
            elif numlist[i] == num:
                in_list = True
        return in_list



print(lin_search(nums_list, 70))

# The time complexity of this algorithm is O(n)
