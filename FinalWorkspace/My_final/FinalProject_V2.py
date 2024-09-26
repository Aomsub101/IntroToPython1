# Final project: Harbour.Space@UTCC inventory & lending system

# Features
   # user system check
   # Welcome

   # Login --> Have to have an account --> name@harbour or name@utcc--> gaining access

   # Auth system

   # Inventory --> Show inventory

   # Lending --> what is lended?, by who?, issue date, return date, range of lending

   # Returning --> what is returned?, by who?, return date.

   # Add item --> what item?, For how many?
# Flow
   # User_system_check --> config

   # Welcome --> Login --> have access? yes --> Lending or Returning 
   #                                    no --> Create an account --> Login

   # Lending --> Inventory
   # Returning
   # Add item
# For window and unix users

# Database idea:
    # Dictionary
    # JSON ✅
    # List

# Encryption idea:
    # Hashing
    # 
##################################################################################################

import os
import json
import getpass as g

#global variable
user_name = ''
is_login = False
user_id = None

# Change directory
current_path = os.getcwd()
new_path = os.path.join(current_path, 'FinalWorkspace', 'My_final')
os.chdir(new_path)    

# get inventory
with open('inventory.json', 'r') as inventory_file:
    inventory = json.load(inventory_file)

# get user data
with open('user.json', 'r') as user_file:
    user = json.load(user_file)


# user system
USER_OS = ""
CLEAR_SCREEN = ""

# accessable users
accessible = ["@harbour", "@utcc"]


def check_user_system() -> None:
    """
    ## args -> None
    
    ## return -> None
    
    This function will get a user operating system
    and define what command will be use for clearing
    a screen 
    """
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


