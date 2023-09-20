from PyInquirer import prompt
from expense import get_spender_list
import csv

def get_all_debts():
    debts = {}
    for spender in get_spender_list():
        debts[spender] = 0
    with open("../Py_Expense_template/expenses.csv", mode = "r", newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            debt = line[0]
            spender = line[2]
            for i in line[3:]:
                if (i != "[") and (i != "]") and (i != " ") and (i != "'"):
                    print(i)
            debts[spender] -= float(debt)
            for i in involved:
                debts[i] += float(debt)/len(involved)
    return debts

#En gros ce que je veux faire :
#Pour chaque dépense, je récupère le montant, le payeur et les impliqués
# que je mets dans une liste de debts
#Je soustrait donc le montant de la dépense au payeur
#Je divise le montant par le nombre d'impliqués et je l'ajoute à chacun des impliqués
#A la fin je boucle sur les montants négatifs avec chaque montant positifs
#Et j'obtiens la liste des dettes (chaque addition final = dette payée)


def get_status():
    # Créez une liste d'utilisateurs
    print(get_all_debts())
    return True