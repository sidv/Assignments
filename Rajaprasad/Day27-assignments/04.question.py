'''
4.Calculate the subnet mask,network address
I want to create a subnet and with maximum 237 host
192.168.0.0
'''

'''
given ip address : 192.168.0.0 so we want 237 host meand 2^? = 237 = most probably 8

2^8 = 256  so 237 host will be inside fit there.

subnet mask address = 192.168.0.0/32-8 = 192.168.0.0/24

binary ip  : 11000000.10101000.00000000. 00000000
bin mask ip: 11111111.11111111.11111111. 00000000

n/w address =  11000000.10101000.00000000. 00000000  --> 192.168.0.0
'''
