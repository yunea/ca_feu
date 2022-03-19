# Echauffement
# Creer un programme qui affiche un rectangle dans le terminal
# Exercice 1 de l'epreuve du feu : feu00.py

import sys


def line(arg):
    #premiere ligne du rectangle dans un tableau
    arg = int(arg)
    line_tab = []
    last_index = arg-1
    while arg > 0:
        line_tab.append("-")
        arg = arg-1
    line_tab[0] = "o"
    line_tab[last_index] = "o"
    return line_tab


def center_line(arg):
    #ligne entre la premiere et la derniere du rectangle dans un tableau
    arg = int(arg)
    line_tab = []
    last_index = arg-1
    while arg > 0:
        line_tab.append(" ")
        arg = arg-1
    line_tab[0] = "|"
    line_tab[last_index] = "|"
    return line_tab


def rectangle(x, y):
    x = int(x)
    y = int(y)
    rectangle_tab = {}
    if y == 1:
        rectangle_tab[0] = line(x)
        return rectangle_tab
    elif y == 2:
        rectangle_tab[0] = line(x)
        rectangle_tab[1] = line(x)
        return rectangle_tab
    else:
        i = y-2
        j = 1
        rectangle_tab[0] = line(x)
        while i > 0:
            rectangle_tab[j] = center_line(x)
            j = j+1
            i = i-1
        rectangle_tab[y-1] = line(x)
        return rectangle_tab


def afficher(rect):
    line = ''
    result = []
    for key, value in rect.items():
        for char in value:
            line = line+char
        result.append(line)
        line = ''
    for str in result:
        print(str)


def two_int_args(args):
    #verifie qu'il y a deux arguments et que se sont des entiers
    if len(args) == 2:
        try:
            for arg in args:
                int(arg)
            return True, ""
        except:
            return False, "Error : arguments must be integer"
    else:
        return False, "Error : two arguments needed"


def arg_is_null(arg1, arg2):
    if int(arg1) == 0 or int(arg2) == 0:
        return True
    else:
        return False


sys.argv.pop(0)
#verifie qu'il y a deux arguments et que se sont des entiers
res_two_int_args, error_message = two_int_args(sys.argv)
if (res_two_int_args == True):
    if (arg_is_null(sys.argv[0], sys.argv[1]) == False):
        rect_tab = rectangle(sys.argv[0], sys.argv[1])
        afficher(rect_tab)
    else:
        print("Error : arguments can not equal zero")
else:
    print(error_message)
