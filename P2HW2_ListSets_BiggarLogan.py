num_1 = float(input('Enter num 1: '))
num_2 = float(input('Enter num 2: '))
num_3 = float(input('Enter num 3: '))
num_4 = float(input('Enter num 4: '))
num_5 = float(input('Enter num 5: '))
num_6 = float(input('Enter num 6: '))
print('Created list')
my_list = [ num_1, num_2, num_3, num_4, num_5, num_6 ]
print(my_list)
print('Smallest number in list:', min(my_list))
print('Largest number in list:', max(my_list))
print('Sum of numbers in list:', sum(my_list))
avg_list = sum(my_list) / len(my_list)
print('Average of numbers in list:', format(avg_list, ",.2f"))
print('Created set')
my_list = [ num_1, num_2, num_3, num_4, num_5, num_6 ]
my_final_list = set(my_list)
print(list(my_final_list))
