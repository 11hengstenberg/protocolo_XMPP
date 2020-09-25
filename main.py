"""
librerias
"""


import getpass 
import registrar as reg
import funciones as fun

"""
servidor a conectar
"""
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
        print("-----MENU-----")
        print ("0. Exit")
        print ("1. Register")
        print ("2. Login")
        num = int(input())
        print("---------------")
    
    else:
        print("-----MENU-----")
        print ("0. Exit")
        print ("1. Log out")
        print ("2. show accounts")
        print ("3. add users")
        print ("4. user information")
        print ("5. direct message")
        print ("6. change status")
        print ("7. show Grups")
        print ("8. group message")
        num2 = int(input())
        print("---------------")
    

    """
    
    according to the option
    """

    """
    menu 1
    """
    if num == 1:
        print("\n-----REGISTER-----\n")
        name = input ("name:\n")
        username = input ("id:\n")
        password = getpass.getpass("password:\n")
        print("\n----------------------\n")
        register = reg.EchoBot(username+servidor,password, name)
        print(username+servidor)
            

        if register.connect():
            register.process(block= True)
            num = None
            
    
    if num == 2:

        print("-----LOGIN-----")
        username = input("id:\n")
        password = getpass.getpass("password:\n")
        print("------------------------")

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
            datos = funciones.all_users()
            for i in range(len(datos)):
                print ("------------------------------------")
                print ("Email:",datos[i][0])
                print ("JID:",datos[i][1])
                print ("Username",datos[i][2])
                print ("Name", datos[i][3])
                print ("-------------------------------------")
            num2 = None
        
        if num2 == 3:
            print("-----ADD USER-----")
            add_user = input ("User name\n")
            print("------------------------")
            funciones.add_friend(add_user+servidor)
            print ("new friend\n")
            num2= None
        
        if num2 == 4:
            print("-----DATA USER-----")
            data_user = input ("User name data\n")
            print("------------------------")
            data1 = funciones.user_information(data_user)
            print ("-------info-------")
            print ("Email:",data1[0][0])
            print ("JID:",data1[0][1])
            print ("Username",data1[0][2])
            print ("Name", data1[0][3])
            print ("--------------------")

            num2 = None
        
        if num2 == 5:
            print("-----DIRECT MESSAGE-----")
            data_user = input ("User name:\n")
            message = input ("message:\n")
            print("------------------------")
            funciones.direct_message(data_user+servidor,message)
            num2 = None
        
        if num2 == 6:
            new_estado = ["chat","awat", "xa","dnd"]
            print ("-------Change Status-------")
            print ("1. chat")
            print ("2. away")
            print ("3. xa")
            print ("4. dnd") 
            resultado = int(input ("State:\n"))
            msg = input ("message:\n")
            seleccion = new_estado[resultado-1]
            print (seleccion)
            funciones.state(seleccion,msg)
            num2 = None

        if num2 == 7:
            print ("------show grups------")
            print ("-----------------------")
            funciones.show_Rooms()
            print ("---------------------")

        if num2 == 8:
            print ("-------group message-------")
            



    """
    exit program
    """

    if (num == 0 or num2 ==0):
        if login_flag == True:
            if funciones.connect():
                funciones.log_out()
                login_flag = False
        app_flag = False



            
            

        


