credentials_accepted = False
credentials = []
credentials_san = []
bypass = False
counter1 = 0

import sys
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

File = open(r"\\fsacad02.academic.bmet.ad\StudentHome\Students\23002024\My Documents\The Shelf\PYTHON\Terminal\check.txt", "r")
login_info_entered = File.read()
File.close()
print(bcolors.OKBLUE + login_info_entered + bcolors.ENDC)

if login_info_entered != "True":
    print(bcolors.WARNING + "No credentials found" + bcolors.ENDC)
    File = open(r"\\fsacad02.academic.bmet.ad\StudentHome\Students\23002024\My Documents\The Shelf\PYTHON\Terminal\pass.txt", "w")
    login_psw = str(input("create a password"))
    login_usr = str(input("create a Username"))
    login_name = str(input("create a password"))
    File.writelines([login_psw, "\n", login_usr, "\n", login_name])
    File.close()
    File = open(r"\\fsacad02.academic.bmet.ad\StudentHome\Students\23002024\My Documents\The Shelf\PYTHON\Terminal\check.txt", "w")
    File.write("True")
    File.close()
    bypass = True

File = open(r"\\fsacad02.academic.bmet.ad\StudentHome\Students\23002024\My Documents\The Shelf\PYTHON\Terminal\pass.txt", "r")
credentials.extend(File.readlines())
for x in credentials:
    credentials_san.append(x.replace("\n", ""))

counter1 = 0
while credentials_accepted == False:
    user_input_username = str(input("Please enter your username"))
    user_input_password = str(input("Please enter your password"))
    if user_input_password == credentials_san[1] and user_input_username == credentials_san[0]:
        print(bcolors.OKGREEN + "Password and Username accepted" + bcolors.ENDC)
        credentials_accepted = True
    else:
        print(bcolors.FAIL + "Incorrect password" + bcolors.ENDC)
        counter1 = counter1 + 1
        print(bcolors.FAIL + "Fail" + bcolors.ENDC, bcolors.WARNING + str(counter1) + bcolors.ENDC, "/",bcolors.WARNING + "3" + bcolors.ENDC )
    if counter1 >= 3:
        File = open(r"\\fsacad02.academic.bmet.ad\StudentHome\Students\23002024\My Documents\The Shelf\PYTHON\Terminal\pass.txt", "w")
        File.write("")
        File.close
        print(bcolors.WARNING + "#" + bcolors.ENDC, bcolors.FAIL + "LOGIN CREDENTIALS PURGED" + bcolors.ENDC, bcolors.WARNING + "#" + bcolors.ENDC)
        File = open(r"\\fsacad02.academic.bmet.ad\StudentHome\Students\23002024\My Documents\The Shelf\PYTHON\Terminal\check.txt", "w")
        File.write("False")
        File.close()    
        sys.exit()
class programs:
    @staticmethod
    def ip_check():
        ip_file = open(r"\\fsacad02.academic.bmet.ad\StudentHome\Students\23002024\My Documents\The Shelf\PYTHON\IP_checker\ip_list.txt", "r")
        ip_file_RAW = []
        ip_file_RAW.extend(ip_file.readlines())
        ip_file_SANITISED = []
        byteadress = []
        bytearr = []
        invalid_ip = []
        temp2 = []
        counter9 = 0
        temp = ip_file_SANITISED
        byteadress.extend(("First byte", "Second byte", "Third byte", "Forth byte"))
        good_pass = True

        class bcolors:
            HEADER = '\033[95m'
            OKBLUE = '\033[94m'
            OKCYAN = '\033[96m'
            OKGREEN = '\033[92m'
            WARNING = '\033[93m'
            FAIL = '\033[91m'
            ENDC = '\033[0m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'

        for counter1 in ip_file_RAW:
            ip_file_SANITISED.append(counter1.replace("\n", ""))

        for counter2 in temp:
            temp2.append(counter2.replace(".", ""))

        #Letter sanitation and checking
        for counter3 in temp2:
            for char in counter3:
                good_pass = True
                Remove_ip = False
                if str.isdigit(char) == False:
                    print(counter3, bcolors.FAIL + "has a letter included" + bcolors.ENDC)
                    good_pass = False
                    invalid_ip.append(temp2.index(counter3))
        invalid_ip.sort(reverse=True)
        for x in invalid_ip:
            ip_file_SANITISED.pop(x)
        #value validation and range checking 
        for counter4 in ip_file_SANITISED:
            bytearr.clear()
            skip_pass = False
            try:
                First_byte, Second_byte, Third_byte, Forth_byte =[int(counter5) for counter5 in counter4.split(".")]
                bytearr.extend((First_byte, Second_byte, Third_byte, Forth_byte))
            except:
                skip_pass = True
                print("[", ip_file_SANITISED[ip_file_SANITISED.index(counter4)], "]",  bcolors.FAIL + "Ip adress is to long or short" + bcolors.ENDC)

            counter8 = 0
            counter7 = -1
            if skip_pass == False:
                for counter6 in bytearr:
                    counter7 = counter7 + 1
                    good_pass = True
                    counter8 = counter8 + 1
                    #range check will report any ip's  that are out side the rage of 255 and 0
                    if counter6 > 255 or counter6 < 0:
                        print(byteadress[counter7], bcolors.FAIL + "from" + bcolors.ENDC ,bytearr, bcolors.FAIL + "is out of range" + bcolors.ENDC)
                        good_pass = False
                        counter9 = counter9 + 1
                    if good_pass == True and counter8 == 4:
                        print(bytearr, bcolors.OKGREEN + "is a Valid IP Address" + bcolors.ENDC, ip_file_SANITISED.index(counter4) + 1)

        #counts and checks how many IP's have validated and compares between the ammount of Ip's that where entered
        validation_value = len(ip_file_SANITISED)
        validation_value = validation_value - 1 
        validation_value = validation_value - (counter9)
        if validation_value != len(ip_file_RAW):
            print(validation_value, "of", len(ip_file_RAW), bcolors.WARNING + "IP's validated" + bcolors.ENDC)
        else:
            print(validation_value, "of", len(ip_file_RAW), bcolors.OKGREEN + "IP's validated" + bcolors.ENDC)




end_program = False

os.system('cls')
print("welcome", credentials_san[2])
while end_program == False:
    actions = str(input(""))
    actions = actions.replace(" ", "_")
    try:
        func = programs.__dict__.get(actions)
        func.__func__()
    except:
        print(bcolors.FAIL + "Program not found in index " + bcolors.ENDC, "\n", bcolors.WARNING + "try the 'help' command" + bcolors.ENDC)