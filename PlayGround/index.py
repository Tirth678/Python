# # # #list
# # # # list is a mutable(changable), ordered collection of htergeneous(different) elements
# # # fruits = ["apple", "banana", "mango"]
# # # # it is indexed-based(0-indexed)
# # # # accesing elements through index
# # # print(fruits[1]) # positive indexing
# # # print(fruits[-1]) # negative indexing

# # # # operations possible on list
# # # a = [1,2,3]
# # # b = [6,7,9]
# # # # print(a+b) # concatination

# # # # repetition
# # # # print(a*5)

# # # # membership operator(in)
# # # if 69 in a:
# # #     print("true")
# # # else:
# # #     print("false")

# # # # slicing
# # # print(a[0:2])
# # # print(a.append(21)) # add element from last
# # # print(a.insert(1,20)) # insert at given index
# # # print(a.remove(2)) # remove first match
# # # print(a.pop(3)) # pop removes elemtent by default it will pop last element
# # # print(a.sort()) # sort in acsending order
# # # print(a.reverse()) # reverse the list
# # # print(a.extend(b)) # merge another list
# # # print(a.count(0)) # count of occurrences of any value example: 0 here

# # a = (1,2,3)
# # print(a)
# # print(a.count(2)) # returns count of any value in tuple
# # value = a.index(1) # will return index of given value(agar andar che baaki nai)
# # print(value)
# # # converting list into tuple
# # fruits = [1,2,3,"somemthiong"]
# # something = tuple(fruits)
# # print(something)

# student = {
# "id": 101,
# "name": "om",
# "marks": 90,
# }
# # accesing elements
# print(student["marks"])
# print(student.get("marks")) # using get method

# # operations
# student["age"] = 20 # adding a new key:value pair
# print(student)
# del student["marks"] # deleting a key:value pair
# print(student)
# student.clear() # this is used to empty whole dictionary
# print(student)


import array as arr
om = arr.array("i", [10,12,29,230,1])
