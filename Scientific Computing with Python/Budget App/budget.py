class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
    def withdraw(self, amount, description = ""):
        if self.get_balance() - amount >= 0:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    def get_balance(self):
        sum = 0
        for record in self.ledger:
            sum += record["amount"]
        return sum
    def transfer(self, amount, category):
        if self.withdraw(amount,"Transfer to " + category.name):
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False
    def check_funds(self, amount):
        return amount <= self.get_balance()
    def __str__(self):
        s = "*"*(int((30-len(self.name))/2))
        output = (s + self.name + s).rjust(30,"*") + "\n"
        for record in self.ledger:
            output += record["description"][0:23].ljust(23)
            output += "{:.2f}".format(record["amount"]).rjust(7) + "\n"
        output += "Total: " + "{:.2f}".format(self.get_balance())
        return output

def create_spend_chart(categories):
    withdrawals = [0]*len(categories)
    for i in range(len(categories)):
        for j in categories[i].ledger:
            if j["amount"] < 0:
                withdrawals[i] -= j["amount"]
    sum1 = sum(withdrawals)
    percentage = [0]*len(categories)
    for i in range(len(withdrawals)):
        percentage[i] = int(withdrawals[i] / sum1 * 100 / 10)
    r = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    for i in range(len(categories)):
        for j in range(11):
            if j <= percentage[i]:
                r[j][i] = 'o'
    output = "Percentage spent by category\n"
    for i in range(10, -1, -1):
        output += str(i*10).rjust(3) + '|'
        for j in range(len(categories)):
            output += ' ' + r[i][j] + ' '
        output += ' \n'
    output += '    ' + '-'*(len(categories)*3+1) + '\n'
    length, names = [],[]
    for i in range(len(categories)):
        length.append(len(categories[i].name))
    for i in range(len(categories)):
        names.append(categories[i].name.ljust(max(length)))
    for i in range(max(length)):
        output += '    '
        for j in range(len(categories)):
            output += ' ' + names[j][i] + ' '
        output += ' '
        if i != max(length) - 1:
            output += '\n'
    return output