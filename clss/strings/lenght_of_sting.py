#### find length of sringg
# strings = input("Enter a string: ")
# c = 0
# for i in strings:
#     # increment value if element found init
#     c += 1

#     print(i)

# print("length of sting is: ", c)

# #############################################################
# #############################################################

# rstring = input("Enter a string: ")
# r = ""
# for i in rstring:
#     r = r + i

# print("Reversed string is: ", r)

# #############################################################
# #############################################################

a = "code hello"
r = ""

for i in a:
    print(f"value of i: {i}, {i} != 'l': {i != 'l'}, value of r: {r}")
    if i != "l":
        r = r + i
    print(f"update value of r: {r}")
print(r)
