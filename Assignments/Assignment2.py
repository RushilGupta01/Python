string = 'Print only the words that start with s in this sentence'
for words in string.split():
    if words[0] == 's':
        print(words)


print(tuple(range(0,11,2)))

num = range(1,51)
for digits in num:
    if digits%3==0:
        print(digits)

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(words)%2==0:
        print(word + '<= has an even length')

for num in range(1,101):
    if num%3==0:
        print('Fizz')
    elif num%5==0:
        print('Buzz')
    elif num%3==0 and num%5==0:
        print('FizzBuzz')
    else:
        print(num)

    
st = 'Create a list of the first letters of every word in this sentence'
for letters in st.split():
    print([letters[0]])