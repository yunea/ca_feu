#Evaluer une expression
#Recoit une expression arithmetique dans une chaine de caracteres et en retourne le result apres l'avoir calcule
#Exercice 2 de l'epreuve du feu : feu01.py
import sys

sys.argv.pop(0)
if len(sys.argv) == 1:
    print(sys.argv)
else:
    print("Error : 1 argument needed")
