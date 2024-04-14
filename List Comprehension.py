# List Comprehension in Python

# Like always, I research when I want to learn something new, or new to me.
# Since the years I've played around with Python programming, I never ever
# explored list comprehension at all. This is like killing two birds with one stone's
# throw. I'm only experimenting with this tonight; I kept on ignoring it. But it
# shortens for loops down, when looping through a list, using a for loop right
# inside the list[ ] brackets. Believe it or not, I'm also new to this list comprehension
# thing. So you are not alone on this one. But try these out and tinker with them.
# I did that here. I just play and tinker and see what works and what won't work.
# This is what computer science is all about. Sometimes you just have to keep on
# learning and do constant research; you can only avoid something for so long,
# like I did with this headache. But like everything we learn; it gets easier over time.
# Happy researching. I'm also happily doing research with these below.

text_list = ['dog','cat','bird','fish','turtle']

words = [text for text in text_list]
print(words)

text_list = ['dog','cat','bird','fish','turtle']

words = [text if text == 'dog' else 'none' for text in text_list]
print(words[1])

num_list = [1,2,3,4,5]

nums = [num for num in num_list]
print(nums)

num_list = []

nums = [num for num in range(20)]
print(nums)
