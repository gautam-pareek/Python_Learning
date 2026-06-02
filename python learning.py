name = input("What is your name?  :")
age = int(input("What is your age?  :"))
current_year = int(input ("What is the current year?  :"))
future_year = int(input("What year do yuou want to know your age in?  :"))
salary=500000
is_employed=True
city="Pune"

#  print(f"My name is {name} and I am {age}. I am earning {salary} every month.")
print(f"{name} will be {age + future_year-current_year} years old in {future_year}.")

