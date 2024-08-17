
''' str.strip: Remove leading and trailing whitespace.'''

s = "  hello  "
stripped = s.strip()
print(f"stripped :{stripped}")

s = "  hello brother      "
stripped2 = s.strip()
print(f"stripped2 :{stripped2}")




'''str.split: Split a string into a list.'''

s1 = "a,b,c"
parts = s1.split(',')
print(f"parts :{parts}")

s2 ="alphabet pure game name"
parts2 = s2.split(' ')
print(f"parts:{parts2}")



'''str.startswith and str.endswith: Check if a string starts or ends with a substring.'''

s = "hello world"
starts_with_hello = s.startswith('hello')
ends_with_world = s.endswith('world')

print(starts_with_hello,ends_with_world)


'''format : Format a string using placeholder'''
name = "John"
age = 30
formatted = "Name: {}, Age: {}".format(name, age)
formatted = f"Name: {name}, Age: {age}"