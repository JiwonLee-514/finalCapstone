import math

user_input = input("Please choose one (investment / bond) : ")

if user_input.lower() == "investment" :
  
  print("Start to calculate the amount of interest you'll earn on your investment")
  
  deposit = int(input("The amount of money that you are depositing : "))
  input_rate = int(input("The interest rate (%) - Only number - : "))
  years = int(input("The number of years you plan on investing : "))
  
  rate = input_rate / 100
  
  interest = input("What do you want? 'simple' or 'compound' : ")

  if interest.lower() == "simple" :
    total_amount = round(deposit * (1 + rate * years))   
    # f'{total_amount:.2f}'  ->  print ".00"
    print("Total amount is : ", total_amount)

  elif interest.lower() == "compound" :
    total_amount = round(deposit * math.pow((1+rate),years))   
    print("Total amount is : ", total_amount)
  
  else :
    print("Sorry, You didn't enter one of menu")


elif user_input.lower() == "bond" :
  print("Start to calculate the amount you'll have to pay on a home loan")
  
  house_value = int(input("The present value of the house. (e.g.100000) : "))
  input_rate = int(input("The interest rate (%) - Only number - : "))
  months = int(input("The number of months you plan to take to repay the bond : ")) 

  rate = (input_rate / 100) / 12

  repayment = round((rate * house_value) / (1 - (1 + rate)**(-months)))

  print("Repayment amount is : ", repayment)

else :
  print("Please make sure you enter 'investment' or 'bond' ")
