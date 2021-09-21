import tkinter as tk


root = tk.Tk()
root.title(" GUI Subnet calculator")
root.geometry("600x400")
root.config(bg='#00FA9A')

ip = tk.StringVar(root)
sbnt = tk.IntVar(root)
ntad = tk.StringVar(root)
bdad = tk.StringVar(root)
avip = tk.StringVar(root)
rng = tk.StringVar(root)


def clean():
    ip.set('')
    sbnt.set('')
    ntad.set('')
    bdad.set('')
    avip.set('')
    rng.set('')


def net_adress(ipl, mask):
    maskb = str("1"*mask+"0"*(32-mask))
    mlst = [int(maskb[i:i+8], 2) for i in range(0, len(maskb), 8)]
    return [ipl[i] & mlst[i] for i in range(4)]


def broadcast(ntadr, mask):
    maskb = str("0"*mask+"1"*(32-mask))
    inv = [int(maskb[i:i+8], 2) for i in range(0, len(maskb), 8)]
    return [ntadr[i] | inv[i] for i in range(4)]


def available(mask, ipl):
    if 0 < ipl[0] < 128:
        subnetbit = mask - 8
        hostbit = 32 - mask
        snets = 2**subnetbit
        hosts = 2**hostbit - 2
    elif 128 < ipl[0] < 192:
        subnetbit = mask - 16
        hostbit = 32 - mask
        snets = 2**subnetbit
        hosts = 2**hostbit - 2
    elif 191 < ipl[0] < 224:
        subnetbit = mask - 24
        hostbit = 32 - mask
        snets = 2**subnetbit
        hosts = 2**hostbit - 2
    else:
        print(" class d or e ")
    return snets, hosts


def subrange(ntadr, bdcst):
    ntadr[-1] = ntadr[-1]+1
    bdcst[-1] = bdcst[-1]-1
    ntadr = [str(x) for x in ntadr]
    bdcst = [str(x) for x in bdcst]
    return ".".join(ntadr)+"-"+".".join(bdcst)


def calculate():
    ipl = [int(x) for x in ip.get().split(".")]
    mask = sbnt.get()
    ntadr = net_adress(ipl, mask)
    ntad.set(".".join([str(x) for x in ntadr]))
    bdcst = broadcast(ntadr, mask)
    bdad.set(".".join([str(x) for x in bdcst]))
    rng.set(subrange(ntadr, bdcst))
    subnets, hosts = available(mask, ipl)
    avip.set(f"hosts : {hosts} subnets: {subnets}")


tk.Label(root, text="IP Address").grid(row=0, column=0)
ipfld = tk.Entry(root, textvariable=ip)
ipfld.grid(row=0, column=1)

tk.Label(root, text="Subnet").grid(row=1, column=0)
sbntfld = tk.Entry(root, textvariable=sbnt)
sbntfld.grid(row=1, column=1)

tk.Label(root, text="Subnet").grid(row=1, column=0)
sbntfld = tk.Entry(root, textvariable=sbnt)
sbntfld.grid(row=1, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=2, column=0)
tk.Button(root, text="Clear", command=clean).grid(row=2, column=1)

tk.Label(root, text="Network Address").grid(row=3, column=0)
ntfld = tk.Entry(root, textvariable=ntad)
ntfld.grid(row=3, column=1)

tk.Label(root, text="Broadcast Address").grid(row=4, column=0)
bdfld = tk.Entry(root, textvariable=bdad)
bdfld.grid(row=4, column=1)

tk.Label(root, text="No Of available IP").grid(row=5, column=0)
avipfld = tk.Entry(root, textvariable=avip)
avipfld.grid(row=5, column=1)

tk.Label(root, text="Range").grid(row=6, column=0)
rngfld = tk.Entry(root, textvariable=rng)
rngfld.grid(row=6, column=1)

root.mainloop()
