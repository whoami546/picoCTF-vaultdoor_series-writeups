#!/usr/bin/python3
frace = "hello123"
flag_count = 0
key = "jU5t_a_sna_3lpm12g94c_u_4_m7ra41"
keyword = frace + key + "a"
buffer = ['']*33

string = keyword[len(frace):len(keyword)-1]

while flag_count < 8:
    buffer[flag_count] = string[flag_count]
    flag_count += 1

while flag_count < 16:
    buffer[flag_count] = string[23 - flag_count]
    flag_count += 1

while flag_count < 32:
    buffer[flag_count] = string[46 - flag_count]
    flag_count += 2

flag_count = 31
while flag_count >= 17:
    buffer[flag_count] = string[flag_count]
    flag_count -= 2

print(''.join(buffer) + "a")