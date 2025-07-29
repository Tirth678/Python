# when working with large amount of data, with same data type to increase effeciency and perfomance
# we use arrays 
# on python.org there are many more types of arrays avaliable here we have choosen i which stands for integer
# it has all properties as list, but every value will be of same type
from array import array
newarray = array("i", [2,3,4,5])
print(newarray)
newarray.append(17)
print(newarray)