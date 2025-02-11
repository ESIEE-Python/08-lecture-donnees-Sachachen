"""code parcourant un fichier et aui lit les donnees"""

#### Imports et définition des variables globales
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires
def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, 'r', encoding ='utf8') as f :
        r = csv.reader(f, delimiter=';')
        l = list(r)
        liste_int = [[int(i) for i in s] for s in l]
        return liste_int

def get_list_k(data, k):
    "prend une sous liste d indice k dans la liste principale"
    l = data
    return l[k]

def get_first(l):
    "prend la premiere valeur de l"
    return l[0]

def get_last(l):
    "prend la derniere valeur de l"
    return l[-1]

def get_max(l):
    "prend la valeur max de l"
    return max(l)

def get_min(l):
    "prend la valeur min de l"
    return min(l)

def get_sum(l):
    "retourne la somme des valeurs de l"
    return sum(l)


#### Fonction principale


def main():
    "fonction principale qui retourne le fichier et la liste demandee"
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
