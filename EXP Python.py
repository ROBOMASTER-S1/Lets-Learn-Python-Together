x = []
line_brk='\n'
sentence='type a list of four words: '.capitalize()

for i in range(5):
    message=input(sentence).title().strip()
    x.append(message)
    x.sort()

print(line_brk+x[0],x[1],x[2],x[3])


                
