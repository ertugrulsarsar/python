my_List = [1,2,3]
my_Tuple = 1,2,3    #değiştirilemez

print(type(my_List))
print(type(my_Tuple))

my_List[0] = 2
# my_Tuple[0] = 2

sonuc = my_Tuple[0]
sonuc = my_List[0]

my_List.append(1)
sonuc = my_Tuple.count(1)

my_Tuple2 = tuple([2,3,4])
my_List2 = list ([2,3,4])

print(type(my_Tuple2))
print(type(my_List2))

print(sonuc)




#TypeError: 'tuple' object does not support item assignment