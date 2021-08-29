string2 = '''A broad range of industrial and consumer products use computersascontrolsystems. Simple special-purpose devices like microwave ovens and remote controls are included, as are factory devices like industrial robots and computer-aided design, as well as general-purpose devices like personal 
computers and mobile devices like smartphones. Computers power the Internet, which links hundreds of millions of other computers and users. '''

list=string2.split()
c=0
z=''
for i in list:
    if c<=len(i):
        c=len(i)
        z=i
print(z)
