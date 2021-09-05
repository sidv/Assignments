''' 
2.Calculate the network address,Number of  available address,broad cast address,range for following
ip : 192.0.4.8 subnet mask: 255.255.255.252
ip : 10.1.4.5 subnet mask: 255.255.254.0
ip : 192.0.2.3 subnet mask: 255.255.224.0
'''
#i 
'''
given ip adress : 192.0.4.8
mask IP address : 255.255.255.252

binary format = 11000000.00000000.00000100. 00001000
mask binary   = 11111111.11111111.11111111. 11111100

n/w address = 11000000.00000000.00000100.00000000 --> 192.0.4.0
b/c address = 11000000.00000000.00000100.11111111 --> 192.0.4.255

range = 192.0.4.8/24 means 2^32-24 = 2^8 --> 256
'''

#ii

'''
given ip address = 10.1.4.5
given mask addres = 255.255.254.0

binary ip address = 00001010.00000001. 00000100.00000101
binary mask adres = 11111111.11111111. 11111110.00000000

n/w address = 00001010.00000001.00000000.00000000 --> 10.1.0.0
b/c address = 00001010.00000001.11111111.11111111 --> 10.1.255.255


range = 10.1.4.5/16  means 2^32-16 = 2^16 = 65536
'''

# iii 
'''
given ip : 192.0.2.3
given mask : 255.255.224.0

binary ip : 11000000.00000000. 00000010.00000011
bunary mask:11111111.11111111. 11100000.00000000

n/w addr = 11000000.00000000.00000000.00000000 --> 192.0.0.0
b/c addr = 11000000.00000000.11111111.11111111 --> 192.0.255.255

range = 192.0.2.3/16 means 2^32-16 = 2^16 = 65536 no's addresses
'''