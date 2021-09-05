'''
3.Calculate the subnet mask,network address
I want to create a subnet and with maximum 126 host
192.168.0.0
'''

'''
given ip address = 192.168.0.0 we want 126 host means 2^? = 126 --> most posibly 7
2^7 = 128 means 126 host will be present inside there 

so subnet mask address  = 192.168.0.0/32-7 --> 192.168.0.0/25

binary ip : 11000000.10101000.00000000.0 0000000
mask ip   : 11111111.11111111.11111111.1 0000000
n/w adress = 11000000.10101000.00000000.0000000 --> 192.168.0.0
'''
