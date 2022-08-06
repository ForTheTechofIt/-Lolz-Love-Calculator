
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower() #Convert to lowercase
name2 = name2.lower() #Convert to lowercase


total1 = 0 #Start counters at 0             
total2 = 0 

combined_string = name1+name2
lower_string = combined_string.lower()

t = combined_string.count('t')
r = combined_string.count('r')
u = combined_string.count('u')
e = combined_string.count('e')

true = t + r + u + e

l = combined_string.count('l')
o = combined_string.count('o')
v = combined_string.count('v')
e = combined_string.count('e')

love = l + o + v + e

total_scoreint = int(str(true)+str(love))


if total_scoreint < 10 or total_scoreint > 90:
    print(f'Your score is {total_scoreint}, you go together like coke and mentos.')
elif total_scoreint >= 40 and total_scoreint <= 50:
    print(f'Your score is {total_scoreint}, you are alright together.')
else:
    print(f'Your score is {total_scoreint}')
#