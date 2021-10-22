def fun(n):
    if n<10:
        return 1
    else:
        return 1+fun(n//10)

def cCrypt(data, key, op):
    dataList = list(data)
    cipher = list()
    if op ==1:
        for c in dataList:
            cipher.append(chr(ord(c+key)))
            return"".join(cipher)
    else:
        for c in dataList:
            cipher.append(chr(ord(c-key)))
        return"".join(cipher)
