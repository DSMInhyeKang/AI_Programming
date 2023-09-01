# a = 123
# print(a)
# print(type(a))

# a = 10
# b = 4

# print(a/b)
# print(a//b)

# print("""Hello world!
#       abc
#         def
#             ddd cc""")


# print(len('Python is strong'))


a = "python is strong, you need python"

print(a[0:7])
print(a[-1])
print(a[-6])
print(a[:16])
print(a[18:])
print(a[:])

print(a[10:-17])
print(a[18:-7])


print("I have %d pens" % 3)
print("I have %d apples and %d bananas" % (4, 6))


b=3
print(f'I have {b} apples')
print("I have {0} apples and {1} bananas".format(5, 4))

print(a.count("o"))
print(a.find("is"))


print(a.split())
odd = [1, 3, 5, 7, 9]
print(type(odd))

l = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(l[3][:2])

print([1,2,3]*3)

l.extend([5, 6])
l.append([5, 6])
print(l)