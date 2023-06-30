import os,time,math;from math import*

text_features=(
    'cls', # index 0 = clear screen
    '\x1b[31m', # index 1 = red
    '\x1b[32m', # index 2 = green
    '\x1b[33m', # index 3 = yellow
    '\x1b[34m', # index 4 = blue
    '\x1b[37m', # index 5 = white
    'title Majestic Calculator' # index 6 = window title
    )

text_words=(
    f'\n  {text_features[3]}Majestic Calculator\n\n {text_features[5]}Press (1) for Standard \
Decimal Base 10 Calculator\n Press (2) for Binary Base 2 Calculator\n Press (3) for Octal \
Base 8 Calculator\n Press (4) for Hexadecimal Base 16 Calculator\n\n {text_features[3]}(BIN) \
(OCT) (HEX) Number Translator\n\n {text_features[5]}Press (5) for Binary Base 2 Number \
Translator\n Press (6) for Octal Base 8 Number Translator\n Press (7) for Hexadecimal Base \
16 Number Translator\n\n Press (Q) to quit\n\n\
 {text_features[1]}READY:{text_features[5]}', # index 0 = text_words

    f'\n  {text_features[3]}Majestic Calculator\n\n Standard Decimal Base 10 Calculator', # index 1 = text_words

    f'\n  {text_features[3]}Majestic Calculator\n\n Binary Base 2 Calculator', # index 2 = text_words

    f'\n  {text_features[3]}Majestic Calculator\n\n Octal Base 8 Calculator', # index 3 = text_words

    f'\n  {text_features[3]}Majestic Calculator\n\n Hexadecimal Base 16 Calculator', # index 4 = text_words

    f'\n  {text_features[3]}Majestic Calculator\n\n Binary Base 2 Number Translator', # index 5 = text_words

    f'\n  {text_features[3]}Majestic Calculator\n\n Octal Base 8 Number Translator', # index 6 = text_words

    f'\n  {text_features[3]}Majestic Calculator\n\n Hexadecimal Base 16 Number Translator', # index 7 = text_words

    f'\n  {text_features[3]}Majestic Calculator\n\n Binary Base 2 Translator', # index 8 = text_words

    f'\n  {text_features[3]}Majestic Calculator\n\n Octal Base 8 Translator', # index 9 = text_words

    f'\n  {text_features[3]}Majestic Calculator\n\n Hexadecimal Base 16 Translator', # index 10 = text_words

    f'\n\n {text_features[5]}Please enter a decimal base 10 number:{text_features[2]}', # index 11 = text_words

    f'\n\n {text_features[5]}Enter First Number:{text_features[2]}', # index 12 = text_words

    f'\n\n {text_features[5]}Enter (+) (-) (*) (/) Operator:{text_features[2]}', # index 13 = text_words

    f'\n\n {text_features[5]}Enter Second Number:{text_features[2]}', # index 14 = text_words

    f'\n {text_features[3]}Majestic Calculator\n\n{text_features[1]}Invalid operator!', # index 15 = text_words

    f'\n\n {text_features[1]}ERROR! {text_features[3]}Cannot divide by zero.', # index 16 = text_words

    f'\n\n {text_features[1]}ERROR!', # index 17 = text_words

    f'\n {text_features[5]}Do you wish to continue? Press (Enter) or press (Q) to quit:', # index 18 = text_words

    f'\n  {text_features[3]}Thanks for choosing Majestic Calculator' # index 19 = text_words
    )

operator=(
    chr(43),chr(45),chr(42),chr(47) # math operators in ASCII codes
    )

button=('1','2','3','4','5','6','7','q') # button choices, q = quit

