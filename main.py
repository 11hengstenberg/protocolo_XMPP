"""
librerias
"""

from terminal_text_color import AlertTextColor
import getpass 
from tabulate import tabulate
import registrar as reg
import funciones as fun

"""
servidor a conectar
"""
atc =   AlertTextColor()
servidor = "@redes2020.xyz"

num = None
num2 = None
app_flag = True
login_flag = False

while app_flag == True:

    """
    initial menu
    """

    if login_flag == False:
        atc.success("-----MENU-----")
        print ("0. Exit")
        print ("1. Register")
        print ("2. Login")
        num = int(input())
        atc.success("---------------")
    
    else:
        atc.warning("-----MENU-----")
        print ("0. Exit")
        print ("1. Log out")
        print ("2. show accounts")
        print ("3. add users")
        print ("4. user information")
        print ("5. direct message")
        num2 = int(input())
        atc.warning("---------------")
    

    """
    
    according to the option
    """

    """
    menu 1
    """
    if num == 1:
        atc.info("\n-----REGISTER-----\n")
        name = input ("name:\n")
        username = input ("id:\n")
        password = getpass.getpass("password:\n")
        atc.info("\n----------------------\n")
        register = reg.EchoBot(username+servidor,password, name)
        print(username+servidor)
            

        if register.connect():
            register.process(block= True)
            num = None
            
    
    if num == 2:

        atc.info("-----LOGIN-----")
        username = input("id:\n")
        password = getpass.getpass("password:\n")
        atc.info("------------------------")

        funciones = fun.Funciones(username+servidor,password, username)
        if (funciones.connect()):
            funciones.process()
            print ("se ha logueado")
            login_flag = True
            num = None 

    



    """
    menu 2
    """
    if login_flag == True:
        if num2 == 1:
            if funciones.connect():
                funciones.log_out()
            
            login_flag = False
            num2 = None
        
        if num2 == 2:
            data = tabulate(funciones.all_users(), headers=[ "JID", "Username","Name"], tablefmt="fancy_grid") 
            print (data)
            num2 = None
        
        if num2 == 3:
            atc.info("-----ADD USER-----")
            add_user = input ("User name\n")
            atc.info("------------------------")
            funciones.add_friend(add_user+servidor)
            print ("new friend\n")
            num2= None
        
        if num2 == 4:
            atc.info("-----DATA USER-----")
            data_user = input ("User name data\n")
            atc.info("------------------------")
            data = tabulate(funciones.user_information(data_user), headers=[ "Email","JID", "Username", "Name"], tablefmt="grid")
            print(data)
            num2 = None
        
        if num2 == 5:
            atc.info("-----DIRECT MESSAGE-----")
            data_user = input ("User name:\n")
            message = input ("message:\n")
            atc.info("------------------------")
            funciones.direct_message(data_user+servidor,message)
            num2 = None

            


            

        





    """
    exit program
    """

    if (num == 0 or num2 ==0):
        if login_flag == True:
            if funciones.connect():
                funciones.log_out()
                login_flag = False
        app_flag = False



            
            

        


