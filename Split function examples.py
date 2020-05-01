a=('"Python Programmer\'s Glossary Bible"'.split())

print(f"# Use the 'split()' method to convert printed text \
into a list, using 'f' string format.\n\n{a}")

print('\n# Turn the converted list into actual values.\n\n'+a[0],a[1],a[2],a[3])

print("\n# Use the 'split()' method to convert printed text into a \
list, using old string format.\n\n{}".format(a))

'''-----------------------------------------------------------------------------'''

knowledge_poem=(
f'''\n‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.

THIS BELONGS TO EVERY MAN, WOMAN AND CHILD
Never give up your dream, no matter how far away it may seem to be, because that is when it is ever so
close to becoming true. If you dream of something long enough and strong enough, your dream will come
true, when you least expect it. Always remember, we are never too young or too old to dream and use our
imagination, for we only get one and it is ours forever. May your heart be filled with courage and
compassion, and your mind be as limitless and as wondrous as the universe itself!
If you dream it, you can be it. Believe it!'''.split())

print('\nLet\'s get',len(knowledge_poem),"converted list values out of this Knowledge poem, \
using the 'split()' function.\n")

print('Let\'s get the indexes of the converted list values, using the \'enumerate\' function\n.')

for index,value in enumerate(knowledge_poem):
    print(value,':',index)
    
print('\nLet\'s get the converted list values:',knowledge_poem[0],'and',knowledge_poem[15])
