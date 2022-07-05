import sys

def add():
    lst[index] += 1

def sub():
    lst[index] -= 1

def right():
    global index
    if index >= len(lst) - 1:
        lst.append(0)
    index += 1

def left():
    global index
    if index > 0:
        index -= 1

def dot():
    print(chr(lst[index]), end='')

def coma():
    code = input()
    try:
        lst[index] = int(code)
    except:
        lst[index] = ord(code)

if __name__ == '__main__':
    lst = [0]
    index = 0
    charPos = 0

    code = sys.argv[1]
    while charPos < len(code):
        if code[charPos] == '+':
            add()
        elif code[charPos] == '-':
            sub()
        elif code[charPos] == '>':
            right()
        elif code[charPos] == '<':
            left()
        elif code[charPos] == '.':
            dot()
        elif code[charPos] == ',':
            coma()
        elif code[charPos] == '[':
            if lst[index] == 0:
                while code[charPos] != ']':
                    charPos += 1
        elif code[charPos] == ']':
            if lst[index] != 0:
                while code[charPos] != '[':
                    charPos -= 1
        charPos += 1
    
    print()