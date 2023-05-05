N=int(input("Ingrese Número De Juegos: "))
NJ=0
NE=0
NM=0
for i in range(1, N+1):
 from random import randint
 
 #Primer Intento Para Juan
 J11=randint(1,6)
 J21=randint(1,6)
 if(J11==4)or(J21==4):
    J=J11+J21-4
 else:
    J=0
 #Segundo Intento Para Juan 
 if (J==1)or(J==2)or(J==3):
    J=randint(1,6)
 if J==0:
    J12=randint(1,6)
    J22=randint(1,6)
 
 if(J12==4)or(J22==4):
    J=J12+J22-4
 else:
    J=0
 
 
 
 #Primer Intento Para Maria
 M11=randint(1,6)
 M21=randint(1,6)
 if(M11==4)or(M21==4):
    M=M11+M21-4
 else:
    M=0
 #Segundo Intento Para Maria
 if (M<=J)and(M!=0):
    M=randint(1,6) 
 if M==0:
    M12=randint(1,6)
    M22=randint(1,6)
 
 if(M12==4)or(M22==4):
    M=M12+M22-4
 else:
    M=0

 #Resultado Final
 if M>J:
     NM=NM+1
 if M==J:
    NE=NE+1
 if M<J:
    NJ=NJ+1

print('De los %i juegos, el %.2f %% los gana Juan'% (N, NJ/N*100))
print('De los %i juegos, el %.2f %% los gana María'% (N, NM/N*100))
print('De los %i juegos, el %.2f %% son empates'% (N, NE/N*100))