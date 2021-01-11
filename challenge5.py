def k_encrypt(hex_str, key_lst, n):
  str_len = int(len(hex_str)//n)
  ret_lst = []
  for i in key_lst:
    temp_key = ""
    for j in range(str_len):
      temp_key += i
    ret_lst.append(b_xor(hex_str, temp_key))
  return ret_lst
  
def main():
  print("working on this")
  
if __name__ == '__main__':
  main()
