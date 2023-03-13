#!/usr/bin/python3
chars_brute = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_")
def switchBits(c, p1, p2):
    mark1 = 1 << p1
    mark2 = 1 << p2
    bit1 = ord(c) & mark1
    bit2 = ord(c) & mark2
    rest = ord(c) & (255 - (mark1 + mark2))
    shift = p2 - p1
    result = chr((bit1 << shift) | (bit2 >> shift) | rest)
    return result

valid_char = []
def scramble(passwd_chars):
    c = passwd_chars
    c = switchBits(c, 1, 2)
    c = switchBits(c, 0, 3)
    c = switchBits(c, 5, 6)
    c = switchBits(c, 4, 7)
    c = switchBits(c, 0, 1)
    c = switchBits(c, 3, 4)
    c = switchBits(c, 2, 5)
    c = switchBits(c, 6, 7)
    return c

expected = [
        0xF4,
      0xC0,
      0x97,
      0xF0,
      0x77,
      0x97,
      0xC0,
      0xE4,
      0xF0,
      0x77,
      0xA4,
      0xD0,
      0xC5,
      0x77,
      0xF4,
      0x86,
      0xD0,
      0xA5,
      0x45,
      0x96,
      0x27,
      0xB5,
      0x77,
      0xD2,
      0xD0,
      0xB4,
      0xE1,
      0xC1,
      0xE0,
      0xD0,
      0xD0,
      0xE0
      ]
b = 0
while b < len(expected):
    for i in chars_brute:
        if chr(expected[b]) == scramble(i):
            valid_char.append(i)
    b += 1

print(f"\n\n[+] flag : picoCTF{chr(123)}{''.join(valid_char)}{chr(125)}\n\n")