def welcome() -> None:
    """
    ### args -> None

    ### return -> None

    This function will display a login page
    and let user decide whether to login or creating a new account

    After user granted access they will go to a welcome page
    and continue to the "action()" function.
    """
    os.system(CLEAR_SCREEN)

    # Before login
    while not is_login:
        print(r"""
                                                            ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
                                                            ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
                                                            ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
                                                            ██║     ██║   ██║██║   ██║██║██║╚██╗██║
                                                            ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
                                                            ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
              
                                        Please login as a harbour or utcc students before lending or returning items :D
                                        ----------              login with '@harbour' or '@utcc'              ----------

                                                                 (L)ogin with existing account
                                                                 (C)reate a new account
        """)
        choice = input("Enter your choice: ").lower().strip()

        while choice not in ['l', 'c']:
            print("\nInvalid choice!")
            choice = input("Enter your choice again: ").lower().strip()
        
        if choice == 'l':
            login()
            os.system(CLEAR_SCREEN)
        else:
            create_account()

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
            
                                                            ---- Press Enter to continue ----
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
                    
                                                        ----------     Press Enter to continue     ----------                                                  
    """)
    input()
    
    action()


def login() -> None:
    """
    ## args -> None
    
    ## return -> None
    
    This function will let you enter your username and password
    
    # Username

    It will first check if your username exists or not
    if exist: enter password
    if not exist: Create a new useraccount or retry

    # Password

    You have only 3 tries to enter a password or if you forget a password
    you can press (F) and enter to reveal the password

    if the password is correct, you will get access to lending system
    if the password is wrong, you have 2 choices. Forget password or re-enter
    the password till you run out of retry quoto
    """ 

    global is_login
    global user_name
    global user_id

    def get_user_id(user_name: str) -> int:
        """
        ## args -> user_name as string

        ## return -> integer
        
        This sub-function will get a user_name as a argument
        and will return a user_id of this user_name
        """
        for usr in user['users']:
            if usr['user_name'] == user_name:
                return usr['id'] - 1


    user_name = input("\nPlease enter your user name: ").lower().strip()

    while not (any(each_user['user_name'] == user_name\
                   for each_user in user['users'])):
        print(f"There is no {user_name} account registered.")
        print("\nDo you want to create a new account? (Y)es (N)o (R)etry")
        choice = input("Enter your choice: ").lower().strip()
        
        while choice not in ['y', 'n', 'r']:
            print("Invalid choice!")
            choice = input("\nEnter a valid choice: ")

        if choice == 'y':
            create_account()
            os.system(CLEAR_SCREEN)
            return None
        elif choice == 'r':
            user_name = input("\nEnter your user name again: ")
        else:
            return None
    
    user_id = get_user_id(user_name)

    password_check = user['users'][user_id]['password']
    password = g.getpass("Password(It will be invisible) or\
                         press (F) and enter if forget password: ")
    
    if password in ['f', 'F']:
        show_password(user_name, password_check)
        return None

    count = 3
    while password_check != password:
        if count == 1:
            os.system(CLEAR_SCREEN)
            print(r"""       
                                                                You run out of retry quota!
                                                            You will be at Login page again 
                                                         ------   Press Enter to continue   ------     
            """)
            input()
            return None
        
        count -= 1
        if count > 1:
            print(f"\nWRONG!\nYou have {count} tries left")
        else:
            print(f"\nWRONG!\nYou have 1 try left. Don't get it wrong!")
        
        print("\nPress (F) then enter if forget your password")

        password = g.getpass("Please re-enter your password: ")
        if password in ['f', 'F']:
            show_password(user_name, password_check)
            return None
        
    is_login = True


def show_password(user_name: str, password: str) -> None:
    """
    ## args -> user_name as string, password as string

    ## return -> None

    This function will display a user's password
    """
    os.system(CLEAR_SCREEN)
    print(r"""


                                            ███╗   ██╗███████╗██╗  ██╗████████╗    ████████╗██╗███╗   ███╗███████╗
                                            ████╗  ██║██╔════╝╚██╗██╔╝╚══██╔══╝    ╚══██╔══╝██║████╗ ████║██╔════╝
                                            ██╔██╗ ██║█████╗   ╚███╔╝    ██║          ██║   ██║██╔████╔██║█████╗  
                                            ██║╚██╗██║██╔══╝   ██╔██╗    ██║          ██║   ██║██║╚██╔╝██║██╔══╝  
                                            ██║ ╚████║███████╗██╔╝ ██╗   ██║          ██║   ██║██║ ╚═╝ ██║███████╗
                                            ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝   ╚═╝          ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝
                                                                                                                
                                                            ██████╗  ██████╗ ███╗   ██╗████████╗                  
                                                            ██╔══██╗██╔═══██╗████╗  ██║╚══██╔══╝                  
                                                            ██║  ██║██║   ██║██╔██╗ ██║   ██║                     
                                                            ██║  ██║██║   ██║██║╚██╗██║   ██║                     
                                                            ██████╔╝╚██████╔╝██║ ╚████║   ██║                     
                                                            ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝                     
                                                                                                                
                                                    ███████╗ ██████╗ ██████╗  ██████╗ ███████╗████████╗           
                                                    ██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝           
                                                    █████╗  ██║   ██║██████╔╝██║  ███╗█████╗     ██║              
                                                    ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝     ██║              
                                                    ██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗   ██║              
                                                    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝              
   
    """)
    print("*" * 49)
    print(f"The password for account '{user_name}' is: '{password}'")
    print("*" * 10 + "   Press Enter to continue   "+ "*" * 10)
    
    input()


def create_account() -> None:
    """
    ## args -> None
    
    ## return -> None

    This function use for creating a new user account.
    It will get a username that ended with "harbour" or "@utcc" 
    and a password contain at least 5 characters that
    don't contain any spaces
    """
    global user_name
    global user_id

    os.system(CLEAR_SCREEN)
    print(r"""
                                                       ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗        
                                                      ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝        
                                                      ██║     ██████╔╝█████╗  ███████║   ██║   █████╗          
                                                      ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝          
                                                      ╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗        
                                                       ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝        
                                                                                                            
                                                 █████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗
                                                ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝
                                                ███████║██║     ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║   
                                                ██╔══██║██║     ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║   
                                                ██║  ██║╚██████╗╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║   
                                                ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   

                                                 --------   Welcome! please create your account   --------
                                              ** Please ended with '@harbour' or '@utcc' in your user name **
          """)
    
    user_name = input("\nEnter user name with '@harbour' or '@utcc': ")\
                .lower().strip()

    cond1 = user_name[len(user_name)-8: len(user_name)] != "@harbour"
    cond2 = user_name[len(user_name)-5: len(user_name)] != "@utcc"

    while cond1 and cond2:
        print("\nPlease ended with '@harbour' or '@utcc' in your username!")
        user_name = input("Enter your username again: ").lower()
        cond1 = user_name[len(user_name)-8: len(user_name)] != "@harbour"
        cond2 = user_name[len(user_name)-5: len(user_name)] != "@utcc"

    while any(usr['user_name'] == user_name for usr in user['users']):
        print("\nThis account already exists")
        user_name = input("Please think of a new username: ").lower()

    password = g.getpass("\nPlease create a new password\
                         longer than 5 character(it will be invisible): ")

    while len(password) <= 5 or ' ' in password:
        if len(password) <= 5:
            password = g.getpass("\nPassword must contain more than 5\
                                 character(it will be invisible): ")
        elif ' ' in password:
            password = g.getpass("\nPassword must not contain a space\
                                 (it will be invisible): ")

    new_user = {
        "id": len(user['users']) + 1,
        "user_name": user_name,
        "password": password,
        "items":[]
    }

    user['users'].append(new_user)

    with open('user.json', 'w') as user_file:
        json.dump(user, user_file, indent=2)

    os.system(CLEAR_SCREEN)
    print(r"""
                                                         █████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗
                                                        ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝
                                                        ███████║██║     ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║   
                                                        ██╔══██║██║     ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║   
                                                        ██║  ██║╚██████╗╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║   
                                                        ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   
                                                                                                                    
                                                         ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗██████╗ ██╗ 
                                                        ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██║ 
                                                        ██║     ██████╔╝█████╗  ███████║   ██║   █████╗  ██║  ██║██║ 
                                                        ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝  ██║  ██║╚═╝ 
                                                        ╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗██████╔╝██╗ 
                                                         ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝ ╚═╝ 
                                                                
                                                          -----     Press Enter to continue to login page     -----
    """)

    input()
    
    os.system(CLEAR_SCREEN)


def action() -> None:
    """
    ## args -> None

    ## return -> None

    This function will let user decide what they want to do
    (L)ending
    
    (R)eturning
    
    (A)dd lending item
    
    (N)othing just chilling
    """
    exit_ = False
    while not exit_:
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
                                                                            (A)dd lending item
                                                                            (N)othing just chilling
        """)
        
        choice = input("Select your choice: ").lower().strip()

        while choice not in ['l', 'r', 'a', 'n']:
            choice = input("Please choose the appropriate choice: ")\
                    .lower().strip()
        
        if choice == 'l':
            lending()
        elif choice == 'r':
            returning()
        elif choice == 'a':
            add_item()
        else:
            exit_ = True
    exit()


