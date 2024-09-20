# Final project: Harbour.Space@UTCC inventory & lending system

# Features
   # user system check
   # Welcome

   # Login --> Have to have an account --> name@harbour.com --> gaining access

   # Auth system

   # Inventory --> Show inventory

   # Lending --> what is lended?, by who?, issue date, return date, range of lending

   # Returning --> what is returned?, by who?, return date.

# Flow
   # User_system_check --> config

   # Welcome --> Login --> have access? yes --> Lending or Returning 
   #                                    no --> Create an account --> Login

   # Lending --> Inventory
   # Returning

# For window and unix users

# Database idea:
    # Dictionary
    # JSON
    # List

# Encryption idea:
    # Hashing
    # 
##################################################################################################

import os

# user system
USER_OS = ""
CLEAR_SCREEN = ""

#global variable
user_name = ''
user_inventory = {}
user_item_amount = {}
user_return_date = {}
is_login = False


# Database mocking
## Inventory
inventory = {
    "1": "Scissors",
    "2": "Pencil",
    "3": "Microphone",
    "4": "Batteries",
}
## amount of the stuff in the inventory
inventory_amount = {
    "1": 5,
    "2": 20,
    "3": 3,
    "4": 15,
}

# accessable users
accessible = ["@harbour", "@utcc"]

def check_user_system():
    global USER_OS
    global CLEAR_SCREEN
    
    # window users
    if os.name == "nt":
        USER_OS = "WINDOW"
        CLEAR_SCREEN = "cls"
    # mac or linux users
    elif os.name == "posix":
        USER_OS = "UNIX"
        CLEAR_SCREEN = "clear"

def welcome():
    global user_name
    global is_login
    os.system(CLEAR_SCREEN)

    # Before login
    if not is_login:
        print(r"""
                                                            ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
                                                            ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
                                                            ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
                                                            ██║     ██║   ██║██║   ██║██║██║╚██╗██║
                                                            ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
                                                            ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
              
                                        Please login as a harbour or utcc students before lending orr returning items :D
                                        ----------              login with '@harbour' or '@utcc'              ----------
        """)

        user_name = input("Enter your Username: ").lower()

        while ('@harbour' not in user_name) and ('@utcc' not in user_name):
            print("Access denied!\n")
            print("Please using '@harbour' or '@utcc' at the end of your username to login")
            user_name = input("Enter your username again: ")
        is_login = True

        os.system(CLEAR_SCREEN)
        
        print(r"""
                                                        █████╗  ██████╗ ██████╗███████╗███████╗███████╗               
                                                        ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝               
                                                        ███████║██║     ██║     █████╗  ███████╗███████╗               
                                                        ██╔══██║██║     ██║     ██╔══╝  ╚════██║╚════██║               
                                                        ██║  ██║╚██████╗╚██████╗███████╗███████║███████║               
                                                        ╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝               
                                                                                                                    
                                                ██████╗ ██████╗  █████╗ ███╗   ██╗████████╗███████╗██████╗ ██╗
                                                ██╔════╝ ██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██║
                                                ██║  ███╗██████╔╝███████║██╔██╗ ██║   ██║   █████╗  ██║  ██║██║
                                                ██║   ██║██╔══██╗██╔══██║██║╚██╗██║   ██║   ██╔══╝  ██║  ██║╚═╝
                                                ╚██████╔╝██║  ██║██║  ██║██║ ╚████║   ██║   ███████╗██████╔╝██╗
                                                ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═════╝ ╚═╝
                
                                                                ---- Press any key to continue ----
        """)
        input()

    os.system(CLEAR_SCREEN)

    # After login
    print(r"""
                                                    ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
                                                    ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
                                                    ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
                                                    ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
                                                    ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
                                                    ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                    +++++++++++++***                                 %%%%%    
                                                                ++==+============+++**                    %%%%%%%%%%%%%%%%%%%
                                                                +======================+++*#          %%%%%%##########%%%%%%%%%#
                                                            +======----------=========+++*##  %%%%#############***###%@%%%%%%%
                                                            =====-------------------=====+++**%#####%%%@@@@%%#####**###%%%%%%%% 
                                                        ====----------------------======+++*%@@@@@@@@@@@@@#####*###@%%%%%%%  
                                                        ===-----------:-------------=======++*%@     @@@@@####**##%%%%%%%%    
                                                        =---------::::------------------====++#@   @@@@@%###**##%%%%%%%%      
                                                        ==------::::----------------------====+*%@ @@@@%###**##%%%%%%%%        
                                                        =----------------------::::--------===+*%@@@%%###**##%%%%%%%%          
                                                        =----------------:::::::::::::------==+*#%@%###**##%%%%%%%%             
                                                        =-----------:::::::::::::::::::----=+**#####**##%%%%%%%%                
                                                        =-------::::::::::::::::::::::---++**########%%%%%%%%%                  
                                                        #----:::::::::::::::::::::::-=++***##***##%%%%%%%%%                     
                                                    %%##+-::::::::::::::::::::::-=++********###%%%%%%%                         
                                                %%###%@@--:::::::::::::::::-=+++**********###%%%%%                            
                                            %%%###@@@  --:::::::::::::-=+++***********#####%@@@                              
                                            %%%####%@@@    ---:::::-==++++***********########%@@@                               
                                        %%%#*##%@@@@@@   @#==+++++**************######***#%@@@                                
                                        %%%#*###%@@@@@@@@@@@@@#**#************#####**++**#%@@@                                  
                                    %%%%##*#####%%%%%%%%%#####**********######**++++**#%@@@                                    
                                    %%%%##**###############***####%########*++++++**#%@@@                                       
                                %%%%%####***********######%%%%%%%%%%###*****###%@@@@                                          
                                %%%%%%%@##############%%%%%%%%%%%%%%                                                            
                                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                                 
                                #%%%%%%%%%%%%%%%%%%%%%%%%                                                                       
                                %#%%%%%%%%%%#%%%         
                                                                                                
                                                    ██╗  ██╗ █████╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗        
                                                    ██║  ██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██║   ██║██╔══██╗       
                                                    ███████║███████║██████╔╝██████╔╝██║   ██║██║   ██║██████╔╝       
                                                    ██╔══██║██╔══██║██╔══██╗██╔══██╗██║   ██║██║   ██║██╔══██╗       
                                                    ██║  ██║██║  ██║██║  ██║██████╔╝╚██████╔╝╚██████╔╝██║  ██║    ██╗
                                                    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝
                                                                                                                    
                                                    ██╗     ███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗          
                                                    ██║     ██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝          
                                                    ██║     █████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗         
                                                    ██║     ██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║         
                                                    ███████╗███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝         
                                                    ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     
                    
                                                    ----------     Press any key to continue     ----------                                                  
    """)
    input()
    
    action()

