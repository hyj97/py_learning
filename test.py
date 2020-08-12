# d = {'lilee': 25, 'wangyan': 21, 'liqun': 32, 'age': 19}
#
# print(d.items())
# print(type(d.items()))
# a=lambda item:item[1]
# print(a(d.items()))

d = {('education', 'age'): 'Stanford University'}
c = sorted(d.items(), key=lambda item: item[1])
a = {}
for i in c:
    a[i[0]] = i[1]
print(a)
