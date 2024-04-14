# I Never ever use these myself, but they are another tool I might one day have
# a usefulness for. But here is some researching I had done with 'lambda functions()
# These are, what they call anonymous functions, because you use them, then
# throw them away; whatever that means is still unclear to me at this time. So
# every time I learn something new, I always try to expand on it myself with different
# approaches to whatever it is, I might be wanting to learn or understand. Python
# has so many bells and whistles, that I won't in my entire lifetime live to be able to use
# them all, or even understand them all. I'm an almost a Pythonista programmer, but
# I'm not God either. But this is stuff I had learned but I might never ever use such bells
# and whistles at all. But, sometimes we all have to learn new tricks in our fields of
# interests even if we never use such things in our fields, whatever they might be. Every
# field of interest has their own fair share of bells and whistles, just like my chosen field
# of interest does. I love robots, computer science, and had also developed a keen ability
# to do breadboard electronics with a Raspberry Pi 4, since the last two years. Anyway,
# have some fun with these lambda functions(), or not. lol

lambda_func = lambda x:x + 2
print(lambda_func(5))

lambda_func = lambda x:x - 2
print(lambda_func(7))

lambda_func = lambda x,y:x + y
print(lambda_func(5,2))

lambda_func = lambda x,y:x - y
print(lambda_func(7,2))

lambda_func = lambda x,y,z:x + y + z
print(lambda_func(4,2,1))

lambda_func = lambda x,y,z:x - y + z
print(lambda_func(7,5,3))

lambda_func = lambda x,y,z:x - y + z + 2
print(lambda_func(7,5,3))

lambda_func = lambda first,middle,last:first+middle+last
print(lambda_func('Joseph',' C.',' Richardson'))

lambda_func = lambda first,middle,last,science:first+middle+last+science
print(lambda_func('Joseph',' C.',' Richardson',' is into Computer Science.'))

lambda_func = lambda x:True if x> 2 else False
print(lambda_func(2))

lambda_func = lambda x:'Thank you.' if x> 2 else 'I want a higher number than two!'
print(lambda_func(2))

lambda_func = lambda x:True if x> 2 else False
print(lambda_func(2))

lambda_func = lambda x:True if x>= 2 else False
print(lambda_func(2))

lambda_func = lambda x:'Thank you.' if x>= 2 else 'I want a number to equal two or \
higher than two!'
