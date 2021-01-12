from pickle import *
def encrypt(a):
    f=open('creds.dat','wb+')
    dump(a,f)
    print('done')
    f.close()
def decrypt():
    f=open('creds.dat','rb')
    return load(f)
encrypt('5hj4f3hf6gg456g6g3546hj.')
print(decrypt())



