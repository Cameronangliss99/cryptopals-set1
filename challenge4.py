import convert

def s_1_c_4():
    c4 = open('s_1_c_4.txt', 'r')
    c4 = c4.read()
    c4 = c4.split()
    ret_lst = []
    # for i in c4:
    #   ret_lst.append(i[:-1])
    return c4

def s_1_c_4_solution():
    ret_lst = []
    n = 2
    for i in s_1_c_4():
        # print(i)
        k_str = k_decrypt(i, allKeys(n), n)
        # print(k_str)
        for j in k_str:
            ret_lst.append(j)
    return ret_lst

def getKey(item):
    return item[0]

def main:
    txt = open('sample_solution_s_1_c_4_decoded.txt', 'w', encoding = 'latin-1')
    s_list = s_1_c_4_solution()
    f_list = []
    for i in s_list:
        # print(i)
        hex_string = bytes.fromhex(i).decode('latin-1')
        fltr_str = fltr(hex_string)
        f_list.append([getBasicFit(fltr_str) + getAdvFit(fltr_str), fltr_str])
    f_list = sorted(f_list, key = getKey)
    for i in f_list:
        txt.write(i[1] + '\n' + 'SCORE: ' + str(i[0]) +'\n\n')
    txt.close()

if __name__ == '__main__':
    main()

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
