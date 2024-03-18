# Create this fun Password Python program example below.

# Created by Joseph C. Richardson, GitHub.com

message_text = 'Please type your password to enter: '
password = 'open sesame'
welcome = "Welcome!\n\nYou've gained access into HEXADECACOM A.I."
incorrect_password = 'PASSWORD INCORRECT!\n'
end_program = 'Now you know how to make Python create a password, that only you know.'

count = 1
while count <= 3:

    message = input(message_text)

    if message == password:
        print('\n'+welcome+'\n') # This is where you would put all your nice, complex Python code
        break
    
    else:
        print('\n'+incorrect_password)
    count += 1

print(end_program)
