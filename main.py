#print('hello world')
database = {}
class Budget():
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
    def deposit(self,amount, bal):
        bal -= amount
        return bal
    def withdraw(self, amount, bal):

    def balance(db):
        for cat, bal in db.items():
            print(cat, bal)
    def transfer(db, option1, amount,option2):
        value1 = db[option1]
        value2 = db[option2]

        db[option1] = int(value1) - amount
        db[option2] = int(value2) + amount
        return db
def init():
    print('welcome to the budgetApp \n')
    homepage()

def homepage():
    try:

        user = int(input('\n What would you like to do?: \n (1) create new budget\n (2) deposit into budget\n (3) withdraw\n (4) transfer\n (5) check_balance\n (6) logout\n'))
    except:
        print('invalid option')
        homepage()
    if (user == 1):
        new_budget()
    elif (user == 2):
        deposit-()
    elif (user == 3):
        withdrawal()
    elif (user == 4):
        tranfer()
    elif (user == 5):
        balance
    elif (user == 6):
        logout()
    else:
        print('invalid option\n')

def new_budget():
        print('creating a new budget\n')

        budget_name = input('input budget\n')
        try:
            amount = int(input('Enter your budget amount \n$'))
    except:
        print('invalid option')
        new_budget()

    Budget = Budget(budget_title, amount)
database[budget_title] = amount
    print(f'Budget{budget_title} was setup with ${amount}')
    homepage()


def withdrawal():
    print(' **withdraw from a created budget\n')
    print(f'***Availabe balance***')

    for key,value in database.items():
        print(f'-{key}')

    pick = int(input('press(1) to continue to your withdrawal\n press (2) to cancel withdrawal\n')
    if (pick == 1):
        user = input('select budget category\n')
        if user in database:
            amt = int(input('Enter amount \n$'))
        if amt < database[user]:
            balance = int(database[user])
            new_balance = Budget.withdraw(amount, bal)
        database[user] = new_balance
        print(f'${amt} has been withdrawn from budget{user}\nBudget amount remaining ${new_balance}')
        homepage()

        else:
            pick = int(input(f'\nBudget {user} is insuffecient of the ${amt} required\nBalance {database[user]\n)
            if(pick == 1):
                amt = int(input('enter amount \n$'))
            balance = int(database[user])
            new_balance =   Budget.deposit(amount, bal)
            database[user] = new_balance
            print(f'Budget{user}has been credited with ${amt}\n')
            withdrawal()

        elif (pick == 2):
            withdrawal()
        else:
            print('invalid option\n')
            withdrawal()
def deposit():
    print('***deposit into budget***\n')
    print(f'***Availabe budget***')

    for key, value in database.items():
        print(f'-{key}')

    pick = int(input('press(1) to continue to your deposit\n press (2) to cancel deposit\n'))
    if (pick == 1):
        user = input('select budget category\n')
    if user in database:
        amt = int(input('Enter amount \n$'))
    if amt < database[user]:
        balance = int(database[user])
    new_balance = Budget.deposit(amount, bal)
    database[user] = new_balance
    print(f'${amt} has been deposited with ${amt}\nTotal Budget amount is now ${new_balance}')
    homepage()

    else:
        print('')
        pick = int(input(f'Budget{user} does not exist press (1) to create new budget\n press(2) to deposit funds\n')
        if (pick == 1):
            new_budget()
        elif (pick == 2):
            deposit()
        elif (pick == 3):
            homepage()
        else:
            print('invalid option\n')
            deposit()
    def balance():
        print('****Getting your budget balance***\n')
        check_bal = Budget.balance(database)
        if(check_bal == None):
            print('')
            homepage()
        else:
            print(f'${check_bal}')
            homepage()
    def transfer():
        print('****Available budgets**')
        for key, value in database.items():
            print(key)
        print('***Transfer Operations***')
        for key, value in database.items():
        print(key)
        print('')
    print('**** Transfer Operations ****')
    if from_budget in database:
        from_amount = int(input('Enter amount you want to transfer \n$')
        if from_amount < database[from_budget]:
            to_budget = input('Enter destination of funds \n')
            if to_budget in database:
                db = Budget.transfer(database, from_budget, from_amount, to_budget)
                print('')
                print(f'you transferred ${from_amount} from {from_budget} to {to_budget)
                for key, value in db.items():
                    print(key, value)
                homepage()
            else:
                print(f'\n{from_budget} Budget does not exist, please choose from the valid budget below
                transfer()
      else:
        print(f'insuffecient balance-${from_amount} in {from_budget} budget')
        transfer()
    else:
        print(f'Budget {from_budget} does not exist\n')
        
        transfer()


init()