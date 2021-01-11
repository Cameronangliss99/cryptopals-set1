#Nik and Cam
#Base conversions

import base64
import codecs
import math

def bin2Hex(st):
    return hex(int(st, 2))[2:]

def bin2Base64(st):
    st = bin2Hex(st)
    return hex2Base64(st)

def bin2Plain(st):
    return eval(str(codecs.decode(bin2Hex(st), "hex"))[1:])

def hex2Bin(st):
    return bin(int(st, 16))[2:]

def hex2Base64(st):
    return codecs.encode(codecs.decode(st, 'hex'), 'base64').decode().replace("\n", "")

def hex2Plain(st):
    if len(st) % 2 != 0:
        st = '0' + st
    return eval(str(codecs.decode(st, "hex"))[1:])
        # print(st)

def base642Bin(st):
    hexSt = base642Hex(st)
    return hex2Bin(hexSt)

def base642Hex(st):
    return base64.b64decode(st).hex()

def base642Plain(st):
    hexSt = base642Hex(st)
    return hex2Plain(hexSt)

def plain2Bin(st):
    b = st.encode()
    return hex2Bin(codecs.encode(b, "hex"))

def plain2Hex(st):
    b = st.encode()
    return str(codecs.encode(b, "hex"))[2:-1]

def plain2Base64(st):
    hexSt = plain2Hex(st)
    return hex2Base64(hexSt)    

## ENCRYPT/DECRYPT
def k_decrypt(hex_str, key_lst):

    str_len = math.ceil(len(hex_str)/(len(key_lst[0])))
    # print(str_len)
    ret_lst = []

    for i in key_lst:
        temp_key = ""
        for j in range(str_len):
            temp_key += i
        # print(len(hex_str), len(temp_key))
        ret_lst.append([reverse_b_xor(hex_str, temp_key[:len(hex_str)]), i])

    return ret_lst

def fltr(hex_str):
    # if hex_str == None:
    #     return
    temp = ""
    for i in hex_str:
        if i.lower() in "abcdefghijklmnopqrstuvwxyz !?,.;:_-'\"":
            temp += i
    return temp

def getKey(item):
    return item[0][0]

def test():
    
    binStr = '11010000110010101101100011011000110111100000001'
    hexStr = '001fd'
    base64Str = 'aGVsbG8B'
    plainStr = "hello\x01"
    
    #Test functions:
    # print('Binary to Test')
    # print(bin2Hex(binStr))
    # print(bin2Base64(binStr))
    # print(bin2Plain(binStr))
    # print()

    print('Hex to Test')
    # print(hex2Bin(hexStr))
    # print(hex2Base64(hexStr))
    print(hex2Plain(hexStr))
    # print()

    # print('Base64 to Test')
    # print(base642Bin(base64Str))
    # print(base642Hex(base64Str))
    # print(base642Plain(base64Str))
    # print()

    # print('Plain to Test')
    # print(plain2Bin(plainStr))
    # print(plain2Hex(plainStr))
    # print(plain2Base64(plainStr))

if __name__ == "__main__":
    test()
