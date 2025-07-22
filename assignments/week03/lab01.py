# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
age = int(input("enter age: "))
if age >0 and age <= 12:
    print("your child")
elif 13 <= age <= 19:
    print("your tennager")
elif 20 <= age <= 59:
    print("your adult")
else:
    print("your senior")