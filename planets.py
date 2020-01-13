# Use append() to add Jupiter and Saturn at the end of the list.
# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
# Use insert() to add Earth, and Venus in the correct order.
# Use append() again to add Pluto to the end of the list.
# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.

planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
# print(planet_list)
planet_list.append("Saturn")
# print(planet_list)

planet_list.extend(["Uranus", "Neptune"] )
# print(planet_list)

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
# print(planet_list)

planet_list.append("Pluto")
print(planet_list)

# Slice list by choosing index range to extricate. First number is the first item needed, second number is one number greater than last item needed.
rocky_planets = planet_list[0:4]
print("Rocky Planets:", rocky_planets)

# del is a keyword, use it followed by the list name and put the index number of the item you want to delete in the square brackets.
del planet_list[8]
print(planet_list)

