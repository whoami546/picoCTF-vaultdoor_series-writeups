#!/usr/bin/python3
myBytes = [0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x66, 0x36, 0x30, 0x67, 0x6c, 0x64, 0x6c]

flag = []
i = 0
list_int = []
while i < 32:
    for _ in range(1,1000):
        if ((_ ^ 0x55) - myBytes[i]) == 0:
            list_int.append(_)
    i += 1

for integers in list_int:
    flag.append(chr(integers))
print("\n\nflag : picoCTF{%s}\n" % (''.join(flag)))