def stan_cal():
    while True:
        try:
            os.system(text_features[0])
            num1=int(input(f' {text_words[1]}{text_words[12]}').lower().strip())

            os.system(text_features[0])
            oper=input(f' {text_words[1]}\n\n {text_features[2]}{num1}{text_words[13]}').lower().strip()

            if oper==operator[0]:
                os.system(text_features[0])
                num2=int(input(f' {text_words[1]}\n\n {text_features[2]}{num1} \
{operator[0]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f' {text_words[1]}\n\n {text_features[2]}{num1} \
{operator[0]} {num2} = {text_features[5]}" {int(num1+num2)} "\n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break
            elif oper==operator[1]:

                os.system(text_features[0])
                num2=int(input(f' {text_words[1]}\n\n {text_features[2]}{num1} \
{operator[1]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f' {text_words[1]}\n\n {text_features[2]}{num1} \
{operator[1]} {num2} = {text_features[5]}" {int(num1-num2)} "\n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break
            elif oper==operator[2]:

                os.system(text_features[0])
                num2=int(input(f' {text_words[1]}\n\n {text_features[2]}{num1} \
{operator[2]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f' {text_words[1]}\n\n {text_features[2]}{num1} \
{operator[2]} {num2} = {text_features[5]}" {int(num1*num2)} "\n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break
            elif oper==operator[3]:

                os.system(text_features[0])
                num2=int(input(f' {text_words[1]}\n\n {text_features[2]}{num1} \
{operator[3]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f' {text_words[1]}\n\n {text_features[2]}{num1} \
{operator[3]} {num2} = {text_features[5]}" {int(num1/num2)} "\n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

        except ZeroDivisionError:
            os.system(text_features[0])
            print(f' {text_words[1]}{text_words[16]}')
            time.sleep(2)

        except ValueError:
            os.system(text_features[0])
            print(f' {text_words[1]}{text_words[17]}')
            time.sleep(2)

def bin_cal():
    while True:
        try:
            os.system(text_features[0])
            num1=int(input(f' {text_words[2]}{text_words[12]}').lower().strip())

            os.system(text_features[0])
            oper=input(f' {text_words[2]}\n\n {text_features[2]}{bin(num1)}{text_words[13]}').lower().strip()

            if oper==operator[0]:
                os.system(text_features[0])
                num2=int(input(f' {text_words[2]}\n\n {text_features[2]}{bin(num1)} \
{operator[0]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f' {text_words[2]}\n\n {text_features[2]}{bin(num1)} \
{operator[0]} {bin(num2)} = {text_features[5]}" {bin(num1+num2)} " \
{text_features[2]}= {text_features[5]}" {int(num1+num2)} " \n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[1]:
                os.system(text_features[0])
                num2=int(input(f' {text_words[2]}\n\n {text_features[2]}{bin(num1)} \
{operator[1]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f' {text_words[2]}\n\n {text_features[2]}{bin(num1)} \
{operator[1]} {bin(num2)} = {text_features[5]}" {bin(num1-num2)} " \
{text_features[2]}= {text_features[5]}" {int(num1-num2)} " \n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[2]:
                os.system(text_features[0])
                num2=int(input(f' {text_words[2]}\n\n {text_features[2]}{bin(num1)} \
{operator[2]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f' {text_words[2]}\n\n {text_features[2]}{bin(num1)} \
{operator[2]} {bin(num2)} = {text_features[5]}" {bin(num1*num2)} " \
{text_features[2]}= {text_features[5]}" {int(num1*num2)} " \n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[3]:
                os.system(text_features[0])
                num2=int(input(f' {text_words[2]}\n\n {text_features[2]}{bin(num1)} \
{operator[3]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[2]}\n\n {text_features[2]}{bin(num1)} \
{operator[3]} {bin(num2)} = {text_features[5]}" {bin(int(num1/num2))} " \
{text_features[2]}= {text_features[5]}" {int(num1/num2)} " \n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

        except ZeroDivisionError:
            os.system(text_features[0])
            print(f' {text_words[2]}{text_words[16]}')
            time.sleep(2)

        except ValueError:
            os.system(text_features[0])
            print(f' {text_words[1]}{text_words[17]}')
            time.sleep(2)

def oct_cal():
    while True:
        try:
            os.system(text_features[0])
            num1=int(input(f' {text_words[3]}{text_words[12]}').lower().strip())

            os.system(text_features[0])
            oper=input(f' {text_words[3]}\n\n {text_features[2]}{oct(num1)}{text_words[13]}').lower().strip()

            if oper==operator[0]:
                os.system(text_features[0])
                num2=int(input(f' {text_words[3]}\n\n {text_features[2]}{oct(num1)} \
{operator[0]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f' {text_words[3]}\n\n {text_features[2]}{oct(num1)} \
{operator[0]} {oct(num2)} = {text_features[5]}" {oct(num1+num2)} " \
{text_features[2]}= {text_features[5]}" {int(num1+num2)} " \n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[1]:
                os.system(text_features[0])
                num2=int(input(f' {text_words[3]}\n\n {text_features[2]}{oct(num1)} \
{operator[1]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f' {text_words[3]}\n\n {text_features[2]}{oct(num1)} \
{operator[1]} {oct(num2)} = {text_features[5]}" {oct(num1-num2)} " \
{text_features[2]}= {text_features[5]}" {int(num1-num2)} " \n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[2]:
                os.system(text_features[0])
                num2=int(input(f' {text_words[3]}\n\n {text_features[2]}{oct(num1)} \
{operator[2]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f' {text_words[3]}\n\n {text_features[2]}{oct(num1)} \
{operator[2]} {oct(num2)} = {text_features[5]}" {oct(num1*num2)} " \
{text_features[2]}= {text_features[5]}" {int(num1*num2)} " \n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[3]:
                os.system(text_features[0])
                num2=int(input(f' {text_words[3]}\n\n {text_features[2]}{oct(num1)} \
{operator[3]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[3]}\n\n {text_features[2]}{oct(num1)} \
{operator[3]} {oct(num2)} = {text_features[5]}" {oct(int(num1/num2))} " \
{text_features[2]}= {text_features[5]}" {int(num1/num2)} " \n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

        except ZeroDivisionError:
            os.system(text_features[0])
            print(f' {text_words[3]}{text_words[16]}')
            time.sleep(2)

        except ValueError:
            os.system(text_features[0])
            print(f' {text_words[3]}{text_words[17]}')
            time.sleep(2)

def hex_cal():
    while True:
        try:
            os.system(text_features[0])
            num1=int(input(f' {text_words[4]}{text_words[12]}').lower().strip())

            os.system(text_features[0])
            oper=input(f' {text_words[4]}\n\n {text_features[2]}{hex(num1)}{text_words[13]}').lower().strip()

            if oper==operator[0]:
                os.system(text_features[0])
                num2=int(input(f' {text_words[4]}\n\n {text_features[2]}{hex(num1)} \
{operator[0]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f' {text_words[4]}\n\n {text_features[2]}{hex(num1)} \
{operator[0]} {hex(num2)} = {text_features[5]}" {hex(num1+num2)} " \
{text_features[2]}= {text_features[5]}" {int(num1+num2)} " \n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[1]:
                os.system(text_features[0])
                num2=int(input(f' {text_words[4]}\n\n {text_features[2]}{hex(num1)} \
{operator[1]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f' {text_words[4]}\n\n {text_features[2]}{hex(num1)} \
{operator[1]} {hex(num2)} = {text_features[5]}" {hex(num1-num2)} " \
{text_features[2]}= {text_features[5]}" {int(num1-num2)} " \n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[2]:
                os.system(text_features[0])
                num2=int(input(f' {text_words[4]}\n\n {text_features[2]}{hex(num1)} \
{operator[2]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[4]}\n\n {text_features[2]}{hex(num1)} \
{operator[2]} {hex(num2)} = {text_features[5]}" {hex(num1*num2)} " \
{text_features[2]}= {text_features[5]}" {int(num1*num2)} " \n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break
                
            elif oper==operator[3]:
                os.system(text_features[0])
                num2=int(input(f' {text_words[4]}\n\n {text_features[2]}{hex(num1)} \
{operator[3]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f' {text_words[4]}\n\n {text_features[2]}{hex(num1)} \
{operator[3]} {hex(num2)} = {text_features[5]}" {hex(int(num1/num2))} " \
{text_features[2]}= {text_features[5]}" {int(num1/num2)} " \n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

        except ZeroDivisionError:
            os.system(text_features[0])
            print(f' {text_words[4]}{text_words[16]}')
            time.sleep(2)

        except ValueError:
            os.system(text_features[0])
            print(f' {text_words[4]}{text_words[17]}')
            time.sleep(2)

def bin_trans():
    while True:
        try:
            os.system(text_features[0])
            num_trans=int(input(f' {text_words[8]}{text_words[11]}').lower().strip())

            os.system(text_features[0])
            but=input(f'{ text_words[8]}\n\n {text_features[2]}{num_trans} = {text_features[5]}\
" {bin(num_trans)} "\n {text_words[18]}').lower().strip()

            if but==('\r'):
                continue
            elif but==button[7]:
                break

        except ValueError:
            os.system(text_features[0])
            print(f' {text_words[8]}{text_words[17]}')
            time.sleep(2)

def oct_trans():
    while True:
        try:
            os.system(text_features[0])
            num_trans=int(input(f' {text_words[9]}{text_words[11]}').lower().strip())

            os.system(text_features[0])
            but=input(f' {text_words[9]}\n\n {text_features[2]}{num_trans} = {text_features[5]}\
" {oct(num_trans)} "\n {text_words[18]}').lower().strip()

            if but==('\r'):
                continue
            elif but==button[7]:
                break

        except ValueError:
            os.system(text_features[0])
            print(f' {text_words[9]}{text_words[17]}')
            time.sleep(2)

def hex_trans():
    while True:
        try:
            os.system(text_features[0])
            num_trans=int(input(f' {text_words[10]}{text_words[11]}').lower().strip())

            os.system(text_features[0])
            but=input(f' {text_words[10]}\n\n {text_features[2]}{num_trans} = {text_features[5]}\
" {hex(num_trans)} "\n {text_words[18]}').lower().strip()

            if but==('\r'):
                continue
            elif but==button[7]:
                break

        except ValueError:
            os.system(text_features[0])
            print(f'{text_words[10]}{text_words[17]}')
            time.sleep(2)

def maj_cal():
    os.system(text_features[6])
    while True:
        os.system(text_features[0])
        choice=input(text_words[0]).lower().strip()

        if choice==button[0]:
            stan_cal()
            pass
        elif choice==button[1]:
            bin_cal()
            pass
        elif choice==button[2]:
            oct_cal()
            pass
        elif choice==button[3]:
            hex_cal()
            pass
        elif choice==button[4]:
            bin_trans()
            pass
        elif choice==button[5]:
            oct_trans()
            pass
        elif choice==button[6]:
            hex_trans()
            pass
        elif choice==button[7]:
            os.system(text_features[0])
            print(text_words[19])
            time.sleep(3)
            break

maj_cal()
