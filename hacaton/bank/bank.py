welcome = input(" Welcome to our bank system do you want to login or register? : ")

# register system 

if welcome == "register":
    name = input("Enter your name :")
    email = input("Enter your email :")
    ID = input("Enter your ID :")
    phone = input("Enter your Phone number :")
    if len(phone) != 9:
        print("incorrect number !!! enter again :") 
        input("enter num again : ")
    CVC = input("Enter your CVC :")
    if len(CVC) != 3:
        print("incorrect CVC !!! ") 
        input("enter CVC again : ")
    password = input("Enter your new password:")
    if len(password) < 10:
        print("min 10 charecters") 
    confirm = input("Confirm your password :")
    if confirm != password:
        print("you entered wrong password!!")
        input("enter password again : ")
    print("###############################################################")
    print("You successfully registered !!! Welcome to Goa Bank <3 <3")
    print("                                                                 ")
    



# login page 
if welcome == "login":
    name1 = input("Enter your name :")
    email1 = input("Enter email : ")
    password1 = input("Enter your password______forgot? Y/N : ")
    if password1 == "Y":
        resetemail = input("enter your email :")
        resetcode = input("enter your one time code : ")
        newpassword = input("enter your new password : ")
        confirmpassword = input("confirm new password : ") 
        if confirmpassword != newpassword:
            print("wrong password")
        else:
            print("your password updated!!")
    print("##################################################")
    print("Welcome to Goa Bank <3 <3")


#deposit 
    
deposit = int(input("How much ₾ you want to deposit? : "))
if deposit == 0:
    print("you can't deposit 0 ₾")
    input("how much ₾ you want to deposit ? : ")
print("Now on bank you have " + str(deposit) + " ₾")
print("                                                 ")
print("#################################################")




 #deposit withdraw or tranfer
question1 = input("Do you want to deposit again, withdraw ,  transfer ?")
if question1 == "deposit":
    new_deposit = int(input("how much do you want to deposit again?:"))
    deposit=deposit+new_deposit
print(("Now on bank you have " + str(deposit) + " ₾"))
print("                                                               ")
print("###############################################################")
    
    
# withdraw
if question1 == "withdraw":
    withdraw = int(input("How much do you want to withdraw? : "))
    if withdraw > deposit:
        print("You don't have enough money! ")
        again = int(input("How much do you want to withdraw? : "))
    print("Now you have " + str(deposit - withdraw) + " ₾")

print("                                                             ")
print("#############################################################")
    




# #transfer
if question1 == "transfer":
    transfer = input("do you want to transfer? (yes or no): ")
    if transfer == "yes":
        user_name = input("who you transfer to ? : ")
        user_email = input("number of the person :")
        transfer_to = int(input("how much he have? : "))
        user_ID = input("ID of the person : ")
        transfer_user = int(input("how much you want to transfer?"))
        if transfer_user>deposit:
            print("not enought money")
            transfer_user=int(input("how much you want to transfer?"))
        print("transfer successfully  ")
        print("now you have " + str(deposit - transfer_user) + " ₾")
        print("now second acc have  " + str(transfer_to + transfer_user) + " ₾")





    #logout

print("#################################################")
print("                                                 ")

log_out = input("Do you want to log out?")
if log_out == "yes":
    print("Congratulation! you sucessfully logged out.")
elif log_out == "no":
    print("Great! thank you for being here!")
