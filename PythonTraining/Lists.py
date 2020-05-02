friends = ["kevin", "karen", "jim"] # can make the variables number, boolean  like ["kevin", 20, True]
             # 0       1        2
            # -3      -2       -1

print(friends[0])
print(friends[-1])  # to access items from the back
print(friends[1:])  # print all starting from 1
friends = ["kevin", "karen", "jim", "oscar", "tom"]
print(friends[1:3])  # from index 1 to 3

friends[1] = "Mike"  # updated easily
print(friends[1])
#Functions on list
lucky_number = [4, 8, 15, 16, 23, 42]
friends = ["kevin", "karen", "jim", "jim", "oscar", "tom"]
friends.extend(lucky_number)
print(friends)
friends.append("Creed")
print(friends)
friends.insert(1, "Kelly")
print(friends)
friends.remove("jim")
print(friends)
#friends.clear() clear all items
friends.pop() #last element deleted
print(friends.index("Kelly"))
friends = ["kevin", "karen", "jim", "jim", "oscar", "tom"]
friends.sort()
print(friends)
print(friends.count("jim"))
print(friends.reverse())
friends2 = friends.copy()
print(friends2)
