#simple data structures project
#experimenting with lists & appending data.
print("List of names that are banned!")
names = ["Bob", "Ted","Mike","Jose","Alex"]
names2 = ["Bert","Ed","Eldritch Blast"]
print(names)

#simple appending
names.append("Doug")
print(names)

#appending data based on user input
names.append(input("What is your name? "))
print(names)

#extending the list
names.extend(["Anna","Angelica","Elizabeth"])
print(names)

#extending the list via another list
names.extend(names2)
print(names)