from random import randint
print('\nEl juego inicia para Juan')
#Primer Intento Para Juan
print(' Juan hace un primer intento')
J11=randint(1,6)
J21=randint(1,6)
print(' Obtiene %i en el primer dado'%J11)
print(' obtiene %i en el segundo dado'%J21)
if(J11==4)or(J21==4):
 J=J11+J21-4
else:
 J=0
print(' Su puntaje es %i en el primer intento'%J)
#Segundo Intento Para Juan
if (J==4)or(J==5)or(J==6):
 print(' Juan se planta en su puntaje')
if (J==1)or(J==2)or(J==3):
 print(' Juan mejora su puntaje')
 J=randint(1,6)
 print(' Obtiene %i en el dado lanzado'%J)
if J==0:
 print(' Juan hace un segundo intento')
 J12=randint(1,6)
 J22=randint(1,6)
 print(' Obtiene %i en el primer dado'%J12)
 print(' Obtiene %i en el segundo dado'%J22)
 if(J12==4)or(J22==4):
    J=J12+J22-4
 else:
    J=0
print(' Su puntaje es %i en el segundo intento'%J) 
#Resultado del Juego Para Juan
print('Juan tiene un puntaje final de',J) 
print('\nEl juego inicia para María')
#Primer Intento Para Maria
print(' María hace un primer intento')
M11=randint(1,6)
M21=randint(1,6)
print(' Obtiene %i en el primer dado'%M11)
print(' obtiene %i en el segundo dado'%M21)
if(M11==4)or(M21==4):
 M=M11+M21-4
else:
 M=0
print(' Su puntaje es %i en el primer intento'%M)
#Segundo Intento Para Maria
if M>J:
 print(' María se planta en su puntaje')
if (M<=J)and(M!=0):
 print(' María mejora su puntaje')
 M=randint(1,6)
 print(' Obtiene %i en el dado lanzado'%M)
if M==0:
 print(' María hace un segundo intento')
 M12=randint(1,6)
 M22=randint(1,6)
 print(' Obtiene %i en el primer dado'%M12)
 print(' Obtiene %i en el segundo dado'%M22)
 if(M12==4)or(M22==4):
    M=M12+M22-4
 else:
    M=0


print(' Su puntaje es %i en el segundo intento'%M)
#Resultado del Juego Para María
print('María tiene un puntaje final de',M)
#Resultado Final
print('\nJuan %i vs %i Maria' % (J, M))
if M>J:
 print('La Ganadora es Maria')
if M==J:
 print('Juan y Maria Empatan')
if M<J:
 print('El Ganador es Juan')