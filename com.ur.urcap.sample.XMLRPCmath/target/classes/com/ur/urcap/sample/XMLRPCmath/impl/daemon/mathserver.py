#!/usr/bin/env python

import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import math
import string
import os
import subprocess

def add(a,b):
	print "Received A: " , a
	print "Received B: " , b
	return a+b

def sub(a,b):
	print "Received A: " , a
	print "Received B: " , b
	return a-b
	
def strIndex(str,n):
	print "Received string: ", str
	return str[n]
	
def strCon(stringA,stringB):
	print "String 1: ", stringA
	print "String 2: ", stringB
	return "%s%s" %(stringA,stringB)

def negBool(boo):
	print "Received the boolean: ", boo 
	return not (boo)

 
def lamina(largo, ancho):
    r=open("lamina.txt", "w")
    es=str(largo)+" "+str(ancho)+" 1\n"
    r.write(es)
    r.close()
 
 
def pieza(largo, ancho, cantidad):
    r=open("lamina.txt", "a")
    es2=str(largo)+","+str(ancho)+","+str(cantidad)+" \n"
    r.write(es2)
    r.close()
 


def genPatron():
    ocu=[]
    with open('lamina.txt') as lineas:
        for linea in lineas:
            ocu.append([linea])
        print(ocu)  
        r=open("file.txt", "w")
        te=str(len(ocu)-1)+" 1\n"
        r.write(te)
        te2=ocu[0][0]
        r.write(te2)
        for i in range(len(ocu)-1):
            x,y,can = ocu[i+1][0].split(",")
            g,p=can.split(" ")
            r.write(str(i)+" "+str(x)+" 0 "+str(y)+" 0 1 1 "+str(g)+" 10 999 999  999 0 1 \n")
        r.close()
        es="curl --form file=@file.txt http://www.ingtext.com/ur/pk/receivePost.php"
        pro=subprocess.Popen(es.split(), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (s,err)=pro.communicate()
        s=s.decode()
        g=s.split('\n')
        ocu=[]
        for i in g: ocu.append(i.split("\t"))
        del(ocu[len(ocu)-1])
        print(ocu)
        #El archivo patron 
        r=open("patron.txt", "w")
        move="  movel(pose_trans(Base, p1), a=1.2, v=0.25)\n"
        Abajo="  global p1=pose_trans(plano,p[0,0,-0.05,0,0,0])\n"
        Arriba="  global p1=pose_trans(plano,p[0,0,0.05,0,0,0])\n"
        for i in ocu:
            if len(i)!=2:
                e="  global p1=pose_trans(get_actual_tcp_pose(),p["+str(float(i[0])*0.1)+","+str(float(i[1])*0.1)+",0,0,0,0])\n"
                r.write(e)
                r.write(move)
                r.write(Abajo)
                r.write(move)
                e="  global p1=pose_trans(get_actual_tcp_pose(),p["+str((float(i[3])-float(i[0]))*0.1)+",0,0,0,0,0])\n"
                r.write(e)
                r.write(move)
                e="  global p1=pose_trans(get_actual_tcp_pose(),p[0,"+str((float(i[4])-float(i[1]))*0.1)+",0,0,0,0])\n"
                r.write(e)
                r.write(move)
                e="  global p1=pose_trans(get_actual_tcp_pose(),p[-"+str((float(i[3])-float(i[0]))*0.1)+",0,0,0,0,0])\n"
                r.write(e)
                r.write(move)
                e="  global p1=pose_trans(get_actual_tcp_pose(),p[0,-"+str((float(i[4])-float(i[1]))*0.1)+",0,0,0,0])\n"
                r.write(e)
                r.write(move)
                r.write(Arriba)
                r.write(move)
 
        r.write("end")
        r.close()
 
 
        with open("Part1.txt", "r") as myfile:
            data1=myfile.read()
        myfile.close()
        with open("patron.txt", "r") as myfile:
            data2=myfile.read()
        myfile.close()
        total=data1+"\n"+data2
        f=open('lam1.script',"w") 
        f.write(total)
        f.close()
        os.system("mv lam1.script /home/ur/ursim-current/programs.UR3")
	#os.system("mv lam1.script /programs")
 
def genPatron2():
    ocu=[]
    with open('lamina.txt') as lineas:
        for linea in lineas:
            ocu.append([linea])
        #print(ocu) 
        r=open("file.txt", "w")
        te=str(len(ocu)-1)+" 1\n"
        r.write(te)
        te2=ocu[0][0]
        r.write(te2)
        for i in range(len(ocu)-1):
            x,y,can = ocu[i+1][0].split(",")
            g,p=can.split(" ")
            r.write(str(i)+" "+str(x)+" 0 "+str(y)+" 0 1 1 "+str(g)+" 10 999 999  999 0 1 \n")
        r.close()
        es="curl --form file=@file.txt http://www.ingtext.com/ur/pk/receivePost.php"
        pro=subprocess.Popen(es.split(), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (s,err)=pro.communicate()
        s=s.decode()
        g=s.split('\n')
        ocu=[]
        for i in g: ocu.append(i.split("\t"))
        del(ocu[len(ocu)-1])
        #print(ocu)
        #El archivo patron 
        r=open("patron.txt", "w")
        del(ocu[0])
        del(ocu[0])
        #r.write(str(ocu))
         
        for i in ocu:
            r.write(str(float(i[0])*0.01)+","+str(float(i[1])*0.01)+","+str((float(i[3])-float(i[0]))*0.01)+","+str((float(i[4])-float(i[1]))*0.01)+","+str((float(i[3])-float(i[0]))*-0.01)+","+str((float(i[4])-float(i[1]))*-0.01)+"\n")
        r.close()
    return len(ocu)
 
 
def sshcontrol():
    os.system("bash dr.sh")

#server = SimpleXMLRPCServer(("", 33000), allow_none=True)
server = SimpleXMLRPCServer(("", 33000), allow_none=True)
print "Listening on port 33000..."
server.register_function(add, "add")
server.register_function(sub, "sub")
server.register_function(sshcontrol, "sshcontrol")
server.register_function(strIndex, "strIndex")
server.register_function(strCon, "strCon")
server.register_function(negBool, "negBool")
server.register_function(lamina, "lamina")
server.register_function(pieza, "pieza")
server.register_function(genPatron, "genPatron")
server.register_function(genPatron2, "genPatron2")
server.serve_forever()