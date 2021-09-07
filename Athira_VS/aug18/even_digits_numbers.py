
even_set = {'0','2','4','6','8'}
num_lst = list(range(1000,3001))

'''
for a in range(1000,3001):
    if not {str(a)[0], str(a)[1], str(a)[2], str(a)[3]}.difference(even_set):
        print(a)
'''

# Filter out the numbers with even digits
res_lst = list(filter(lambda a: {str(a)[0], str(a)[1], str(a)[2], str(a)[3]}.difference(even_set) == set() ,num_lst))

# Print the res_list as a comma separated string
print(','.join(map(lambda a: str(a),res_lst)))
