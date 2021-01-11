import convert

def b_xor(st1, st2):
  st1, st2 = hexToB2(st1), hexToB2(st2)
  if len(st1) != len(st2):
    return 'Input lengths not equal'
  ret_str = ''
  for x in range(len(st1)):
    if st1[x] == st2[x]:
      ret_str += '0'
    else:
      ret_str += '1'
  ret_str = B2ToHex(ret_str)
  return ret_str
  
def main():
  hex_str1 = "1c0111001f010100061a024b53535009181c"
  hex_str2 = "686974207468652062756c6c277320657965"
  if b_xor(hex_str1, hex_str2) == "746865206b696420646f6e277420706c6179":
    print("Success! Challenge 2 completed!")
  else:
    print("Keep trying...")

if __name__ == '__main__':
  main()
