import re, os, json, csv, random

class Tracker:

  def __init__(self):
    self.expenses = []
    self.owner = 'Gabriel'

  def __str__(self):
    return f'expenses: {self.expenses}\nowner: {self.owner}'

  def add_expense(self):

    expense = {}

    while True:
      amount = input('Amount: ')
      if amount.isdigit():
        expense['amount'] = amount
        break
      print('Please, input numbers.\n')

    while True:
      category = input('Category: ')
      regex = r'^[a-zA-z]{4,10}$'
      if re.match(regex, category):
        expense['category'] = category
        break
      print('Categories can be "Food", "Groceries", etc. Also it needs to be at least 4 characters long and at max 10 characters long\n')

    while True:
      date = input('Date: ')
      regex = r"^\d{2}/\d{2}/\d{4}$"
      if re.match(regex, date):
        expense['date'] = date
        break
      print('Date format: mm/dd/yyyy')

    while True:
      desc = input('Description: ')
      if len(desc) >= 10 and len(desc.strip()) >= 10:
        expense['description'] = desc
        break
      print('The description needs to have at least 10 words (not including spaces).')

    self.expenses.append(expense)

  def view_expenses(self):
    while True:
      answer = input('\n1. View as JSON\n2. View as CSV\n3. View in the terminal\n4. Go back\n')
      if (answer == '1'):

        if (len(self.expenses) > 0):

          with open(f'{self.owner}_expenses.json', 'w') as json_file:
            json.dump(self.expenses, json_file)
          break

        else:
          print('No expense to show')

      elif (answer == '2'):
        if (len(self.expenses) > 0):

          with open(f'{self.owner}_expenses.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, ['amount', 'category', 'date', 'description'], delimiter='|')
            writer.writeheader()
            writer.writerows(self.expenses)

          # with open('Gabriel_expenses.csv', 'r') as f:
          #   file = csv.reader(f)
          #   for row in file:
          #     if (len(row) == 0):
          #       continue
          #     print(row)
          break

        else:
          print('No expense to show')

      elif (answer == '3'):

        if (len(self.expenses) == 0):
          print('No expense to show')

        print(f'\nExpenses from {self.owner}:\n {self.expenses}\n')
        break

      elif (answer == '4'):
        break

      else:
        print('\nEnter 1 or 2, please.\n')
  
  def monthly_expense_summary(self):
    while True:
      answer = input('What month (by number) you want a summary of?\n')
      if int(answer) <= 12 and int(answer) > 0:

        # filtering just the rows with month given on answer
        def get_month(row):
          date_list = row['date'].split('/')
          return date_list[0] == answer
  
        # filter(callback fn, iterable)
        # creating a list out of the iterator
        filtered_expenses = list(filter(get_month, self.expenses))
        if len(filtered_expenses) == 0:
          print(f'\nNo expenses on month {answer}\n')
          break
 
        # list to keep the amounts prop from the filtered list
        filtered_amounts = []

        # appending all amount props from the filtered list
        for row in filtered_expenses:
          filtered_amounts.append(row['amount'])

        # sum of all amounts
        sum_of_amounts = sum(filtered_amounts)
        
        # median of all amounts
        average_of_amounts = (sum_of_amounts/len(filtered_amounts))

        # creating a dict with all the categories mentioned
        # in the month and counting how many times a expense had it
        categories_dict = {}
        for i in filtered_expenses:
          if i['category'] not in categories_dict:
            categories_dict[i['category']] = 1
          else:
            categories_dict[i['category']] += 1

        # getting the most valued category using max() and the key argument
        mv_categories = max(categories_dict, key=categories_dict.get)

        print(f'\nSummary for the month {answer}:\nTotal number of transactions: {len(filtered_expenses)}\nTotal spent: ${sum_of_amounts} \nAverage amount spent: ${average_of_amounts:.2f} \nMost valued category: {mv_categories}\n')
        break
  
  def seed_expenses(self):
    categories = ['Food', 'Electronic', 'Apparel', 'Invests']
    descs = ['Food for lunch', 'New mobile phone for more memory', 'New and fancy clothes', 'Investments in stocks']
    while True:
      answer = input('How many expenses you want to add?\n')
      if (answer.isdigit()):
        for _ in range(int(answer)):
          expense = {}
          expense['amount'] = self.get_random_int(0, 150)
          expense['category'] = categories[self.get_random_int(0, 3)]
          expense['date'] = f'{self.get_random_int(1, 12)}/{self.get_random_int(1, 30)}/2025'
          expense['description'] = descs[self.get_random_int(0, 3)]
          self.expenses.append(expense)

        print('Seeding executed successfuly')
        break
  
  @staticmethod
  def get_random_int(a: int, b: int):
    return random.randint(a, b)

####### END OF TRACKER CLASS

def main():

  tracker = Tracker()

  while (True):
    answer = input(f'1. Add expense\n2. View expenses\n3. Monthly summary\n4. Seed expenses\n5. Exit\nYour prompt: ')

    if answer == '1':
      tracker.add_expense()
    elif answer == '2':
      tracker.view_expenses()
    elif answer == '3':
      tracker.monthly_expense_summary()
    elif answer == '4':
      tracker.seed_expenses()
    elif answer == '5':
      if os.path.exists('Gabriel_expenses.csv'):
        os.remove('Gabriel_expenses.csv')
      if os.path.exists('Gabriel_expenses.json'):
        os.remove('Gabriel_expenses.json')
      break
    else:
      print('\nEnter 1, 2, 3, 4 or 5.\n')

main()