def lending() -> None:
    """
    ## args -> None

    ## return -> None

    This function will first display a table of existing items
    along with its ID.
    
    The user will decide which item they want by entering 
    1. item's id
    
    2. amount

    3. amount of days user want to lend for

    Then will append those items in user's inventory.

    Lastly, display all of the items that user have lended.
    """

    global user_name
    global is_item_exist
    global user_id

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
    is_item_exist = False
    
    while want_to_lend:
        user_items = user['users'][user_id-1]['items']
        user_item_index = len(user['users'][user_id-1]['items'])


        def get_item_index(item_id: int) -> int:
            """
            ## args -> item_id as integer

            ## return -> integer

            This function is use for getting an item's id 
            that user have already lended it and haven't return it yet.
            """
            count = 0
            for item in user_items:
                if item['id'] == item_id:
                    return count
                count += 1
        
        show_inventory()

        print("What do you want to lend?")

        while True:
            try:
                item_id = int(input("Enter item id: "))
                break            
            except ValueError:
                print("\nPlease enter a number!")

        while not any(item['id'] == item_id for item in inventory['items']):
            print("\nPlease enter an existing item id")
            while True:
                try:
                    item_id = int(input("Enter item id: "))
                    break                
                except ValueError:
                    print("\nPlease enter a number!")
        
        if not any(usr_item['id'] == item_id \
                   for usr_item in user['users'][user_id-1]['items']):
            user_items.append({
                "id": inventory['items'][item_id-1]['id'], 
                "name": inventory['items'][item_id-1]['name']
            })
        else:
            is_item_exist = True
            user_item_index = get_item_index(item_id)

        print(f"\nHow many\
              {inventory['items'][item_id-1]['name']}\
                do you want to lend?")

        while True: 
            try:
                amount = int(input("Enter amount: "))
                break
            except ValueError:
                print("\nPlease lending the available amount")

        while amount > inventory['items'][item_id-1]['amount'] or amount <= 0:
            if amount < 0:
                print("Seriously?? negative number?")
            elif amount == 0:
                print("Bro, come on man. Get serious!")
            else:    
                print(f"There are not enough\
                      {inventory['items'][item_id-1]['name']} for you :(")
                
            print("\nPlease lending the available amount")

            while True:
                try:
                    amount = int(input("Enter amount: "))
                    break
                except ValueError:
                    print("\nPlease lending the available amount")

        inventory['items'][item_id-1]['amount'] -= amount

        with open('inventory.json', 'w') as inventory_file:
            json.dump(inventory, inventory_file, indent=2)

        if is_item_exist:
            user_items[user_item_index]['amount'] += amount
        else:
            user_items[user_item_index].update({'amount': amount})

        print(f"\nWhen do you want to return the\
              {inventory['items'][item_id-1]['name']}?")
        
        while True:
            while True:
                try:
                    days = int(
                        input("Enter number of days you \
                              want to lend before returning it: "))
                    break
                except ValueError:
                    print("\nPlease enter a number!")
            if days < 0:
                print("\nDONT'T ENTER NEGATIVE NUMBERS!")
            elif days == 0:
                print("\nMinimum lending is 1 day.")
            else:
                break

        user_items[user_item_index].update({'days': days})

        with open('user.json', 'w') as user_file:
            json.dump(user, user_file, indent=2)

        print(r"""
                                                                    Anything else?
                                                                        (Y)es I want more
                                                                        (N)ope
              """)
        choice = input("Enter your choice: ").lower().strip()

        while choice not in ['y', 'n']:
            print("\nPlease enter a valid choice")
            print(r"""
                                                                    Anything else?
                                                                        (Y)es I want more
                                                                        (N)ope
              """)
            choice = input("Enter your choice: ").lower().strip()
            
        is_item_exist = False

        if choice == 'n':
            want_to_lend = False
         

    os.system(CLEAR_SCREEN)

    # Display status
    print(f"*" * 80)
    print(f"{'|':<18}Confirm lending")
    print(f"{'|':<5}{'User:':<5}{user_name:<15}")
    print(f"{'|':<5}List of lended items")
    print(f"{'|':<5}{'Id'}{'':<2}|{'':<2}{'Item':<15} \
          {'Amount':<10} {'Days till returning'}")

    for item in user_items:
        ID = item['id']
        item_name = item['name']
        amount = item['amount']        
        days = item['days']

        print(f"{'|':<5}{ID:<2}{'':<2}|{'':<2}{item_name:<15} \
              {amount:<10} {days}")

    user['users'][user_id-1].update({"items": user_items})

    with open('user.json', 'w') as user_file:
        json.dump(user, user_file, indent=2)

    print(f"{'|'}\n{'|':<5}{'Sign:':<5}{'Aademics team ✅':<15}")
    print('*' * 80)

    print(r"""
                                                     ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗███████╗██╗
                                                     ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝██╔════╝██║
                                                        ██║   ███████║███████║██╔██╗ ██║█████╔╝ ███████╗██║
                                                        ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║╚═╝
                                                        ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗███████║██╗
                                                        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝
          
                                                                ---- Press Enter to continue ----
    """)

    input()


