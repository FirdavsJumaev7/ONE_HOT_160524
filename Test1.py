import random
list_1 = list()
for i in range (0, 5):
     number = random.randint(1, 5)
     list_1.append(number)
print(list_1)
min_num = min(list_1)
max_num = max(list_1)
for j in range(len(list_1)):
     if list_1[j] == max_num:
         list_1[j] = min_num
print(list_1)
