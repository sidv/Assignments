'''
5.Calculate the subnet mask,network address
I want to create a subnet and with maximum 100000 host
192.168.0.0
'''

'''
given ip address= 192.168.0.0 we need max 100000 hosts so
2^? = 100000 == most probably 17

2^17 = 131072  so 100000 host can be easily fit inside there

subnet mask address = 192.168.0.0/32-17 = 192.168.0.0/15

binary ip  : 11000000.1010100 0.00000000.00000000
mask ip    : 11111111.1111111 0.00000000.00000000

n/w ip  --> 11000000.1010100 0.00000000.00000000 -> 192.168.0.0
'''
