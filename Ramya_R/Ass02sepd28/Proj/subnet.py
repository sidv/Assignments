import tkinter as tk

win = tk.Tk() #Creating window
win.title("Subnet Calculator") #Setting up the title
win.geometry("800x600")


#Creating Object
ip = tk.StringVar(win)
subnet = tk.IntVar(win)
ntad = tk.StringVar(win)
bdad = tk.StringVar(win)
avip = tk.StringVar(win)
ip_range = tk.StringVar(win)

# clear text
def clear():
	ip.set('')
	subnet.set(0)
	ntad.set('')
	bdad.set('')
	avip.set('')
	ip_range.set('')
	
# display output
def calci():
	ipl = [int(x) for x in ip.get().split(".")]
	mask = subnet.get()
	ntadr = net_adress(ipl, mask)
	ntad.set(".".join([str(x) for x in ntadr]))
	bdcst = broadcast(ntadr,mask)
	bdad.set(".".join([str(x) for x in bdcst]))
	ip_range.set(subrange(ntadr,bdcst))
	subnets,hosts = available(mask,ipl)
	avip.set(hosts)


#ip : 192.0.2.3/12
#11000000.00000000.00000010.00000011
#/21 -mask
#11111111.11110000.00000000.00000000
#Network Address
#11000000.00000000.00000000.00000000
#broadcast address
#11000000.00001111.11111111.11111111

	
# functions for calculation	
def net_adress(ipl,mask):
    maskb = str("1"*mask+"0"*(32-mask)) 
    mlst = [int(maskb[i:i+8],2) for i in range(0,len(maskb),8)]
    return [ipl[i]&mlst[i] for i in range(4)]
#subnetmask = 32
#lst = []
#nead = []
#netw = []
#	for i in range(0,mask): # appending mask value 1
#		lst.append("1")
#	sp = "".join(lst)
#	for  i in range(0,subnetmask): # appending value 0
#		if len(lst) < subnetmask:
#			lst.append("0")
#	maskb ="".join(lst)
#	for i in range(0,len(maskb),8):
#		nead.append(int(maskb[i:i+8],2))
#	#print(nead,"subnetmask")
#	for j in range(4):
#		netw.append(ip[j] & nead[j])
#	return netw


def available_host(ip,sub):
	subnet = 32
	mask = 32 - sub
	no_of_avail_ip_addr= pow(2, mask)
	host_ip_address = no_of_avail_ip_addr - 2
	return no_of_avail_ip_addr,host_ip_address


def broadcast(ntadr,mask):
    maskb = str("0"*mask+"1"*(32-mask))
    inv = [int(maskb[i:i+8],2) for i in range(0,len(maskb),8)]
    return [ntadr[i]|inv[i] for i in range(4)]

def broad_addr(ipl,mask):
	subnet = 32
	lst = []
	bro = []
	broad = []
	for i in range(0,mask): # appending mask value 0
		lst.append("0")
	sp = "".join(lst)
	for  i in range(0,subnet): # appending value 1
		if len(lst) < subnet:
			lst.append("1")
	sp1 ="".join(lst)
	print(ip,"ip")
	for i in range(0,len(sp1),8):
                bro.append(int(sp1[i:i+8],2))
	print(bro,"subnet")
	for j in range(4):
		broad.append(ip[j] | bro[j])
	return broad

def available(mask,ipl):
    if ipl[0] > 0 and ipl[0] < 128:
        sb = mask - 8
        hb = 32 - mask
        snets = 2**sb
        hosts = 2**hb - 2
    elif ipl[0] > 127 and ipl[0] < 192:
        sb = mask - 16
        hb = 32 - mask
        snets = 2**sb
        hosts = 2**hb - 2
    elif ipl[0] > 191 and ipl[0] < 224:
        sb = mask - 24
        hb = 32 - mask
        snets = 2**sb
        hosts = 2**hb - 2
    else:
        print(" class d or e ")
    return snets,hosts

def subrange(ntadr,bdcst):
    ntadr[-1] = ntadr[-1]+1
    bdcst[-1] = bdcst[-1]-1
    ntadr = [str(x) for x in ntadr]
    bdcst = [str(x) for x in bdcst]
    return ".".join(ntadr)+" - "+".".join(bdcst)
    
# creating labels
    
tk.Label(win,text = "IP Address").grid(row=0,column=0)
tk.Entry(win,textvariable=ip).grid(row=0,column=1)

tk.Label(win, text="Subnet Mask (0-32)").grid(row=1, column=0)
tk.Entry(win, textvariable=subnet).grid(row=1, column=1)


tk.Button(win,text="Submit",command = calci).grid(row=2,column=1)


tk.Label(win,text = "Network Address").grid(row=4,column=0)
tk.Entry(win,textvariable=ntad).grid(row=4,column=1)

tk.Label(win, text="Broadcast Address").grid(row=5, column=0)
tk.Entry(win, textvariable=bdad).grid(row=5, column=1)

tk.Label(win,text = "available IP Address").grid(row=6,column=0)
tk.Entry(win,textvariable=avip).grid(row=6,column=1)

tk.Label(win,text = "IP Range").grid(row=7,column=0)
tk.Entry(win,textvariable=ip_range).grid(row=7,column=1)

tk.Button(win,text="Clear",command = clear).grid(row=8,column=1)

win.mainloop()
