#To highlight errors in red fontcolour...........
import sys
print("\n                                                            ATM MACHINE MANAGEMENT ")

#module mysql.connector is for linking python with MYSQL........
import mysql.connector as mycon

#To setup connectivity between python and MYSQL...........
main = mycon.connect(host="localhost", user="root", password="12harshking")
cursor = main.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS atm")
cursor.execute("use atm")


#checking whether the table exist or not if yes then data will inserted into the table............
def check_table_exists(mycon,tablename):
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    if (tablename,) not in tables:
       cursor.execute('''CREATE TABLE IF NOT EXISTS atm
       (ACCOUNT_NO bigint PRIMARY KEY,PIN INT,AMOUNT bigint)''')
       cursor.execute('''INSERT INTO atm
       (ACCOUNT_NO,PIN,AMOUNT)VALUES(123456,1234,500000),(654321,5678,800000)''')
       main.commit()  
cursor.execute("use atm")
tablename = "atm"
check_table_exists(mycon,tablename)



#To display menu............
def display_menu():
    print("\n1. Check Balance ✅")
    print("2. Withdraw 🤑")
    print("3. Deposit 💵:")
    print("4. Exit 👋")

#To check balance in the account.......
def check_balance(accountnumber):
    cursor.execute("select AMOUNT from atm where account_no = %s", (accountnumber,))
    balance = cursor.fetchone()
    bal=balance[0]
    return bal

#To withdraw the ammount from account...........
def withdraw(ac, amount):
    current_balance = check_balance(ac)
    if current_balance >= amount:
        new_balance = current_balance - amount
        cursor.execute("update atm set amount=%s where account_no =%s;",(new_balance,ac))
        main.commit()
        return new_balance

#To diposit amount in the account.........
def deposit(ac, amount):
    current_balance = check_balance(ac)
    new_balance = current_balance + amount
    cursor.execute("update atm set amount=%s where account_no =%s",(new_balance,ac))
    main.commit()

#Main code to execute our atm.........
def maincode():
    ac = int(input("\nEnter Your Account Number : "))
    pin = int(input("Enter Your PIN : "))
    cursor.execute("select * from atm where account_no = %s and pin = %s", (ac, pin))
    account = cursor.fetchone()
    if account:
        print("_____________________")
        print("\n  Welcome To Our ATM")
        print("_____________________")
        for x in range(0,3):
            display_menu()
            choice = int(input("\nEnter your choice : "))
            if choice == int(1):
                print("Your Account Balance Is :",check_balance(ac))
            elif choice == int(2):
                paisa = int(input("\nEnter The Withdrawal Amount : "))
                success = withdraw(ac, paisa)
                if success:
                    print("\nWithdrawal Successful. Your New Balance :",check_balance(ac))
                else:
                    sys.stderr.write("\nInsufficient Balance.........!!!")
            elif choice == int(3):
                paisa=int(input("\nEnter The Amount You Want To Deposit :"))
                diposit=deposit(ac,paisa)
                print("\nDeposited Successfully. Your New Balance :",check_balance(ac))
            elif choice == int(4):
                quit()
            else:
                sys.stderr.write("\nInvalid Choice.........?")
    else:
        sys.stderr.write("\nInvalid account number or PIN. Please try again")

        

#To run maincode again and again.....
while True:
    maincode()