def login():
    pass

def create_account():
    pass

def action():
    os.system(CLEAR_SCREEN)

    print(r"""
                                                ██████╗ ██╗   ██╗██████╗ ██████╗  ██████╗ ███████╗███████╗██████╗ 
                                                ██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝╚════██╗
                                                ██████╔╝██║   ██║██████╔╝██████╔╝██║   ██║███████╗█████╗    ▄███╔╝
                                                ██╔═══╝ ██║   ██║██╔══██╗██╔═══╝ ██║   ██║╚════██║██╔══╝    ▀▀══╝ 
                                                ██║     ╚██████╔╝██║  ██║██║     ╚██████╔╝███████║███████╗  ██╗   
                                                ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝╚══════╝  ╚═╝   
                                                                
                                                                What is your purpose here?
                                                                        (L)ending
                                                                        (R)eturning
                                                                        (N)othing just chilling
    """)
    
    choice = input("Select your choice: ").lower()

    while choice not in ['l', 'r', 'n']:
        print("Please choose the appropriate choice: ")
        choice = input().lower()
    
    if choice == 'l':
        lending()
    elif choice == 'r':
        returning()
    else:
        exit()


def lending():
    global user_name

    os.system(CLEAR_SCREEN)
    print(r"""
                                                    ██╗     ███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗ 
                                                    ██║     ██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝ 
                                                    ██║     █████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗
                                                    ██║     ██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║
                                                    ███████╗███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    
                                                    ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
    """)
    
    want_to_lend = True

    while want_to_lend:
        global user_inventory
        global user_item_amount
        global user_return_date

        show_inventory()
        print("What do you want to lend?")
        item_id = input("Enter item id: ")

        while item_id not in inventory:
            print("\nPlease enter an existing item id")
            item_id = input("Enter item id: ")
        
        if item_id not in user_inventory:
            user_inventory.update({item_id: inventory[item_id]}) 
  
        print(f"\nHow many {inventory[item_id]} do you want to lend?")
        while True:
            try:
                amount = int(input("Enter amount: "))
                break
            except ValueError:
                print("\nPlease lending the available amount")

        while amount > inventory_amount[item_id] or amount < 0:
            if amount < 0:
                print("Seriously?? negative number?")
            else:    
                print(f"There are not enough {inventory[item_id]} for you :(")
            print("\nPlease lending the available amount")

            while True:
                try:
                    amount = int(input("Enter amount: "))
                    break
                except ValueError:
                    print("\nPlease lending the available amount")
        inventory_amount[item_id] -= amount

        if item_id in user_inventory:
            user_item_amount[item_id] = 0
        
        user_item_amount.update({item_id: amount}) # "scissors" : 2

        print(f"\nWhen do you want to returning the {inventory[item_id]}?")
        
        while True:
            while True:
                try:
                    days = int(input("Enter number of days you want to lend before returning it: "))
                    break
                except ValueError:
                    print("\nPlease enter a number!")
            if days < 0:
                print("\nDONT'T ENTER NEGATIVE NUMBERS!")
            else:
                break
        user_return_date.update({item_id: days})

        print(r"""
                                                                    Anything else?
                                                                        (Y)es I want more
                                                                        (N)ope
              """)
        choice = input("Enter your choice: ").lower()

        while choice not in ['y', 'n']:
            print("\nPlease enter a valid choice")
            print(r"""
                                                                    Anything else?
                                                                        (Y)es I want more
                                                                        (N)ope
              """)
            choice = input("Enter your choice: ").lower()

        if choice == 'n':
            want_to_lend = False
    os.system(CLEAR_SCREEN)

    # Display status
    print(f"*" * 80)
    print(f"{'|':<18}Confirm lending")
    print(f"{'|':<5}{'User:':<5}{user_name:<15}")
    print(f"{'|':<5}List of lended items")
    print(f"{'|':<5}{'Id'}{'':<2}|{'':<2}{'Item':<15} {'Amount':<10} {'Days till returning'}")

    for ID in user_inventory:
        item = user_inventory[ID]
        amount = user_item_amount[ID]        
        days = user_return_date[ID]

        print(f"{'|':<5}{ID:<2}{'':<2}|{'':<2}{item:<15} {amount:<10} {days}")

    print(f"{'|'}\n{'|':<5}{'Sign:':<5}{'Aademics team ✅':<15}")
    print('*' * 80)

    print(r"""
                                                     ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗███████╗██╗
                                                     ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝██╔════╝██║
                                                        ██║   ███████║███████║██╔██╗ ██║█████╔╝ ███████╗██║
                                                        ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║╚═╝
                                                        ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗███████║██╗
                                                        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝
          
                                                                ---- Press any key to continue ----
    """)
    input()

    action()

