import general_mykyta as gen
from datetime import datetime
import os

new_message = lambda thing,shift,chars :"".join([chars[(chars.find(x)+shift)%len(chars)] if x in chars else x for x in thing])
def verifyAlphabet(alphabet):
     alphabet = alphabet.strip()
     return len(set(alphabet)) == len(alphabet) and len(alphabet) > 0
def get_parameters():
    """gets the chars (supported charachters) and shift(the amount by which the alphabet will shift) parameters from the user in the correct way, and returns them"""
    while True:
        chars = input("Enter supported charachters(vertical bar -> | is not allowed): ")
        if chars == "ALPHABET":
           chars = "".join(gen.alphabet)
           break
        if verifyAlphabet(chars):
             break
        else:
             print("No duplicates allowed and supposed to be nonempty")
    shift = gen.secure("Enter the shift: ",int)%len(chars)
    return chars,shift
def write_file(chars,shift):
    """takes in the chars and shift and requestr a message from the user,
    then asks for a file name, if the file exists asks for permission to owerwrite it, 
    then it encrypts the message and creates or owerwrites the chosen file in the following structure: 
    1st line contains the chars, 2nd line contains the shift, 3rd line contains the time of the write and the encrypted message."""
    message = gen.secure("Enter nonempty message: ","any",1)
    print(f"Encrypted message: {str(new_message(message,shift,chars))}")
    file = gen.secure("Enter ffile name: ","any",1)
    if file[-4:] != ".txt":
        file += ".txt"
    file_path = "ceasar_cipher_messages/" + file
    if os.path.exists(file_path):
        decide = input("File already exists, owerwrite?(y/n): ").lower()
        if decide == "y":
            with open(file_path, "w") as file:
                file.write(f"{chars}\n{shift}\n{str(datetime.now())[:19]}|{str(new_message(message,shift,chars))}")           
        else:
            return
    else:
        with open(file_path, "w") as file:
            file.write(f"{chars}\n{shift}\n{str(datetime.now())[:19]}|{str(new_message(message,shift,chars))}")
def get_read_file():
    """ asks the user for the file they want to read, verifies that it exists, and returns it to get used by read_file()"""
    while True:
            file = gen.secure("Enter file name(or M to go back): ","any",1)
            if file.lower() != "m":
                if file[-4:] != ".txt":
                    file += ".txt"
                file_path = "ceasar_cipher_messages/" + file
                if os.path.exists(file_path):
                      return file_path
                else:
                      print("file not found")
            else:
                return "None"
def read_file(file_path):
    """gets the file name and reads all the 3rd line and higher messages using the 1st line chars and 2nd line shift, also shows the times of the messages"""
    if file_path != "None":
        with open(file_path,"r") as file:
            content = file.read()
        lines = content.split("\n")
        chars = lines[0]
        shift = len(chars) -int(lines[1])
        messages = lines[2:]
        print()
        for line in messages:
            print(f"{line.split("|")[0]}: ")
            print(f"{new_message(line.split("|")[1],shift,chars)}")
def reply_file(file_path):
    """same as write file but already knows the file path and only writes the message on the next line, without chars or shift"""

    print(f"Supported charachters: {lines[0]}")
    with open(file_path,"r") as file:
        content = file.read()
    lines = content.split("\n")
    chars = lines[0]
    print(chars)
    shift = int(lines[1])
    message = gen.secure("Enter reply: ", "any",1)
    print(f"Encrypted message: {str(new_message(message,shift,chars))}")
    with open(file_path,"a") as file:
        file.write(f"\n{str(datetime.now())[:19]}|{str(new_message(message,shift,chars))}")
     
def main():
    """gives the user a menu to chose from and does the functions accordingly (write_file(), read_file()/reply_file, or just exiting"""
    while True:
        print("""   Menu
        1) Start message
        2) Read/Reply
        3) Quit
        """)
        response = gen.secure("Enter your choice: ",int,1,3)
        if response == 1:
            chars,shift = get_parameters()
            write_file(chars,shift)
        elif response == 2:
            file_path = get_read_file()
            read_file(file_path)
            print()
            if file_path != "None":
                decision2 = gen.secure("Do you wish to make a responce(y/n)?: ",str,1,1)
                if decision2.lower() == "y":
                    reply_file(file_path)
        elif response == 3:
            break
    print("GOODBYE!!!")
main()