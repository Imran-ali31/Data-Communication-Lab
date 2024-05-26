op = int(input('Press 1 for generating hamming code \nPress 2 for finding and correcting hamming code :'))
if op==1:
    d= input("Enter data bits :")
    data= list(d)
    data.reverse()
    h=[]
    r,c,j=0,0,0
    while(len(data)+r+1 > pow(2,r)):r+=1

    for i in range(0,(r+len(data))):
       p=(2**c)
       if(p==(i+1)):
           h.append(0)
           c+=1
       else:
           h.append(int(data[j]))
           j+=1
    c=0
    for i in range(0,len(h)):
        p=(2**c)
        if p==(i+1):
            st=p-1
            k=st
            t=[]
            while k<len(h):
                block= h[k:k+p]
                t.extend(block)
                k+=2*p
            for z in range(1,len(t)):
                h[st]=h[st]^t[z]
            c+=1
    h.reverse()
    print('Hamming code : ',int(''.join(map(str,h))))

elif op==2 :
    d= input('Enter hamming code :')
    data=list(d)
    data.reverse()
    c,j,h,hc,prt=0,0,[],[],[]
    for i in range(len(data)):
        h.append(int(data[i]))
        hc.append(data[i])
    for i in range(len(h)):
        p=(2**c)
        if p== (i+1):
            st=p-1
            k=st
            t=[]
            while k<len(h):
                blc= h[k:k+p]
                t.extend(blc)
                k+= 2*p
            for z in range(1,len(t)):
                h[st]= h[st]^t[z]
            prt.append(h[st])
            c+=1
    prt.reverse()
    error= sum(int(prt)*(2**i)for i , prt in enumerate(prt[::-1]))

    if(error== 0):
        print('There is no error ')
    elif error >= len(hc):
        print('Error cannot detechted ')
    else:
        print('Error in ',error,'bit')
        if hc[error-1]=='0': hc[error-1]='1'
        elif hc[error-1]=='1': hc[error-1]='0'
        hc.reverse()
        print('After correcting the error code is :')
        print(int(''.join(map(str,hc))))
else: print('Option entered invalid ')