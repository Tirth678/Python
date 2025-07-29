str = "Hello world"
print(str) # will print your string
print(str.upper()) # will return new string as HELLO WORLD
print(str.lower()) # will return new string hello world
print(str.title()) # will return new string Hello World
print(str.replace("w", "a")) # replaces world with aorld
print(str.count("o")) # counts number of "o" present in string
print(str.strip()) # removes white spaces from left to right
print("Hello" in str) # returns True or False depending it is present in string or not
print("World" not in str) # returns True or False depending it is present or not
# we also have "slicing" techniques in python
print(str[0:4]) # this will start from indexing 0 to indexing 2 not 3 => Hell
print(str[1:]) # if this is blank complete string will be printed
print(str[:4]) # this will start from indexing 0 as default and will print till index 3
print(str[2:-1]) # negative indexing will start from last word "d" => "llo worl"
print(str[-1:]) # this will return last word only that's d
