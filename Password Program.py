# Create this fun Password Python program example below.

# Created by Joseph C. Richardson, GitHub.com

message_text = 'Please type your password to enter: '
password = 'open sesame'
welcome = "Welcome!\n\nYou've gained access into HEXADECACOM A.I."
incorrect_password = 'PASSWORD INCORRECT!'
denied_entry = 'You have entered the incorrect password too many times.\n\nAccess Denied!'
end_program = 'Now you know how to make Python create a password, that only you know.'
line_break = '\n'

count = 1
while count <= 3:

    message = input(message_text)

    if message == password:
        print(line_break+welcome+line_break) # This is where you would put all your nice, complex Python code
        break
    
    else:
        print(line_break+incorrect_password+line_break)
    count += 1
    
    if count == 4:
        print(denied_entry+line_break)

print(end_program)
