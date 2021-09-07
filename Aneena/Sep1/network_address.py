#1.Calculate the network address,subnet mask(octet format),Number of  available address,broad cast address,range for following


#a)ip : 192.168.1.4/21
IP:		11000000.10101000.00000001.00000100
Subnet mask:	11111111.11111111.11111000.00000000
		------------------------------------
Network Addr:	11000000.10101000.00000000.00000000 = 192.168.0.0
Broadcast Addr:	11000000.10101000.00000111.11111111 = 192.168.7.255

Subnet mask:	255.255.248.0

11111 000.00000000

	11111 000
	00000 000 = 0
	00000 111 = 7 =8

	00000000 = 0    
	11111111 = 255 = 256

	8*256 = 2048
	2048 -2(1 for network and another 1 for broadcast)=2046	(available ips)
	2048 -8 -8 = 2032 
	IP address range 
	192.168.0.1 - 192.168.0.254
	192.168.7.1 - 192.168.7.254


#b)ip : 10.1.4.5/16
IP:		00001010.00000001.00000100.00000101
Subnet mask:	11111111.11111111.00000000.00000000
		------------------------------------
Network Addr:	00001010.00000001.00000000.00000000 = 10.1.0.0
Broadcast Addr:	00001010.00000001.11111111.11111111 = 10.1.255.255

Subnet mask:	255.255.0.0
	00000000.00000000
	11111111 =256
	00000000
	11111111 = 256

Available hosts:	(2^16)-2 = 65536-2 = 65534
256 * 256 = 65536
	65536 -2 = 65534
	65534 -256 -256 = 65024
IP address range:	
10.1.0.1 - 10.1.255.254


#c)ip : 192.0.2.3/12

IP:		11000000.00000000.00000010.00000011
Subnet mask:	11111111.11110000.00000000.00000000
		------------------------------------
Network Addr:	11000000.00000000.00000000.00000000 = 192.0.0.0
Broadcast Addr:	11000000.00001111.11111111.11111111 = 192.15.255.255
Subnet mask:	255.240.0.0
Available hosts:	(2^20)-2 = 1048576-2 = 1048574
IP addr range:
	192.0.0.1- 192.15.255.254



#2.Calculate the network address,Number of  available address,broad cast address,range for following

#a)ip : 192.0.4.8 subnet mask: 255.255.255.252
IP:		11000000.00000000.00000100.00001000
Subnet mask:	11111111.11111111.11111111.11111100
		------------------------------------
Network Addr:	11000000.00000000.00000100.00001000 = 192.0.4.8
Broadcast Addr:	11000000.00000000.00000100.00001011 = 192.0.4.11

Available hosts:4-2 = 2   (2^2 -2)=2
IP addr range:192.0.4.9 - 192.0.4.10

#b)ip : 10.1.4.5 subnet mask: 255.255.254.0
IP:		00001010.00000001.00000100.00000101
Subnet mask:	11111111.11111111.11111110.00000000
		------------------------------------
Network Addr:	00001010.00000001.00000100.00000000 = 10.1.4.0
Broadcast Addr:	00001010.00000001.00000101.11111111 = 10.1.5.255

Available hosts:2^9-2 = 512 - 2 = 510
IP addr range:	10.1.4.1 - 10.1.5.254


#c)ip : 192.0.2.3 subnet mask: 255.255.224.0
IP:		11000000.00000000.00000010.00000011
Subnet mask:	11111111.11111111.11100000.00000000
		------------------------------------
Network Addr:	11000000.00000000.00000000.00000000 = 192.0.0.0
Broadcast Addr:	11000000.00000000.00011111.11111111 = 192.0.31.255

Available hosts:2^13-2 = 8192 - 2 = 8190
IP addr range:	192.0.0.1 - 192.0.31.254

#3.Calculate the subnet mask,network address
I want to create a subnet and with maximum 126 host
192.168.0.0

IP:		11000000.10101000.00000000.00000000
Subnet mask:	11111111.11111111.11111111.10000000 = 255.255.255.128
		------------------------------------
Network Addr:	11000000.10101000.00000000.00000000 = 192.168.0.0
Broadcast Addr:	11000000.10101000.00000000.01111111 = 192.168.0.127

Available hosts:2^7-2 = 128 - 2 = 126
IP addr range:	192.168.0.1 - 192.168.0.126

#4.Calculate the subnet mask,network address
I want to create a subnet and with maximum 237 host
192.168.0.0
In this case we can't get a subnet mask with a maximum of 237 hosts.Because n be the number of zeros in subnet mask,not a number.

#5.Calculate the subnet mask,network address
I want to create a subnet and with maximum 100000 host
192.168.0.0
In this case we can't get a subnet mask with a maximum of 100000 hosts.Because n be the number of zeros in subnet mask,not a number.

