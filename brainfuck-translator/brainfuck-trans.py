def brainfuck(code):
    memory = [0] * 30000
    pointer = 0
    output = ""
    i = 0
    while i < len(code):
        if code[i] == '>':
            pointer += 1
        elif code[i] == '<':
            pointer -= 1
        elif code[i] == '+':
            memory[pointer] += 1
        elif code[i] == '-':
            memory[pointer] -= 1
        elif code[i] == '.':
            output += chr(memory[pointer])
        elif code[i] == ',':
            memory[pointer] = ord(input())
        elif code[i] == '[':
            if memory[pointer] == 0:
                loop_count = 1
                while loop_count != 0:
                    i += 1
                    if code[i] == '[':
                        loop_count += 1
                    elif code[i] == ']':
                        loop_count -= 1
        elif code[i] == ']':
            loop_count = 1
            while loop_count != 0:
                i -= 1
                if code[i] == '[':
                    loop_count -= 1
                elif code[i] == ']':
                    loop_count += 1
            i -= 1
        i += 1
    return output

code = input('brainfuck code here -> ')
output = brainfuck(code)
print(f'brainfuck code -> {output}')
