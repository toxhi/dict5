my_dict = {'one':1,2:'two','three':3,4:[2,4,6]}
print(my_dict['one'])
my_dict[2] = 'mera'
print(my_dict[2])
print(my_dict[4])

my_dict[4] = 'four'
print(my_dict)

my_dict[5]='five'
print(my_dict)
del my_dict[4]
print(my_dict)

dict_1 = {}
dict_2 = dict()

print(dict_1)
print(dict_2)

for item in my_dict:
  print(my_dict[item])