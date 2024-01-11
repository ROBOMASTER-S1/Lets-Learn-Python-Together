# Goofy Python Programming Code that actually works

x = []
line_brk='\n'
dline_brk='\n\n'
text=print,input
loop=range

sentence='type a list of five words: '.capitalize(),\
          'you have all'.capitalize(),'items in your list of words.'

for i in loop(1,6):
    message=text[1](sentence[0]).title().strip()
    x.append(message)
    x.sort()

for j in loop(i):
    text[0](x[j],end=' ')

text[0](dline_brk+sentence[1],i,sentence[2])
