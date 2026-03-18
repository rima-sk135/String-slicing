# using str.format method
name = "Rima"
year = 2003
print("Name: {}, born in: {}".format(name, year))

# string_slicing var=string variable, so,strinng slicing = var[start(inclusive):stop(exclusive):step(in case of skipping)]

name = "Rima Das"

first_name = name[:4]
last_name = name[5:]
funky_name = name[1::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# slicing var = variable, slice = slice(start, stop), so, print(var[slice])
website1 = "https://google.com"
website2 = "https://animixplay.com"

slice= slice(8, -4)

print(website1[slice])
print(website2[slice])

