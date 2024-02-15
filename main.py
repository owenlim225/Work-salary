year = int(input("Enter years of work: "))
collar = input("Enter kind of work: ").upper()
salary = ''

if collar == 'B':
    if year <= 2:
        salary = '10,000'
    elif year <= 5:
        salary = '12,000'
    else:
        salary = '15,000'

elif collar == 'W':
    if year <= 2:
        salary = '20,000'
    elif year <= 5:
        salary = '40,000'
    else:
        salary = '75,000'
else:
    print("invalid character.")
    
    

print("Salary:", salary)
