import mysql.connector as mysqlator
mycon=mysqlator.connect(host="localhost",user="root",passwd="karan123",database="bank")

def open():
    name=input("enter name")
    accountno=int(input("enter account no:"))
    dateob=int(input("enter dob;"))
    phno=int(input("Enter phone:"))
    adress= input("Enter Address : ")
    openbal = int(input("Enter Opening Balance: "))
    data1 = (name,accountno,dateob,phno,adress,openbal)
    data2 = (name,accountno,openbal)
    sql1 = 'insert into account values(%s,%s,%s,%s,%s,%s)'
    sql2 = 'insert into amount values(%s,%s,%s)'
    c = mycon.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    mycon.commit
    print("data entered successfully")
    main()

def deposit_amount():
    amount = int(input("Enter Amount :"))
    accountno=input("Enter Account No: ")
    a = "select balance from amount where acno = %s"
    data = (accountno,)
    c = mycon.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    total = myresult[0] + amount
    sql3 = " update amount set balance = %s where acno = %s"
    d = (total,ac)
    c.execute(sql3,d)
    mycon.commit()
    main()

def withdraw_amount():
    amount = int(input("Enter Amount: "))
    accountno=int( input("Enter Account No: "))
    a = "select balance from amount where acno=%s"
    sql = "update amount set balance = %s where acno = %s"
    data = (accountno,)
    c = mycon.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    total = myresult[0] - ammount
    d = (total,accountno)
    c.execute(sql,d)
    mycon.commit()
    main()

def balance():
    accountno = input("Enter Account No: ")
    a = "select balance from amount where acno = %s"
    data = (accountno,)
    c = mycon.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    print("Balance for Account : ",accountno," is ",myresult[0])
    main()

def dispatchcc():
    accountno = input("Enter Account No: ")
    a = "select from account where acno= %S"
    data = (accountno,)
    c = mycon.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    for i in myresult:
        print(i, end = "")
    main()

def closeaccount():
    account= input("Enter Account No: ")
    sql1="delete from account where acno=%s"
    sql2 = "delete from amount where acno = %s"
    data = (account,)
    c = con.mycursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    mycon.commit()
    main()

def main():
    print("""
1. OPEN NEW ACCOUNT
2. DEPOSIT AMOUNT
3. WITHDRAW AMOUNT
4. BALANCE ENQUIRY
5. DISPLAY CUSTOMER DETAILS
6. CLOSE AN ACCOUNT
""")
    choice = input("Enter Task No: ")
    if (choice == '1'):
        open()
    elif (choice=='2'):
        deposit_Amount()
    elif (choice=='3'):
        withdraw_ammount()
    elif (choice=='4'):
        balance()
    elif (choice=='5'):
        dispactcc()
    elif (choice == '6'):
        closeaccount()
    else:
        print(" Wrong choice..........")
        main()
main()
