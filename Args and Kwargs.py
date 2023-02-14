def test(*args): # unknown number of parameter variables
    print('Hello ',end='')
    return f'{args[0]} {args[1]} {args[2]}'
   

print(test('j','c','r').title()) # unlimited argument values


def test(first,middle,last):
    print('Hello '+first+' '+middle+' '+last)

test(first='j'.title(),middle='c'.title(),last='r'.title())


def test(**kwargs):
    print('Hello '+kwargs['first']+
          ' '+kwargs['middle']+' '+kwargs['last'])

test(first='j'.title(),middle='c'.title(),last='r'.title())


def test(**kwargs):
    print('Hello ',end='')
    for key,value in kwargs.items():
        print(value,end=' ')

test(first='j'.title(),middle='c'.title(),last='r'.title())
