# Archivo de compilación para el algoritmo genético que emplea la codificación de Prins y Liu
# 14-08-13
# Versión 1.0

#En la terminal: g++ principal.cpp -o principal.x y luego ./principal.x
#Optimización: -O0 -O1 -O2 -O3 (Optimizar código, vectorización)
#-g (Depurar código)



#CCOPT = -m32 -O -fPIC -fno-strict-aliasing -fexceptions -DNDEBUG -DIL_STD

##### Cambiar /m32 a 64 en la siguiente linea 
CCOPT = -m64  -fPIC -fno-strict-aliasing -fexceptions -DNDEBUG -DIL_STD 
#CCOPT = -m64 -Ofast -fPIC -fno-strict-aliasing -fexceptions -DNDEBUG -DIL_STD -lgraph -lGL -lglut
#CCOPT = -Os -finline-functions -finline-small-functions -D_GLIBCXX_PROFILE -g -L/usr/lib/nvidia-304/ -lGL -lglut
#CCOPT = -Os -L/usr/lib/nvidia-304/ -lGL -lglut
#CCOPT = -Os -finline-functions -finline-small-functions  -L/usr/lib/nvidia-304/ -lGL -lglut

CCLNFLAGS = -Os 
#CCLNFLAGS = -Os -finline-functions -finline-small-functions -D_GLIBCXX_PROFILE -g -lGL -lglut
#CCLNFLAGS = -Os -finline-functions -finline-small-functions -lGL -lglut

CCFLAGS = $(CCOPT) 

#-------------------------------------
#Invocar al compilador
CC = g++
#CCFLAGS = -Ofast
#CCFLAGS = -Ofast -g
#CCFLAGS =  -g
#CCFLAGS = -O3
#-------------------------------------
#Definición de módulos
#Modulos = Algoritmos Container DibujarOpenGL principal
Modulos = Algoritmos Container principal
#-------------------------------------
all:
		make all_cpp
clean:
		-rm *.o *.x		
all_cpp: $(Modulos)
ejecutar:
			../program.x datos.txt
#-------------------------------------
#Creación de módulos

# -c es para crear archivos auxiliares compilados
# -o indica que la salida del compilado queda en el archivo que se nombra a continuación en la instrucción (.o es equivalente a un dll de windows)
# -std=11 Nuevo estándar de c para manejar la función random
# -g para entrar a modo de depuración
# -w mostrar en pantalla avisos (equivalente a -Wall)


Algoritmos:
	$(CC) -c $(CCFLAGS) Algoritmos.cpp -o Algoritmos.o
	
Container:
	$(CC) -c $(CCFLAGS) Container.cpp -o Container.o
		
DibujarOpenGL:
	$(CC) -c $(CCFLAGS) DibujarOpenGL.cpp -o DibujarOpenGL.o
	
principal.o:
		$(CC) $(CCFLAGS) -c clp.cpp -o principal.o
		
principal: principal.o
	$(CC) $(CCFLAGS) Algoritmos.o Container.o principal.o -o program.x $(CCLNFLAGS)
	
actualizarPrincipal:
	-rm principal.o	
	make principal	
	../program.x

directorio = /home/pparalelo/Escritorio/Packing/individualizadas/

correccion:
	#./program.x $(directorio)hola.txt 1 1 3 4 1
	#./program.x $(directorio)hola.txt 1 2 3 1 1
	./program.x $(directorio)ceschia_CS2000.txt 1 1 3 4 1

lote1:
	./program.x $(directorio)ceschia_CS2000.txt 1 1 3 4 1
	./program.x $(directorio)ceschia_CS2805.txt 1 1 3 4 1
	./program.x $(directorio)ceschia_CS2822.txt 1 1 3 4 1
	./program.x $(directorio)ceschia_CS2843.txt 1 1 3 4 1
	./program.x $(directorio)ceschia_CS2899.txt 1 1 3 4 1
	./program.x $(directorio)ceschia_CS3048.txt 1 1 3 4 1
	./program.x $(directorio)ceschia_CS3056.txt 1 1 3 4 1

lote2:
	./program.x $(directorio)ceschia_CS3074.txt 1 1 3 4 2
	./program.x $(directorio)ceschia_CS3122.txt 1 1 3 4 2
	./program.x $(directorio)ceschia_CS3142.txt 1 1 3 4 2
	./program.x $(directorio)ceschia_CS3151.txt 1 1 3 4 2
	./program.x $(directorio)ceschia_CS3152.txt 1 1 3 4 2
	./program.x $(directorio)ceschia_CS3182.txt 1 1 3 4 2
	./program.x $(directorio)ceschia_CS3203.txt 1 1 3 4 2
	
