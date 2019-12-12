def is_even():
  
   user_data = int(input("Please give me an integer. "))
   out = None
   if user_data % 2 == 0: 
      out = True
   else:
      out = False
   return out 

def multi_condition():
   user_data = int(input("Please give me an integer. "))
   if user_data == 0:
      print('Don\'t be such a zero!')
   elif user_data > 0 and user_data % 2 != 0:
      print('Positively odd!')   
   elif user_data > 0 and user_data % 2 == 0:
      print('Even Steven!')
   elif user_data < 0:
      print('Negative Nelly!') 

   return None


def is_underage():
   if age >= 21:
      print("You may drink, smoke, and drive if you wish!")
   elif 18 <= age < 21:
      print("You may smoke and drive!")
   elif 16 <= age < 18:
      print("You may drive!")
   elif age < 16:
      print("Enjoy your bike, kid!")
   return None

def countdown():
   n = 10
   while n >= 0:
      print(n)
      n = n - 1
    
   return None

def guessing_game(num):
   count = 0
   while count < 10:
      guess = input('Guess a number')
      if guess == 'q':
         print("Goodbye, quitter!")
         count = 11
      else:
         guess = int(guess)
         count += 1
         if guess == num:
            print("You win!")
            count = 11
         elif guess < num:
            print("Too Low!") 
         else:
            print("Too High!")     
   if count == 10:
      print("You Lose!") 
   return None
