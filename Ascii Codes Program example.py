'''ASCII CODES:'''
'''American Standard Code for Information Interchange'''
'''
All modern day computers that support text characters such as \
keyboard interfaces use ASCII codes. Since computers can only \
see numbers, not actual characters, ASCII codes make it possible \
to use numbers to represent one, single character. Each character \
is seven bits long, which makes it equal to one eight-bit byte; the \
eighth, leftmost bit is the 'sign-bit'. If the number is positive, the \
'sign-bit' will be a 'zero', and if the number is a negative number, \
the 'sign-bit will be a 'one'. Take a look at the illustration below to \
gain a better understanding.

One eight-bit binary byte = 11111111 = 255 = 128 or -127
One byte value 00000100 = '4'
One byte value 1000100 = '-4'
The 'sign-bit' can only be one of two states; either negative or positive.

However, ASCII code values are read as human decimal numbers. \
For example, the ASCII code value for the capital later 'A' = '65'. The \
ASCII code value for the lowercase 'a' = '97'. The ASCII code value for \
the capital letter 'B' = '66', and the ASCII code value for the lowercase \
'b' = '98'. Just remember every letter and every number on a computer \
keyboard has an ASCII code value to it. Below are some basic examples \
how to use ASCII code characters in your programs.
'''
'''----------------------------------------------------------------'''

# To get the ASCII code value of any letter or number key, simply type and execute/run
# the program examples below and see what happens. Try using different letters and
# numbers to see their ASCII code values.

print(chr(65))
print(ord('A'))

print(chr(97))
print(ord('a'))

print(chr(66))
print(ord('B'))

print(chr(98))
print(ord('b'))

print('ASCII code',ord('A'),'is the uppercase letter',chr(65))
print('ASCII code',ord('a'),'is the lowercase letter',chr(97))

print('ASCII code',ord('B'),'is the uppercase letter',chr(66))
print('ASCII code',ord('b'),'is the lowercase letter',chr(98))

'''----------------------------------------------------------------'''

# These simple dictionary program examples below illustrates the entire ASCII code
# alphabet character sets: uppercase and lowercase character sets. Type and
# execute/run the program examples below and see what happens.

ascii_lowercase_chars=(

    {'a':97,'b':98,'c':99,'d':100,
     
     'e':101,'f':102,'g':103,'h':104,
     
     'i':105,'j':106,'k':107,'l':108,
     
     'm':109,'n':110,'o':111,'p':112,
     
     'q':113,'r':114,'s':115,'t':116,
     
     'u':117,'v':118,'w':119,'x':120,

     'y':121,'z':122}
    )

ascii_uppercase_chars=(
    
    {'A':65,'B':66,'C':67,'D':68,
     
     'E':69,'F':70,'G':71,'H':72,
     
     'I':73,'J':74,'K':75,'L':76,
     
     'M':77,'N':78,'O':79,'P':80,
     
     'Q':81,'R':82,'S':83,'T':84,
     
     'U':85,'V':86,'W':87,'X':88,

     'Y':89,'Z':90}
    )

print("Uppercase 'A' = ASCII code value",
      (ascii_uppercase_chars['A']))

print("Lowercase 'a' = ASCII code value",
      (ascii_lowercase_chars['a']))

print("Uppercase 'B' = ASCII code value",
      (ascii_uppercase_chars['B']))

print("Lowercase 'b' = ASCII code value",
      (ascii_lowercase_chars['b']))

'''----------------------------------------------------------------'''

# These simple dictionary program examples below illustrates the ASCII code number
# characters and the ASCII code math operators. Type and execute/run the program
# examples below and see what happens.

ascii_number_chars=(
    {'0':48,'1':49,'2':50,'3':51,'4':52,
     
     '5':53,'6':54,'7':55,'8':56,'9':57}
    )

ascii_math_operator_chars=(    
    {'+':43,'-':45,'*':42,'/':47}
    )

print("Number character '0' = ASCII code value",(ascii_number_chars['0']))

print("Number character '1' = ASCII code value",(ascii_number_chars['1']))

print("Number character '2' = ASCII code value",(ascii_number_chars['2']))

print("Number character '3' = ASCII code value",(ascii_number_chars['3']))

print("Math operator character '+' = ASCII code value",
      (ascii_math_operator_chars['+']))

print("Math operator character '-' = ASCII code value",
      (ascii_math_operator_chars['-']))

print("Math operator character '*' = ASCII code value",
      (ascii_math_operator_chars['*']))

print("Math operator character '/' = ASCII code value",
      (ascii_math_operator_chars['/']))