def show_inventory() -> None:
    """
    ## args -> None
    
    ## return -> None

    This function simply display all of the items in inventory.
    """

    global inventory

    print("\nINVENTORY LIST")
    print(f"{'':<2}{'Id'}{'':<2}|{'':<2}{'Item':<15} {'Amount':<10}")
    print("-" *50)

    for itm in inventory['items']:
        ID = itm['id']
        item_name = itm['name']
        amount = itm['amount']
        print(f"{'':<2}{ID:<2}{'':<2}|{'':<2}{item_name:<15} {amount:<10}")

    print("-" * 50)


def returning() -> None:
    """
    ## args -> None
    
    ## return -> None

    This function use for returning items that have been lended.

    It will let the user decide what they want to return
    by entering an item_id, and confirm returning after.

    Lastly, it will store the returning items back into an inventory.
    """
    os.system(CLEAR_SCREEN)
    print(r"""
                                            ██████╗ ███████╗████████╗██╗   ██╗██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗ 
                                            ██╔══██╗██╔════╝╚══██╔══╝██║   ██║██╔══██╗████╗  ██║██║████╗  ██║██╔════╝ 
                                            ██████╔╝█████╗     ██║   ██║   ██║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
                                            ██╔══██╗██╔══╝     ██║   ██║   ██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║
                                            ██║  ██║███████╗   ██║   ╚██████╔╝██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝
                                            ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 

    """)
    if len(user['users'][user_id-1]['items']) == 0:
        print(r"""
                                                                      You have no lended item!
                                                               -----  Press enter to continue  -----
        """)

        input()
        
        return None

    show_user_inventory()

    print("What item do you want to return?")

    while True:
        try:
            item_id = int(input("Enter item id: "))
            break        
        except ValueError:
            print("\nPlease enter a number!")
    
    while not any(usr_item['id'] == item_id \
                  for usr_item in user['users'][user_id-1]['items']):
        if any(item['id'] == item_id for item in inventory['items']):
            print(f"\nYou DID NOT lend \
                  {inventory['items'][item_id-1]['name']}!")
        else:
            print(f"\nThere is no item with that ID!")
        while True:
            try:
                item_id = int(input("Enter item id: "))
                break            
            except ValueError:
                print("\nPlease enter a number!")

    print(r"""
                                Confirm?
                                    (C)onfirm
                                    (N)ah
    """)

    choice = input("Enter your choice: ").lower().strip()

    while choice not in ['c', 'n']:
        print("\nPlease enter an existing choice")
        choice = input("Enter your choice: ").lower().strip()

    if choice == 'c':
        os.system(CLEAR_SCREEN)
        print(r"""
                                                     ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗███████╗██╗
                                                     ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝██╔════╝██║
                                                        ██║   ███████║███████║██╔██╗ ██║█████╔╝ ███████╗██║
                                                        ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║╚═╝
                                                        ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗███████║██╗
                                                        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝
                                                            ------    Press Enter to continue    ------
        """)
        
        for usr in user['users'][user_id-1]['items']:
            if usr['id'] == item_id:
                inventory['items'][item_id-1]['amount'] += usr['amount']
                user['users'][user_id-1]['items'].remove(usr)
                break

        with open('user.json', 'w') as user_file:
            json.dump(user, user_file, indent=2)

        with open('inventory.json', 'w') as inventory_file:
            json.dump(inventory, inventory_file, indent=2)

        input() 
    elif choice == 'n':
        print(r"""
                                                                    ██████╗ ██╗   ██╗███████╗
                                                                    ██╔══██╗╚██╗ ██╔╝██╔════╝
                                                                    ██████╔╝ ╚████╔╝ █████╗  
                                                                    ██╔══██╗  ╚██╔╝  ██╔══╝  
                                                                    ██████╔╝   ██║   ███████╗
                                                                    ╚═════╝    ╚═╝   ╚══════╝
              
                                                           ------    Press Enter to continue    ------
    """)
        input()


