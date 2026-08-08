a="AAAAAAABBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEEEEFFFFFFFFFFFGGGGGGGG"
l=""
for i in a:
    b = len(l)
    if b==0:
        l=l+i
    else:
      for j in l:
          if i==j:
              pass
          else:
              l=l+i
print(l)