lote3:
	./program.x $(directorio)ceschia_CS3207.txt 1 1 3 4 3
	./program.x $(directorio)ceschia_CS3291.txt 1 1 3 4 3
	./program.x $(directorio)ceschia_CS3314.txt 1 1 3 4 3
	./program.x $(directorio)ceschia_CS3388.txt 1 1 3 4 3
	./program.x $(directorio)ceschia_CS3432.txt 1 1 3 4 3
	./program.x $(directorio)ceschia_CS3556.txt 1 1 3 4 3
	./program.x $(directorio)ceschia_CS3695.txt 1 1 3 4 3
	./program.x $(directorio)ceschia_CS3915.txt 1 1 3 4 3
	./program.x $(directorio)ceschia_CS3941.txt 1 1 3 4 3

lote4:
	./program.x $(directorio)NLBR_1_1_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_2_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_3_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_4_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_5_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_6_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_7_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_8_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_9_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_10_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_11_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_12_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_13_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_14_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_15_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_16_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_17_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_18_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_19_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_20_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_21_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_22_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_23_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_24_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_25_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_26_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_27_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_28_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_29_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_30_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_31_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_32_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_33_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_34_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_35_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_36_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_37_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_38_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_39_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_40_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_41_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_42_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_43_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_44_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_45_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_46_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_47_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_48_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_49_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_50_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_51_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_52_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_53_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_54_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_55_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_56_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_57_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_58_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_59_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_60_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_61_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_62_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_63_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_64_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_65_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_66_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_67_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_68_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_69_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_70_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_71_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_72_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_73_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_74_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_75_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_76_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_77_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_78_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_79_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_80_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_81_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_82_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_83_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_84_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_85_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_86_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_87_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_88_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_89_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_90_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_91_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_92_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_93_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_94_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_95_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_96_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_97_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_98_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_99_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_1_100_1.txt 1 2 3 2 1

lote5:
	./program.x $(directorio)NLBR_2_1_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_2_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_3_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_4_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_5_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_6_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_7_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_8_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_9_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_10_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_11_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_12_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_13_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_14_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_15_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_16_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_17_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_18_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_19_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_20_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_21_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_22_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_23_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_24_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_25_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_26_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_27_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_28_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_29_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_30_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_31_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_32_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_33_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_34_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_35_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_36_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_37_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_38_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_39_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_40_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_41_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_42_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_43_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_44_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_45_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_46_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_47_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_48_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_49_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_50_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_51_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_52_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_53_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_54_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_55_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_56_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_57_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_58_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_59_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_60_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_61_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_62_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_63_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_64_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_65_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_66_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_67_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_68_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_69_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_70_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_71_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_72_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_73_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_74_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_75_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_76_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_77_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_78_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_79_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_80_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_81_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_82_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_83_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_84_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_85_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_86_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_87_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_88_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_89_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_90_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_91_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_92_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_93_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_94_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_95_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_96_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_97_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_98_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_99_1.txt 1 2 3 2 2
	./program.x $(directorio)NLBR_2_100_1.txt 1 2 3 2 2

lote6:
	./program.x $(directorio)NLBR_3_1_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_2_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_3_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_4_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_5_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_6_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_7_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_8_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_9_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_10_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_11_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_12_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_13_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_14_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_15_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_16_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_17_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_18_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_19_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_20_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_21_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_22_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_23_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_24_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_25_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_26_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_27_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_28_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_29_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_30_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_31_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_32_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_33_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_34_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_35_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_36_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_37_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_38_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_39_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_40_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_41_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_42_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_43_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_44_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_45_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_46_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_47_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_48_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_49_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_50_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_51_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_52_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_53_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_54_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_55_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_56_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_57_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_58_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_59_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_60_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_61_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_62_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_63_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_64_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_65_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_66_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_67_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_68_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_69_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_70_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_71_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_72_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_73_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_74_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_75_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_76_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_77_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_78_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_79_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_80_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_81_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_82_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_83_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_84_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_85_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_86_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_87_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_88_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_89_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_90_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_91_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_92_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_93_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_94_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_95_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_96_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_97_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_98_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_99_1.txt 1 2 3 2 3
	./program.x $(directorio)NLBR_3_100_1.txt 1 2 3 2 3

lote7:
	./program.x $(directorio)NLBR_4_1_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_2_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_3_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_4_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_5_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_6_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_7_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_8_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_9_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_10_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_11_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_12_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_13_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_14_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_15_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_16_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_17_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_18_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_19_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_20_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_21_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_22_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_23_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_24_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_25_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_26_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_27_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_28_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_29_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_30_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_31_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_32_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_33_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_34_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_35_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_36_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_37_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_38_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_39_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_40_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_41_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_42_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_43_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_44_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_45_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_46_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_47_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_48_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_49_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_50_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_51_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_52_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_53_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_54_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_55_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_56_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_57_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_58_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_59_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_60_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_61_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_62_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_63_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_64_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_65_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_66_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_67_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_68_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_69_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_70_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_71_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_72_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_73_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_74_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_75_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_76_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_77_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_78_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_79_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_80_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_81_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_82_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_83_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_84_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_85_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_86_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_87_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_88_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_89_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_90_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_91_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_92_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_93_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_94_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_95_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_96_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_97_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_98_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_99_1.txt 1 2 3 2 4
	./program.x $(directorio)NLBR_4_100_1.txt 1 2 3 2 4	

