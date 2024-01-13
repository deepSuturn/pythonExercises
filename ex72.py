# This is my first exercise using tuples.
# The objective is to match the numerical number(between 0 and 20) to its full name.

numInFull = (
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
    'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'
)

num = int(input('Type a number between 0 and 20: '))

while True:
    if num >= 0 and num <= 20:
        print(f'You typed the number {numInFull[num]}.')
        break
    else:
        num = int(input('Try again. Type a number between 0 and 20: '))
