# Here is some HEAD METAL PYTHON PROGRAMMING EXAMPLES to play with.

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
poem = ('''‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.'''[::-1],

'''.tneduts tsetaerg rieht era uoy roF !flesruoy ni eveileB
…su fo srehcaet tsetaerg eht ,suht era dnim eht dna traeh eht roF
.noitanigami ruo fo noitaerc s’maerd eht
,lla fo amolpid tsetaerg eht ot yek eht dloh dnim eht dna traeh eht roF
.rednow otni rednop ot yek eht si nettirw eb ot maxe ylno ehT
.dnim eht dna traeh eht era ,dedeen skoobtxet ylno ehT
!flesti dnim eht fo dna traeh eht fo noitnevni eerf a si
’egdelwonK‘'''[::-1])

print(poem[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(256):print(bin(i),hex(i),oct(i),i)

for i in range(256):print(f'{i:b} {i:x} {i:o} {i:d}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums = [i for i in range(1,11)];print(nums)

nums = [i+2 for i in range(1,11)];print(nums)

nums = [i-2 for i in range(1,11)];print(nums)

nums = [i*i for i in range(1,11)];print(nums)

nums = [i/2 for i in range(1,11)];print(nums)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums = [1,2,3,4,5,6,7,8,9,10]

num = [i if i>=5 else False for i in nums]

print(num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
cubed = lambda x,y:x+y**3

print(cubed(10,10)) # 10*10*10 = 1000 + 10 = 1010
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
cubed = lambda x,y:x**3+y

print(cubed(10,10)) # 10*10*10 = 1000 + 10 = 1010
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
full_name = lambda \
            first_name,middle_name,last_name:\
            first_name+' '+middle_name+' '+last_name

print(full_name('First','Middle','Last'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
auto_multi_dimensional_list = []

for i in range(1,11):
    auto_multi_dimensional_list.append(i)
    print(auto_multi_dimensional_list)
