import string

def getencrypt(stringtoencrypt, key, countnum):
    tom = [1,2,0,6,2,0]
    encryptedstring = ""
    cou = 0
    lengthofstring = len(stringtoencrypt)
    while cou<lengthofstring:
        counter = 0
        ch = False
        i = key.find(stringtoencrypt[cou])
        while True:
            while i<len(key):
                if countnum  == counter:
                   
                    if  i <= len(key) - 7:
                        copy=key[i]+key[i+tom[0]]+key[i+tom[1]]+key[i+tom[2]]+key[i+tom[3]]+key[i+tom[4]]+key[i+tom[5]]
                    elif i <= len(key) - 6:
                        copy=key[i]+key[i+tom[0]]+key[i+tom[1]]+key[i+tom[2]]+key[0]+key[i+tom[4]]+key[i+tom[5]]
                    elif i <= len(key) - 5:
                        copy=key[i]+key[i+tom[0]]+key[i+tom[1]]+key[i+tom[2]]+key[1]+key[i+tom[4]]+key[i+tom[5]]
                    elif i <= len(key) - 4:
                        copy=key[i]+key[i+tom[0]]+key[i+tom[1]]+key[i+tom[2]]+key[2]+key[i+tom[4]]+key[i+tom[5]]
                    elif i <= len(key) - 3:
                        copy=key[i]+key[i+tom[0]]+key[i+tom[1]]+key[i+tom[2]]+key[3]+key[i+tom[4]]+key[i+tom[5]]
                    elif i <= len(key) - 2:
                        copy=key[i]+key[i+tom[0]]+key[0]+key[i+tom[2]]+key[4]+key[0]+key[i+tom[5]]
                    elif i <= len(key) - 1:
                        copy=key[i]+key[i+tom[5]]+key[1]+key[i+tom[2]]+key[5]+key[1]+key[i+tom[5]]
                    encryptedstring+=copy
                    ch = True
                    break
                counter+=1
                i+=1
            i=0
            if ch == True:
                break
        cou+=1
        
    return encryptedstring


def encrypt(stringtoencrypt, passw, identifier):
    key = string.printable[:len(string.printable)-6]+" "
    
    ans = 0
    count = 0
    while count<len(passw):
        ans += key.find(passw[count])
        count+=1
    ans +=len(passw)
   
    encryptedstring = ""
    countnum = ans * (identifier + len(key))
    i = 0
    encryptedstring = getencrypt(stringtoencrypt, key, countnum)
    return encryptedstring

def decrypt(encrypted, passw, identifier):
    array = [encrypted[i:i+7] for i in range(0, len(encrypted), 7)]
    key = string.printable[:len(string.printable)-6]+" "
    tom = [1,2,0,6,2,0]
    ans = 0
    count = 0
    while count<len(passw):
        ans += key.find(passw[count])
        count+=1
    ans += len(passw)
    count2 = 0
    countnum =  ans * (identifier + len(key))
    decryptedstring = ""
    cou = 0
    lengthofstring = len(array)
    check = []
    i = 0
    while i<len(key):
        x = getencrypt(key[i], key, countnum)
        check.append(x)
        i+=1
    count3r = 0
    while count3r<lengthofstring:
        i2= 0
        while i2 < len(check):
            if check[i2] == array[count3r]:
                decryptedstring += key[i2]
            i2+=1
        count3r+=1
    return decryptedstring
#g = decrypt("<=><\><OPQOUQOVWXV\"XVVWXV\"XVYZ!Y%!Y",'a0',3)
#print(g)
#g = 'decryptme=\'\'\''+g+'\'\'\''

#with open('stringtoencrypt.txt', 'r') as f:
   #src=f.readlines()
#count=0
#while count<len(src):
    #
    #print(g)
    #count+=1
#src = str(src)
#print(src1)
#sa = decrypt("\]^\|^\4564a64?@[?_[?\]^\|^\4564a64?@[?_[?%&'%+'%0120620\]^\|^\4564a64",'helloworld',int(3))
#count=0
#with open('gosax.txt', 'w') as f:
    #while count<len(src):
        #g = encrypt(src[count],'helloworld',int(3))
        #print(g)
        #f.write(g)
        #f.write("\n")
        #count+=1

    #src1 = src.decode("utf-8")
#g = str(g)
#g = g[2:]
#g = g[:len(g)-1]
#print(g)
#with open('golx.txt', 'r') as f:
    #src = f.read()
    #while count<len(src):
    #g = decrypt(src[count],'helloworld',int(3))
        #print(g)
        #f.write(g)
        #f.write("\n")
        #count+=1
#print(src)
#exec(src)

