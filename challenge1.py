import sys
import convert
import re

def main():
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
