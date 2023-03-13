#!/usr/bin/python3
decimal = [106, 85, 53, 116, 95, 52, 95, 98]
hexadecimal = [0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f]
octal = [0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o146, 0o64]
char = ['a' , '8' , 'c' , 'd' , '8' , 'f' , '7' , 'e']

list_flag = []

def do_append(data):
    for i in data:
        list_flag.append(chr(i))

do_append(decimal)
do_append(hexadecimal)
do_append(octal)
print("\n\nflag : picoCTF{" + ''.join(list_flag) + ''.join(char) + "}\n")
