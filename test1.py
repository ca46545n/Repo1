G = input("Please type a word: " )
f = ''
p = ''

for letters in G:
    if letters in G.lower():
        f += letters
    elif letters in G.upper():
        p += letters
for letter in p or letter in f:
    k = p.replace(" ", '')
    t = f.replace(" ", '')
print('No. of Upper case characters : {}'.format(len(k)))
print('No. of Lower case characters : {} '.format(len(t)))
