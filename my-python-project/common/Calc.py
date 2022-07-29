USD_to_AMD_course = 0
AMD_to_RUB_course = 0
Accounting_tax = 36600 + 25000 + 5000 + 5000
Armenia_tax = 0.05
Russia_tax = 0.06
Income = 0
Bank_transfer_tax = 0.01


def calculate_salary(USD_AMD, AMD_RUB, Inc):
    value = Inc - 20  # 20$ it's a SWIFT commissions
    value = value - (Inc * Armenia_tax)  # Armenia tax
    Accounting_tax_in_USD = Accounting_tax / USD_AMD
    value = value - Accounting_tax_in_USD  # Withdraw accounting tax in USD
    value = value * USD_AMD / AMD_RUB  # converting to rubles
    value = value - value * Bank_transfer_tax
    value = round(value - (Inc * USD_AMD / AMD_RUB * Russia_tax),2)
    print("\nYou paying for:\nSwift transfer\nArmenian tax\nAccounting\nBank commissions to Russian credit "
          "card\nRussian tax")
    input(f"\nAnd in the end, you will get {value} rubles\n\nNow you can press any key and go to cry")


USD_to_AMD_course = int(input("Input a USD to AMD course in drams\n"))
AMD_to_RUB_course = float(input("Input a AMD to RUB course in drams\n"))
Income = int(input("Input your income in USD\n"))

calculate_salary(USD_to_AMD_course, AMD_to_RUB_course, Income)
