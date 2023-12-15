import re
import json

def name(name):
    if name:
        return True
    return False
def email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
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
with open('data.json', 'r') as file:
    datas = json.load(file)
data = {}
i = 0
while i < 7:
    a = input(signup_questions[i]+": ")
    if a.lower() == "exit":
        break
    if a.replace(" ","") == "" or not func[i](a):
        print("Provide a valid "+error[i])
    else:
        data[error[i]] = a
        i += 1

if i == 7:
    print("Account created successfully.")
    datas[data["email"]] = data
    with open('data.json', 'w') as file:
        json.dump(datas, file)