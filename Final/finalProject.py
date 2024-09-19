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

# Database mocking
## Inventory
inventory = {
    1: "Scissors",
    2: "Pencil",
    3: "Microphone",
    4: "Batteries",
}
## amount of the stuff in the inventory
inventory_amount = {
    1: 5,
    2: 20,
    3: 3,
    4: 15,
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
    os.system(CLEAR_SCREEN)
    print(r"""
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
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
                             _   _            _                          
                            | | | | __ _ _ __| |__   ___  _   _ _ __     
                            | |_| |/ _` | '__| '_ \ / _ \| | | | '__|    
                            |  _  | (_| | |  | |_) | (_) | |_| | |     _ 
                            |_| |_|\__,_|_|  |_.__/_\___/ \__,_|_|    (_)
                            | |    ___ _ __   __| (_)_ __   __ _         
                            | |   / _ \ '_ \ / _` | | '_ \ / _` |        
                            | |__|  __/ | | | (_| | | | | | (_| |        
                            |_____\___|_| |_|\__,_|_|_| |_|\__, |        
                                                           |___/                                                                
""")
    
    print(r"""
        What is your purpose here?
                (L)ending items
                (R)eturning items
                (N)othing just chilling around
    """)
    choice = input("Select your choice: ").lower()
    while choice not in ['l', 'r', 'n']:
        print("Please choose the appropriate choice")
        choice = input().lower()
    
    if choice == 'l':
        lending()
    elif choice == 'r':
        returning()
    else:
        exit()

def login():
    pass

def create_account():
    pass

def lending():
    pass

def returning():
    pass

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
    pass
def inventory():
    pass


if __name__ == "__main__":
    check_user_system()
    welcome()
