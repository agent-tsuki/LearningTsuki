# first method
strings = "rusrus"
a, b = "", ""
# for i, j in enumerate(strings):
#     if len(strings) / 2 <= i:
#         b += j
#     else:
#         a += j

# if a == b:
#     print("symmertric")
# else:
#     print("None none")

i = len(strings) // 2 # 3.0 -> 3
if strings[:i] == strings[i:]:
    print("semmtry")
else:
    print("None")
