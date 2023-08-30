

#-----------------------------------------------------
from Accounts import Account
from Customer import Customer

custList = []


dat01 = Customer(Account("Savings"), "Kylie", "Mackay") 
dat02 = Customer(Account("Cheque"), "Donna", "Underwood")
dat03 = Customer(Account("Business"), "Anthony", "Hudson")

custList.extend([dat01, dat02, dat03])




for x in custList:
    print(x)
