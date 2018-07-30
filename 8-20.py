block="*"
b=[]
b.append(block*4)

def mask_security_number(security_number):
    securenum=list(security_number)

    del securenum[-4:]
    masksecuurenum=securenum+b
    print(masksecuurenum)

    sum=""
    for i in masksecuurenum:
        sum=sum+i
    return sum

print(mask_security_number("880720-1234567"))