#P15 2.2.3
#2-1
message="hello word!".title()
print(message)


#p21 
#练习2-3

name_person = "eric"
message=f"Hello {name_person.title()},would you like to learn some Python today?"
print(message)

#练习2-4

name_person = "Eric"
message = f"Hello {name_person.lower()},would you like to learn some Python today?"
print(message)

name_person = "eric"
message = f"Hello {name_person.upper()},would you like to learn some Python today?"
print(message)

name_person = "eric"
message = f"Hello {name_person.title()},would you like to learn some Python today?"
print(message)

#练习2-6

name = "albert einstein"
saying = '"A person who never made a mistake never tried anything new."'
message = f"{name.title()} once said, {saying} "
print(message)

name = "albert einstein"
saying = "\"A person who never made a mistake never tried anything new.\""#\转义
message = f"{name.title()} once said, {saying} "
print(message)

#练习2-7

name = "   albert einstein        "
saying = "\"A person who never made a mistake never tried anything new.\""
message = f"{name.title()} once said, \n\t{saying} "
print(message)

name = "   albert einstein        "
saying = "\"A person who never made a mistake never tried anything new.\""
message = f"{name.title().lstrip()} once said, \n\t{saying} "
print(message)

name = "   albert einstein        "
saying = "\"A person who never made a mistake never tried anything new.\""
message = f"{name.title().rstrip()} once said, \n\t{saying} "
print(message)

name = "   albert einstein        "
saying = "\"A person who never made a mistake never tried anything new.\""
message = f"{name.title().strip()} once said, \n\t{saying} "
print(message)

#p24
#练习2-8

print(3+5)
print(2+6)
print(1+7)
print(4+4)

#练习2-9

figure = 9
message = f"My favorite number is {figure}."
print(message)

MAX = 5000
MAX = MAX + 1
print(MAX)

#p37
#sort()永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse = True)
print(cars)

#sorted()临时排序
cars = ['bmw', 'audi', 'toyota', 'sub']
print('Here is the original list:')
print(cars)

print('\nHere is the original list:')
print(sorted(cars))

print('\nHere is the original list:')
print(cars)

a = [432, 4, 6, 89, 23, 45]
b = sorted(a, reverse=True)
print(a)
print(b)

#P39 
#练习3-8

travel_place = ["Japan", "switzerland","paris", "taiwan"]
print(travel_place)

sorted_visited_palce = sorted(travel_place)
print(sorted_visited_palce)
print(travel_place)

sorted_visited_palce = sorted(travel_place,reverse=True)
print(sorted_visited_palce)
print(travel_place)

travel_place.reverse()
print(travel_place)
travel_place.reverse()
print(travel_place)

travel_place.sort()
print(travel_place)

travel_place.sort(reverse = True)
print(travel_place)

#练习3-9

print(len(travel_place))














