#!/usr/bin/python3
x1 = "0" + bin(1096770097).split('0b')[1] 
x2 = "0" + bin(1952395366).split('0b')[1] 
x3 = "0" + bin(1600270708).split('0b')[1] 
x4 = "0" + bin(1601398833).split('0b')[1]
x5 = "0" + bin(1716808014).split('0b')[1]
x6 = "0" + bin(1734293296).split('0b')[1] 
x7 = "00" + bin(842413104).split('0b')[1]
x8 = "0" + bin(1684157793).split('0b')[1] 
i = 0

def loop(element):
	global i
	while i < 32:
		print(chr(int(eval(f"0b{element[i:i+8]}"))),end="")
		i += 8
	i = 0

print("\nflag : picoCTF{",end="")
loop(x1)
loop(x2)
loop(x3)
loop(x4)
loop(x5)
loop(x6)
loop(x7)
loop(x8)
print("}\n")