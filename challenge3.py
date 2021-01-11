import convert

def reverse_b_xor(xord, st2):
    
  st2, xord = hexToB2(st2), hexToB2(xord)

  if len(st2) != len(xord):
      return 'Input lengths not equal'

  st1 = ''

  for x in range(len(st2)):
    if st2[x] == '1' and xord[x] == '1':
      st1 += '0'
    elif st2[x] == '1' and xord[x] == '0':
      st1 += '1'
    elif st2[x] == '0' and xord[x] == '1':
      st1 += '1'
    elif st2[x] == '0' and xord[x] == '0':
      st1 += '0'
    else:
      return 'Invalid inputs'
  return B2ToHex(st1)
  
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

def main():
  # For s_1_c_3
  inSt1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
  # Asserting answer
  n = 0
  for i in k_decrypt(inSt1, allKeys()):
    if i == '436f6f6b696e67204d432773206c696b65206120706f756e64206f66206261636f6e':
      print(i, allKeys()[n])
    n+=1
    #Answer for s_1_c_3 = '58'
  if b_xor(inSt1, inSt2) == '746865206b696420646f6e277420706c6179':
    print('s_1_c_2 is correct!')
  else:
    print('Uh-oh, s_1_c_2 is incorrect!')

if __name__ == '__main__':
  main()