def add_item() -> None:
    """
    ## args -> None

    ## return -> None

    This function is for adding a new item to inventory.

    It will accept the 
    1.item's name

    2.amount of that item

    Then it will automatically add the new item to the inventory
    along with item's id.
    """
    os.system(CLEAR_SCREEN)

    print(r"""
                                                     █████╗ ██████╗ ██████╗     ██╗████████╗███████╗███╗   ███╗
                                                    ██╔══██╗██╔══██╗██╔══██╗    ██║╚══██╔══╝██╔════╝████╗ ████║
                                                    ███████║██║  ██║██║  ██║    ██║   ██║   █████╗  ██╔████╔██║
                                                    ██╔══██║██║  ██║██║  ██║    ██║   ██║   ██╔══╝  ██║╚██╔╝██║
                                                    ██║  ██║██████╔╝██████╔╝    ██║   ██║   ███████╗██║ ╚═╝ ██║
                                                    ╚═╝  ╚═╝╚═════╝ ╚═════╝     ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝
                                                           
                                                           ------    Welcome to add item page!    ------
    """)

    new_item = {}
    print("What item do you want to add?")
    item_name = input("Enter item name: ")
    
    while len(item_name.strip()) == 0:
        print("\nA single character is fine.")
        item_name = input("Enter item name: ")

    print("\nHow many?: ")

    while True:
        try:
            amount = int(input("Enter amount: "))
            break
        except ValueError:
            print("\nPlease enter a number!")

    while amount <= 0:
        if amount < 0:
            print("HUH?!")
        elif amount == 0:
            print("Bro seriously?!")
        
        while True:
            try:
                amount = int(input("Enter the amount: "))
                break
            except ValueError:
                print("\nPlease enter a number, sMaRT gUy~")
        
    new_item.update({"id": len(inventory['items'])+1})
    new_item.update({"name": item_name})
    new_item.update({"amount": amount})

    inventory['items'].append(new_item)

    with open('inventory.json', 'w') as inventory_file:
        json.dump(inventory, inventory_file, indent=2)

    print(r"""
                                                                    ██╗████████╗███████╗███╗   ███╗     
                                                                    ██║╚══██╔══╝██╔════╝████╗ ████║     
                                                                    ██║   ██║   █████╗  ██╔████╔██║     
                                                                    ██║   ██║   ██╔══╝  ██║╚██╔╝██║     
                                                                    ██║   ██║   ███████╗██║ ╚═╝ ██║     
                                                                    ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝     
                                                                                                        
                                                                 █████╗ ██████╗ ██████╗ ███████╗██████╗ 
                                                                ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
                                                                ███████║██║  ██║██║  ██║█████╗  ██║  ██║
                                                                ██╔══██║██║  ██║██║  ██║██╔══╝  ██║  ██║
                                                                ██║  ██║██████╔╝██████╔╝███████╗██████╔╝
                                                                ╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═════╝ 

                                                             -------    Press Enter to continue    -------
    """)
    input()


