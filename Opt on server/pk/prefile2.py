f=open("Sol200000.txt", "r", encoding='utf8')
d=f.read()
d2=d[:-1]
f.close()
f=open("Sol200000.txt","w", encoding='utf8')
f.write(d2)
f.close()
