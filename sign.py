import re
import time
from connection import Connection
from message import Message

conn = Connection()
message = Message()

def encrypt(passwd):
    s = ""
    for i in passwd:
        s += chr(ord(i)-1) + chr(ord(i)+1)
    return s

def decrypt(passwd):
    s = ""
    for i in range(0, len(passwd), 2):
        s +=chr((ord(passwd[i]) + ord(passwd[i+1])) // 2)
    return s

def refresh():
    global user_data
    email = conn.fetchData("User_Details", "Email")
    password = conn.fetchData("User_Details", "Password")
    user_data = {str(i)[2:-3] : decrypt(str(j)[2:-3]) for i, j in zip(email, password)}


def signin():
    user_name = input("Enter your email: ")
    if user_name in user_data:
        user_password = input("Enter your password: ")
        if user_password == user_data[user_name]:
            name = conn.fetchData(table_name="User_Details", columns="Name", condition=f'WHERE email = "{user_name}"')
            conn.clearScreen()
            print(f"Welcome back {name[0][0]}!")
            id = conn.fetchData(table_name="User_Details", columns="ID", condition=f'WHERE Email = "{user_name}"')
            return id[0][0]
        print("Wrong Password")
        print("Try again in 2s.")
        time.sleep(2)
        return False
    print("Wrong username")
    print("Try again in 2s.")
    time.sleep(2)
    return False


def name(name):
    if name:
        return True
    return False
def email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if email in user_data:
        print("Username is already existed..")
        return
    if re.fullmatch(regex, email):
        return True
    return False

def gender(gender):
    if gender == "M" or gender == "F":
        return True
    return False

def mobile_number(number):
    if len(number) == 10 and number[0] != '0':
        return True
    return False

def aadhar_number(number):
    regex = r"^\d{4}\s\d{4}\s\d{4}$"
    if re.fullmatch(regex, number):
        return True
    return False

def license_number(number):
    regex = r"^[A-Za-z0-9]{6,12}$"
    if re.fullmatch(regex, number):
        return True
    return False

def password(password):
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    if re.fullmatch(regex, password):
        confirm_password = input("Confirm password: ")
        if password == confirm_password:
            return True
    return False

signup_questions = [
    "Enter your name",
    "Enter your email",
    "Type M for male or F for female",
    "Enter your mobile number",
    "Enter your aadhar number",
    "Enter your license number",
    "Enter a password",
]

error = [
    "name",
    "email",
    "gender",
    "mobile number",
    "aadhar number",
    "license number",
    "password",
]

func = [
    name,
    email,
    gender,
    mobile_number,
    aadhar_number,
    license_number,
    password
]



def login():
    while True:
        refresh()
        conn.clearScreen()
        signup = True if input("Type Y for signup N for signin: ").upper() == 'Y' else False
        if signup:
            data = str(len(user_data) + 1)+','
            i = 0
            while i < 7:
                a = input(signup_questions[i]+": ")
                if a.lower() == "exit":
                    break
                if a.replace(" ","") == "" or not func[i](a):
                    print("Provide a valid "+error[i])
                else:
                    if error[i] == "password":
                        data += '"' + encrypt(a) + '",'
                    else:
                        data += '"'+a+'",'
                    i += 1

            if i == 7:
                name, number, purpose = data.split(',')[1], data.split(',')[4],"Account Creation"
                otp = message.otp(name=name, number=number, purpose=purpose)
                if otp == input("Enter The OTP: "):
                    print("Account created successfully.")
                    conn.row_add("User_Details", columns="", values=data[:-1])
                else:
                    print(f"Sorry {'Sir' if data.split(',')[3] == 'M'  else 'Madam'} the entered otp is wrong...")
        else:
            id = signin()
            if id == False:
                continue
            else:
                return id
