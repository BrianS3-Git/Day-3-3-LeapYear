# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
  #print("Year is evenly divisible by 4")
  if year % 100 == 0:
    #print("Year is divisible by 100")
    if year % 400 == 0:
      print(f"The year {year} is a leap year")
    else:
        print(f"The year {year} is NOT a leap year")
  else:
    print(f"The year {year} is a leap year")
else:
  print(f"The year {year} is NOT a leap year")


