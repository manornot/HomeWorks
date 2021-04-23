# HomeWork nr2.

# This code encripts text with cesar code, you task is to decript text and print it.

text = 'sucks to be you, my friend! lol!'

cryptedText = ''
for character in text:
    cryptedText += (chr(ord(character) - 1))

print(cryptedText)