lote8:
	./program.x $(directorio)NLBR_5_1_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_2_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_3_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_4_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_5_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_6_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_7_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_8_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_9_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_10_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_11_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_12_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_13_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_14_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_15_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_16_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_17_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_18_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_19_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_20_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_21_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_22_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_23_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_24_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_25_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_26_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_27_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_28_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_29_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_30_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_31_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_32_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_33_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_34_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_35_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_36_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_37_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_38_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_39_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_40_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_41_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_42_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_43_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_44_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_45_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_46_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_47_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_48_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_49_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_50_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_51_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_52_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_53_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_54_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_55_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_56_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_57_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_58_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_59_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_60_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_61_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_62_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_63_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_64_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_65_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_66_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_67_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_68_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_69_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_70_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_71_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_72_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_73_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_74_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_75_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_76_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_77_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_78_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_79_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_80_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_81_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_82_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_83_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_84_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_85_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_86_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_87_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_88_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_89_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_90_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_91_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_92_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_93_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_94_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_95_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_96_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_97_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_98_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_99_1.txt 1 2 3 2 5
	./program.x $(directorio)NLBR_5_100_1.txt 1 2 3 2 5

lote9:
	./program.x $(directorio)NLBR_6_1_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_2_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_3_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_4_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_5_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_6_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_7_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_8_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_9_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_10_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_11_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_12_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_13_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_14_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_15_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_16_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_17_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_18_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_19_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_20_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_21_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_22_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_23_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_24_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_25_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_26_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_27_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_28_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_29_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_30_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_31_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_32_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_33_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_34_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_35_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_36_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_37_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_38_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_39_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_40_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_41_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_42_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_43_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_44_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_45_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_46_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_47_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_48_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_49_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_50_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_51_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_52_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_53_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_54_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_55_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_56_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_57_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_58_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_59_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_60_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_61_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_62_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_63_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_64_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_65_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_66_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_67_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_68_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_69_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_70_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_71_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_72_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_73_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_74_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_75_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_76_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_77_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_78_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_79_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_80_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_81_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_82_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_83_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_84_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_85_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_86_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_87_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_88_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_89_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_90_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_91_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_92_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_93_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_94_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_95_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_96_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_97_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_98_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_99_1.txt 1 2 3 2 6
	./program.x $(directorio)NLBR_6_100_1.txt 1 2 3 2 6

lote10:
	./program.x $(directorio)NLBR_7_1_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_2_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_3_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_4_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_5_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_6_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_7_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_8_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_9_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_10_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_11_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_12_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_13_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_14_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_15_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_16_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_17_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_18_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_19_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_20_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_21_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_22_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_23_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_24_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_25_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_26_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_27_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_28_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_29_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_30_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_31_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_32_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_33_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_34_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_35_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_36_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_37_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_38_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_39_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_40_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_41_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_42_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_43_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_44_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_45_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_46_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_47_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_48_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_49_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_50_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_51_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_52_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_53_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_54_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_55_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_56_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_57_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_58_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_59_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_60_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_61_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_62_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_63_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_64_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_65_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_66_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_67_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_68_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_69_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_70_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_71_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_72_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_73_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_74_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_75_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_76_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_77_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_78_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_79_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_80_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_81_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_82_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_83_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_84_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_85_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_86_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_87_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_88_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_89_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_90_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_91_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_92_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_93_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_94_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_95_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_96_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_97_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_98_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_99_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_7_100_1.txt 1 2 3 2 1

lote11:
	./program.x $(directorio)NLBR_8_1_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_2_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_3_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_4_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_5_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_6_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_7_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_8_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_9_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_10_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_11_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_12_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_13_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_14_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_15_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_16_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_17_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_18_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_19_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_20_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_21_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_22_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_23_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_24_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_25_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_26_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_27_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_28_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_29_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_30_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_31_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_32_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_33_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_34_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_35_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_36_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_37_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_38_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_39_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_40_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_41_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_42_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_43_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_44_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_45_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_46_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_47_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_48_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_49_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_50_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_51_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_52_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_53_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_54_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_55_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_56_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_57_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_58_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_59_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_60_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_61_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_62_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_63_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_64_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_65_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_66_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_67_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_68_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_69_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_70_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_71_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_72_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_73_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_74_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_75_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_76_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_77_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_78_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_79_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_80_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_81_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_82_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_83_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_84_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_85_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_86_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_87_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_88_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_89_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_90_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_91_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_92_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_93_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_94_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_95_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_96_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_97_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_98_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_99_1.txt 1 2 3 2 1
	./program.x $(directorio)NLBR_8_100_1.txt 1 2 3 2 1
#-------------------------------------
