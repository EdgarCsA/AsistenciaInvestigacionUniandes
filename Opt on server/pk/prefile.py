f=open("file.txt", "r", encoding='utf8')
f1=f.readlines()
f.close()
del f1[:2]
f1 = [x for x in f1 if x != '\n']

f=open("file.txt","w", encoding='utf8')
f.writelines(["%s" % item  for item in f1])
f.close()
