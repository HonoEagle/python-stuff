def text_to_brainfuck(text):
    output = ""
    for c in text:
        ascii_value = ord(c)
        output += ">" + "+" * ascii_value + "."
    return output

text = input('put the text here -> ')
brainfuck_code = text_to_brainfuck(text)
print(brainfuck_code)