def show_inventory():
    print("\nINVENTORY LIST")
    print(f"{'':<2}{'Id'}{'':<2}|{'':<2}{'Item':<15} {'Amount':<10}")
    print("-" *50)

    for ID in inventory:
        item = inventory[ID]
        amount = inventory_amount[ID]
        print(f"{'':<2}{ID:<2}{'':<2}|{'':<2}{item:<15} {amount:<10}")

    print("-" * 50)

def returning():
    os.system(CLEAR_SCREEN)
    print(r"""
                                            ██████╗ ███████╗████████╗██╗   ██╗██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗ 
                                            ██╔══██╗██╔════╝╚══██╔══╝██║   ██║██╔══██╗████╗  ██║██║████╗  ██║██╔════╝ 
                                            ██████╔╝█████╗     ██║   ██║   ██║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
                                            ██╔══██╗██╔══╝     ██║   ██║   ██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║
                                            ██║  ██║███████╗   ██║   ╚██████╔╝██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝
                                            ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 

""")
    print("What do you want to return?")
    show_user_inventory()
    print("What item do you want to return?")
    item_id = input("Enter item id: ")

    while item_id not in user_inventory:
        if item_id in inventory:
            print(f"\nYou DID NOT lend {inventory[item_id]}!")
        else:
            print(f"\nThere is no item with that ID!")
        item_id = input("Enter item id: ")

    print(r"""
                                Confirm?
                                    (C)onfirm
                                    (N)ah
    """)
    choice = input("Enter your choice: ").lower()

    while choice not in ['c', 'n']:
        print("\nPlease enter an existing choice")
        choice = input("Enter your choice: ").lower()

    if choice == 'c':
        os.system(CLEAR_SCREEN)
        print(r"""
                                                     ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗███████╗██╗
                                                     ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝██╔════╝██║
                                                        ██║   ███████║███████║██╔██╗ ██║█████╔╝ ███████╗██║
                                                        ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║╚═╝
                                                        ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗███████║██╗
                                                        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝
                                                         ------    Press any key rro continue    ------
    """)
        inventory_amount[item_id] += user_item_amount[item_id]
        user_inventory.pop(item_id)
        user_item_amount.pop(item_id)
        input()
        action()
    elif choice == 'n':
        print(r"""
                                                                    ██████╗ ██╗   ██╗███████╗
                                                                    ██╔══██╗╚██╗ ██╔╝██╔════╝
                                                                    ██████╔╝ ╚████╔╝ █████╗  
                                                                    ██╔══██╗  ╚██╔╝  ██╔══╝  
                                                                    ██████╔╝   ██║   ███████╗
                                                                    ╚═════╝    ╚═╝   ╚══════╝
              
                                                         ------    Press any key rro continue    ------
    """)
        input()
        action()

def show_user_inventory():
    print("\nYOUR INVENTORY\n")

    print(f"{'':<2}{'Id'}{'':<2}|{'':<2}{'Item':<15} {'Amount':<10}")
    print("-" *50)

    for ID in user_inventory:
        item = user_inventory[ID]
        amount = user_item_amount[ID]

        print(f"{'':<2}{ID:<2}{'':<2}|{'':<2}{item:<15} {amount:<10}")

    print("-" * 50)

def exit():
    os.system(CLEAR_SCREEN)
    print(r"""
                                    //////////////////////////////////////////////////////////////////////////////////
                                    //  ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗  //
                                    //  ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║  //
                                    //     ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║  //
                                    //     ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║  //
                                    //     ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝  //
                                    //     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝   //
                                    //////////////////////////////////////////////////////////////////////////////////
    """)
    
    print("DON'T FORGET TO RETURN THESE STUFF!!!")
    show_user_inventory()


if __name__ == "__main__":
    check_user_system()
    welcome()