import random

not_love = ['Sorry, not a match.'.title(), 'Not in the cards.'.title(), 'This relationship is not meant to be.'.title(), 'Not true love.'.title(), 'Someone else is out there for you.'.title()]
love = ['This is A match!'.title(), 'This is love!'.title(), 'Hold on to each other!'.title(), 'Soul mate connection!'.title(), 'Perfect Union!'.title()]
maybe_love = ['Not impossible but not be easy'.title(), '50/50 chance at love'.title(), 'A Troubled and Fruitful Connection'.title(), 'Maybe but will be difficult'.title()]

while True:

    name1a = input('Your First Name: ').strip()
    if name1a.isalpha():
        break
    else:
        print('* Invalid Entry *')
while True:

    name1b = input('Your Last Name: ').strip()
    if name1b.isalpha():
        break
    else:
        print('* Invalid Entry *')

while True:

    birth1 = input('Year You Were Born: ').strip()
    if birth1.isdigit():
        break
    else:
        print('* Numerical Entry Required (ex. 1988) *')

while True:

    name2a = input("Their First Name: ").strip()
    if name2a.isalpha():
        break
    else:
        print('* Invalid Entry *')

while True:

    name2b = input("Their Last Name: ").strip()
    if name2b.isalpha():
        break
    else:
        print('* Invalid Entry *')


while True:

    birth2 = input('Year They Were Born: ').strip()
    if birth2.isdigit():
        break
    else:
        print('* Numerical Entry Required (ex. 1988) *')


name1 = name1a + name1b
name2 = name2a + name2b
birth = birth1 + birth2

combo = len(name1) + len(name2)


if combo % 2 == 0 and int(birth) % 2 != 0:
    print("\n" + random.choice(maybe_love))
elif combo % 2 == 0 and int(birth) % 2 == 0:
    print("\n" + random.choice(love))
else:
    print("\n" + random.choice(not_love))

