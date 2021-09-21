#Project:
#1.Create GUI subnet calculator.
#	-Take IP address input
#	-Take subnet mask as input
#	-Display IP adresss,subnet mask,Network address,Broadcast address,No.of available IP address,Range


#!/usr/bin/env python3
import ipaddress
import sys
import tkinter as tk

win = tk.Tk() #Creating window
win.title("Subnet Calculator") #Setting up the title
win.geometry("1000x1000")



#display output function
def Display():
	val= ipaddress.ip_interface(f'{ip.get()}/{subnet_mask.get()}')
	IP_address = f'Ip Address : {val.ip}'
	mask_address = f'Mask Address : {val.netmask}'
	mask = f'Mask : {str(val.network).split("/")[1]}'
	network_address = f'Network Address : {str(val.network).split("/")[0]}'
	b_address = f'Broad cast Address : {val.network.broadcast_address}'
	
	avail = 32-int(str(val.network).split("/")[1])
	no = pow(2, avail)
	available = f'Available ip Address : {no - 2}'
	
	n = f'{str(val.network).split("/")[0]}'
	n = list(n.split("."))
	n[3] = int(n[3]) + 1
	start_range = ".".join(map(str, n))
	b = f'{val.network.broadcast_address}'
	b = list(b.split("."))
	b[3] = int(b[3]) - 1
	end_range = ".".join(map(str, b))
	
	ip_range = f'ip range: {start_range + "-"+ end_range}'

	lst.insert(tk.END, IP_address, mask_address, mask, network_address, b_address, available, ip_range )
 
 #for printing in terminal   
	val = ipaddress.ip_interface(f'{ip.get()}/{subnet_mask.get()}')
	print("ip Address : ", val.ip)
	print("Mask Address : ", val.netmask)
	print("mask : ", str(val.network).split('/')[1])
	print("Network : ", str(val.network).split('/')[0])
	print("Broadcast : ", val.network.broadcast_address)
	print("Available ip : ", no-2)
	print("Ip range", start_range + "-"+ end_range)

#frames
left_fr = tk.Frame(win)
left_fr.grid(row=0,column=0)
left_fr.place(x=10, y=150)
right_fr = tk.Frame(win)
right_fr.grid(row=0,column=2)
right_fr.place(x=400, y=150)

#Creating Object
ip = tk.StringVar(left_fr)
subnet_mask = tk.IntVar(left_fr)

# creating labels

tk.Label(left_fr, text='Enter IP address(Ex:10.1.4.5) : ').grid(row=1, column=0)
tk.Entry(left_fr, textvariable=ip).grid(row=1, column=1)

tk.Label(left_fr, text='Enter subnet mask(0-32) : ').grid(row=2, column=0)
tk.Entry(left_fr, textvariable=subnet_mask).grid(row=2, column=1)

tk.Button(left_fr, text='Submit', command=Display).grid(row=4, column=0)

lst = tk.Listbox(right_fr)
lst.grid(row=1, column=2)


win.mainloop()

#a = input(str("Enter ip address: "))
#print(a)
#b = ipaddress.IPv4Network(a)
#print(str(b.netmask))

