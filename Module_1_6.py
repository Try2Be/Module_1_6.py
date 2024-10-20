my_dict = { 'Ulyana': 2004, 'Sergey': 1998, 'Uyra': 1987}
print (my_dict)
print (my_dict.get('Ulyana'), my_dict.get('Lexa'))
my_dict.update({'Vasiliy': 1995, 'Alex': 1996})
a = my_dict.pop ('Vasiliy')
print (a)
print (my_dict)
my_set = { 1, 2, 3, 1, 5, 2.5}
print(my_set)
print (my_set.add(7),my_set.add(8))
my_set.remove(3)
print (my_set)