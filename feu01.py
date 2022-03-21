#Evaluer une expression
#Recoit une expression arithmetique dans une chaine de caracteres et en retourne le resultat apres l'avoir calcule
#Exercice 2 de l'epreuve du feu : feu01.py
import sys


def str_to_tab(chaine):
    result = chaine.split(' ')
    return result


def parentheses(chaine):
    str_in_par = ''
    tab_in_par = []
    #recuperation chaine entre parenthèse
    for car in chaine:
        if car == "(":
            if car == ")":
                tab_in_par.append(str_in_par)
                str_in_par = ''
            else:
                str_in_par = str_in_par+str(car)
    #TODO: calculer ce qu'il y a dans les parentheses
    #TODO: renvoyer le calcul avec les parenthèses remplacees par le resultat
    return tab_in_par


def multiplication(chaine):
    i = 0
    j = 0
    res = 0
    result = []
    result1 = []
    result2 = []
    for car in chaine:
        if car == "*":
            j = chaine[i+1]
            res = int(chaine[i-1])*int(chaine[i+1])
            index = len(result1)-1
            result1.pop(index)
            result1.append(str(res))
            break
        else:
            result1.append(car)
        i = i+1
    i = 0
    for car in chaine:
        if car == str(j):
            if chaine[i-1] == "*":
                l = len(result2)
                while l > 0:
                    result2.pop(l-1)
                    l = l-1
        else:
            result2.append(car)
        i = i+1
    for r in result1:
        result.append(r)
    for r in result2:
        result.append(r)
    print(result)


#--------main-------
sys.argv.pop(0)
if len(sys.argv) == 1:
    calcul = str_to_tab(sys.argv[0])
    multiplication(calcul)
else:
    print("Error : 1 argument needed")