def show_user_inventory() -> None:
    """
    ## args -> None

    ## return -> None

    This function will simply display a table of 
    what item(s) user have lended.
    """

    print("\nYOUR INVENTORY\n")
    
    print(f"{'':<2}{'Id'}{'':<2}|{'':<2}{'Item':<15} {'Amount':<10}")
    print("-" *50)

    for usr_item in user['users'][user_id-1]['items']:
        ID = usr_item['id']
        item_name = usr_item['name']
        amount = usr_item['amount']

        print(f"{'':<2}{ID:<2}{'':<2}|{'':<2}{item_name:<15} {amount:<10}")

    print("-" * 50)


def exit() -> None:
    """
    ## args -> None

    ## return -> None

    This function is the ending function and display a thank you sign.

    Use when user don't want to do anything.
    """

    os.system(CLEAR_SCREEN)

    if len(user['users'][user_id-1]['items']):
        print("DON'T FORGET TO RETURN THESE STUFF!!!")
        show_user_inventory()
        
        print(r"""
                                        //////////////////////////////////////////////////////////////////////////////////
                                        //  ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗  //
                                        //  ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║  //
                                        //     ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║  //
                                        //     ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║  //
                                        //     ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝  //
                                        //     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝   //
                                        //////////////////////////     Press Enter to exit     ///////////////////////////
        """)

        input()
    else:
        print(r"""
                                        //////////////////////////////////////////////////////////////////////////////////
                                        //  ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗  //
                                        //  ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║  //
                                        //     ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║  //
                                        //     ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║  //
                                        //     ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝  //
                                        //     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝   //
                                        //////////////////////////     Press Enter to exit     ///////////////////////////
        """)
        input()


if __name__ == "__main__":
    check_user_system()
    welcome()