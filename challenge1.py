import sys
import convert
import re

def allKeys(n):

    hex_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    
    if n == 1:
        return hex_lst
    else:
        return allKeysr(n, n - 1, [], hex_lst, hex_lst)

def allKeysr(n, c, new_lst, old_lst, hex_lst):
    if c == 0:
        return old_lst
    else:
        for i in range(len(old_lst)):
            for j in range(len(hex_lst)):
                new_lst.append(old_lst[i] + hex_lst[j])
        return allKeysr(n, c-1, [], new_lst, hex_lst)

def k_encrypt(hex_str, key_lst, n):

    str_len = int(len(hex_str)//n)
    ret_lst = []

    for i in key_lst:
        temp_key = ""
        for j in range(str_len):
            temp_key += i
        ret_lst.append(b_xor(hex_str, temp_key))

    return ret_lst

def getBasicFit(st):
    score = 0
    for i in st:
        letter = i.lower()
        if letter in "zqxj":
            score += 0
        elif letter in 'kv':
            score += 1
        elif letter in 'bpygfwmuc':
            score += 2
        elif letter in 'ld':
            score += 3
        elif letter in 'rhsni':
            score += 4
        elif letter in 'oa':
            score += 5
        elif letter == 't':
            score += 6
        elif letter == 'e':
            score += 8
        else:
            score += 0
    return score

def getAdvFit(st):
    score = 0
    n_list = ['bx', 'cj', 'cv', 'cx', 'dx', 'fq', 'fx', 'gq', 'gx', 'hx', 'jc', 'jf', 'jg', 'jq', 'js', 'jv', 'jw', 'jx', 'jz', 'kq', 'kx', 'mx', 'px', 'pz', 'qb', 'qc', 'qd', 'qf', 'qg', 'qh', 'qj', 'qk', 'ql', 'qm', 'qn', 'qp', 'qs', 'qt', 'qv', 'qw', 'qx', 'qy', 'qz', 'sx', 'vb', 'vf', 'vh', 'vj', 'vm', 'vp', 'vq', 'vt', 'vw', 'vx', 'wx', 'xj', 'xx', 'zj', 'zq', 'zx']
    for i in range(len(st) - 1):
        lt1 = st[i]
        lt2 = st[i + 1]
        if lt1.lower() + lt2.lower() in n_list or lt2.lower() + lt1.lower() in n_list:
            score -= 100
    return score
        
def h_dist(str1, str2):
    if len(str1) == len(str2):
        ret_count = 0
        for k in range(len(str1)):
            if str1[k] == str2[k]:
                pass
            else:
                ret_count+= 1
        return ret_count
    else:
        return 'Input strings not the same length'

# SOLUTION FOR S_!_C_4
def getKey(item):
    return item[0]

def main():

    # print(B642B2('l0=='))

    # tStr1 = plain2bin("this is a test")
    # tStr2 = plain2bin("wokka wokka!!!")
    # print(h_dist(tStr1, tStr2))

    # tStr = 'Nikesh'
    # print(plain2bin(tStr)[2:])
    
    # For Challenge 1
    
    hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    b64_str = convert.hex2Base64(hex_str)
    if b64_str == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t":
        print("Success! Challenge 1 completed!")
    else:
        print("Keep trying...")

if __name__ == '__main__':
    main()

# sys.setdefaultencoding()

# for i in s_1_c_4_solution():
#     try:
#         bytes_object = bytes.fromhex(i)
#         try:
#             ascii_string = bytes_object.decode("ASCII")
#             txt.write(ascii_string + '\n')
#         except:
#             pass
#     except Exception as e:
#         print(ascii_string, e)
#     txt.write(ascii_string)
# txt.close()

# print(bytes.fromhex('f1c9b817a6d2caaeb5f7edbca7dac912c2198cbfa6ffe1c0aca319d8efcd').decode('latin-1'))

# str_test = k_encrypt('f1c9b817a6d2caaeb5f7edbca7dac912c2198cbfa6ffe1c0aca319d8efcd', ['a'], 1)
# print(str_test)
# str_test2 = k_decrypt('5b6312bd0c7860041f5d47160d7063b868b326150c554b6a0609b3724567', ['a'], 1)
# print(str_test2)

# # For s_1_c_1
# inStr = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
# if hexToB64(inStr) == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t':
#     print('s_1_c_1 is correct!')
# else:
#     print('Uh-oh, s_1_c_1 is incorrect!')
#     print(hexToB64(inStr))


# # For s_1_c_2
# inSt1 = '1c0111001f010100061a024b53535009181c'
# inSt2 = '686974207468652062756c6c277320657965'
# # Asserting answer
# if b_xor(inSt1, inSt2) == '746865206b696420646f6e277420706c6179':
#     print('s_1_c_2 is correct!')
# else:
#     print('Uh-oh, s_1_c_2 is incorrect!')

# # For s_1_c_3
# inSt1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# # Asserting answer
# n = 0
# for i in k_decrypt(inSt1, allKeys()):
#     if i == '436f6f6b696e67204d432773206c696b65206120706f756e64206f66206261636f6e':
#         print(i, allKeys()[n])
#     n+=1
#     #Answer for s_1_c_3 = '58'
# if b_xor(inSt1, inSt2) == '746865206b696420646f6e277420706c6179':
#     print('s_1_c_2 is correct!')
# else:
#     print('Uh-oh, s_1_c_2 is incorrect!')
# 436f6f6b696e67204d432773206c696b65206120706f756e64206f66206261636f6e

