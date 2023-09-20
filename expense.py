from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },
]

def get_spender_list():
    spenders = []
    with open("../Py_Expense_template/users.csv", mode = "r", newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            spenders.append(line[0])
    return spenders

def ask_involved(list_involved):
    remainlist = get_spender_list()
    for i in list_involved:
        remainlist.remove(i)
    choices =[]
    for payer in remainlist:
        choices.append({"name": payer})
    choices.append("Leave")

    main_option = {
        "type": "list",
        "name": "main_options",
        "message": "Nouvelle Dépense - Impliqués :" + list_involved.__str__(),
        "choices": choices
    }
    option = prompt(main_option)
    if (option['main_options']) == "Leave":
        if len(list_involved) == 1:
            return get_spender_list()
        else:
            return list_involved
    else:
        list_involved.append(option['main_options'])
        ask_involved(list_involved)
    return list_involved

def new_expense(*args):
    infos = prompt(expense_questions)
    if (infos['spender'] == "" or infos['amount'] == "" or infos['label'] == ""):
        print("Missing information !")
        return False
    try :
        float(infos['amount'])
    except:
        print("Not a number !")
        return False
    if (infos['spender'] not in get_spender_list()):
        print("Spender not found !")
        return False
    involved = ask_involved([infos['spender']])
    f = open("expenses_report.csv", "a")
    f.write(f"{infos['amount']},{infos['label']},{infos['spender']},{involved}\n")
    print("Expense Added !")
    f.close()
    return True

