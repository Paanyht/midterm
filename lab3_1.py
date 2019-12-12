def sums():   
  first_sum = 2 + 2
  first_sum = first_sum * 10
  secret = first_sum + 2
  return secret
def string_manip(first_name):
    name = first_name
   all_caps = name.upper()
   all_lowercase = name.lower()
   first_five_letters = name[:5]
   last_two_letters = name[-2:]
   return [all_caps, all_lowercase, first_five_letters, last_two_letters]
def greeter_bot():
   fname = input('what\'s your name?')
   print('Hello, ' + fname+"!")
def temp_calculator():
   c = float(input('what is the temperature?'))
   print(c*(9/5)+32) 
def equitable_bill_splitter():
   people = int(input("How many people are paying? "))
   salaries = []
   total = 0
   for i in range(people):
      sal = int(input("What is the salary of person {}?".format(i+1)))
      total += sal
      salaries.append(sal)
   total_bill = int(input("How much is the bill? "))
   for j in range(len(salaries)):
      print("Person {} should pay ${}\n".format(j + 1, round((total_bill * (salaries[j]/total)), 2)))
