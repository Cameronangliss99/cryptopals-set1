import convert

def s_1_c_4():

    c4 = open('s_1_c_4.txt', 'r')
    c4 = c4.read()
    c4 = c4.split()
    ret_lst = []

    # for i in c4:
    #     ret_lst.append(i[:-1])

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
