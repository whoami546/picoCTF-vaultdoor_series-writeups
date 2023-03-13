#!/usr/bin/python3
from base64 import b64decode
from urllib import parse

value = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
value += "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
value += "JTM0JTVmJTM4JTM0JTY2JTY0JTM1JTMwJTM5JTM1"

url_str = b64decode(value).decode()
flag = "picoCTF{" +  parse.unquote(url_str) + "}"

print("\n\nflag : %s\n" % flag)