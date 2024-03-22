
tup_nums = ()
num = float(input())
while num >= 0:
    tup_nums = tup_nums + (num,)
    num = float(input())

num_list = list(tup_nums)

reversed_values = ""

for i in range(len(num_list)-1, -1, -1):

    reversed_values += str(num_list[i])
 
    if i != 0:
        reversed_values += ", "

print(reversed_values)