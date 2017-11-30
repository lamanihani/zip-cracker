######################################## zip/rar password cracker ######################################
#################### BY : Lamani Hani                  ( VEGETA-LFH )  #################################
#################              CONTACT : fb : www.facebook.com/lamanihani              #################
#########################          github : www.github.com/lamanihani       ############################
#################### TNX TO : my GOD and prophet MOHAMED & Mom :v , mr.robot ;) ########################
import os 
import sys
import time
os.system('clear')
print('''\033[1;31m \033[97m
         ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗   .Zip
  .RAR  ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗_/
     \__██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
        ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗   
        ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                  \033[90mby \033[96mH\033[95ma\033[94mn\033[93mi \033[92mL\033[91ma\033[96mm\033[93ma\033[95mn\033[94mi \033[91mV\033[92mE\033[93mG\033[94mE\033[95mT\033[96mA\033[97m-\033[93ml\033[95mF\033[91mH\033[97m
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(9. / 100)
print(" ")
hani=input("\033[94m[?]\033[97m drag the \033[91mtarget file \033[97m:")
slowprint("\033[94m[!]\033[92m Searching\033[97m:")
os.system('zip2john ' +(hani)+' > test.hash')
os.system('john test.hash')
os.system('clear')
os.system('clear')
os.system('clear')
os.system('clear')
print('''
         ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
   .RAR ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗  .Zip
      \_██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝_/
        ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
        ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                  \033[90mby \033[96mH\033[95ma\033[94mn\033[93mi \033[92mL\033[91ma\033[96mm\033[93ma\033[95mn\033[94mi \033[91mV\033[92mE\033[93mG\033[94mE\033[95mT\033[96mA\033[97m-\033[93ml\033[95mF\033[91mH\033[97m
''')
print(" ")
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(9. / 100)
        
slowprint('\033[94m[!] \033[91mPassword \033[92mfound \033[97m:')
print(" ")
os.system('john --show test.hash')
print(" ")
os.remove('test.hash')

