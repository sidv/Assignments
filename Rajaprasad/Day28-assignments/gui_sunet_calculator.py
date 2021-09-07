#!/usr/bin/env python3
import ipaddress
import sys
import tkinter as t

root = t.Tk()
root.geometry('600x400')
root.title('Gui subnet calculator')

# defining function


def Display():
    # print(ip.get())
    # print(subnet_mask.get())
    # Ip = f'IP address : {ip.get()}'
    # subnet = f'subnet :{ip.get()}/{subnet_mask.get()}'

    ipi = ipaddress.ip_interface(f'{ip.get()}/{subnet_mask.get()}')
    # print("Address", ipi.ip)
    IP_addr = f' Ip Address : {ipi.ip}'
    # print("Mask", ipi.netmask)
    mask_addr = f'Mask : {ipi.netmask}'
    # print("Cidr", str(ipi.network).split('/')[1])
    Cidr = f'Cidr : {str(ipi.network).split("/")[1]}'
    # print("Network", str(ipi.network).split('/')[0])
    n_w_addr = f'Network Address : {str(ipi.network).split("/")[0]}'
    # print("Broadcast", ipi.network.broadcast_address)
    b_address = f'Broad cast Address : {ipi.network.broadcast_address}'

    lst.insert(t.END, IP_addr, mask_addr, Cidr, n_w_addr, b_address)


# if __name__ == "__main__":

    ipi = ipaddress.ip_interface(f'{ip.get()}/{subnet_mask.get()}')
    print("Address", ipi.ip)
    print("Mask", ipi.netmask)
    print("Cidr", str(ipi.network).split('/')[1])
    print("Network", str(ipi.network).split('/')[0])
    print("Broadcast", ipi.network.broadcast_address)

    # creating frame
lframe = t.Frame(root)
lframe.place(x=10, y=100)
rframe = t.Frame(root)
rframe.place(x=400, y=100)

# creating variable
ip = t.StringVar(lframe)
subnet_mask = t.StringVar(lframe)

# creating labels
t.Label(root, text='GUI subnet calculator ',
        font='consolas 14 bold', padx=20, pady=20).grid(row=0, column=1)

t.Label(lframe, text='Enter Ip address : ').grid(row=1, column=0)
t.Entry(lframe, textvariable=ip).grid(row=1, column=1)

t.Label(lframe, text='Enter subnet mask(0-32) : ').grid(row=2, column=0)
t.Entry(lframe, textvariable=subnet_mask).grid(row=2, column=1)

t.Button(lframe, text='Submit', command=Display).grid(row=3, column=0)

lst = t.Listbox(rframe, bg='grey', fg='white', justify='left')
lst.grid(row=1, column=3)


root.mainloop()
