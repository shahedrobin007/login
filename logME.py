from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           print('\033[1;36;40m<───----------------[ WELCIOME TO CSB WORLD]───────────────>')
           print('')
           print(" \033[1;92m  <───────[ CYBER SECQURITY BROKER ]───────>")
           print("\033[1;93m")
           print("  <───────[ Welcome To THE DARK WORLD  ]───────>")
           print("")
           try:
                x = str(input('\033[1;92mUsername \033[1;93m: '))
                print("")
                e = getpass('\033[1;92mPassword \033[1;93m: ')
                print ("")
                if x=="CYBER SECQURITY BROKER" and e=="ACCESS GRANTED":
                   print('wait...')
                   time.sleep(0.5)
                   os.system('clear')
                   print('')
                   os.system('figlet ' + x + ' | lolcat')
                   print('\033[1;92m 01001010101101001010101010111 ')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     PASSWORD INCORRECT")
                      time.sleep(2)
                      print("")
           except Exception:

                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     PASSWORD INCORRECT")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     PASSWORD INCORRECT")
                      time.sleep(0.5)
menu()
