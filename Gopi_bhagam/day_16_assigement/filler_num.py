"""
def square_num(num):
        return num%2==0
my_list =list(range(10,50))
update=filter(square_num,my_list)
print(list(update))
"""
even_filter = list(range(10,50))
res = list(filter(lambda x: x%2 == 0 , even_filter))
print(res)
