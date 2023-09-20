from PyInquirer import prompt
user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

def add_user(*args):
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    f = open("users.csv", "a")
    f.write(f"{infos['name']}\n")
    print("User Added !")
    f.close()
    return True