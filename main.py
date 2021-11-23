# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
  print("Year is evenly divisible by 4 - check")
  if year % 100 == 0:
    print("Year is also divisible by 100 - check")
    if year % 400 == 0:
      print("Year is also divisible by 400 - check")
      print(f"The year {year} is a leap year")
    else:
        print("BUT year is not divisible by 400, so...")
        print(f"The year {year} is NOT a leap year")
  else:
    print(f"The year {year} is a leap year")
else:
  print(f"The year {year} is NOT a leap year")


