# STARS Game Demo Python program example.

# Created by Joseph C. Richardson, GitHub.com

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

# Execute/run this program example and see how the
# while-loop only breaks when one of the two 'break'
# statements is executed. If none of them gets
# executed, the while-loop keeps on iterating. This
# program example is another great example of how
# the conditional 'if:' and 'elif:' statements work in
# conjunction with the logical operators.

while True:
    try:
        stars=int(input(f'How many stars would you like? ').strip())
        if stars>1:
            print(f'\n{stars} Stars: [',' * '*stars,f']\n\nI gave you {stars} \
Stars!\n\nI hope you enjoy your {stars} Stars...')
            break

        elif stars==1:
            print(f'\n{stars} Star: [','*'*stars,f']\n\nI gave you {stars} \
Star!\n\nI hope you enjoy your \'One\' \
and \'Only\', single Star...')
            break

        elif stars==0:
            print('\nSorry Hero! Zero doesn\'t count.\n')
    except ValueError:
        print('\nNumbers only please!\n')
