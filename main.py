# Let’s take the original income tax pseudocode from the Case study.  We are going to calculate the income tax of a single person based on their gross income and if they have any dependents:

# Input the gross income and number of dependents
grossIncomeString = input("What is the person's gross income? ")
dependentsString = input ("How many dependents do they have? ")

grossIncome = int(grossIncomeString)
dependents = int(dependentsString)

# Compute the taxable income using the formula:
# Taxable income = gross income - 10000 - (3000 * number of dependents)
taxableIncome = grossIncome - 10000 - (3000 * dependents)

# Compute the income tax using the formula:
# Tax = taxable income * 0.20
tax = taxableIncome * 0.20

# (my input to the pseudocode) Round the tax to the highest non float number and print the result
totalTaxableIncome = round(tax)
print("This person has an income tax of $" + str(totalTaxableIncome) + ".")

# Lambert, Kenneth A. (2018-01-01). Fundamentals of Python: First Programs (Page 39). Cengage Learning. Kindle Edition.