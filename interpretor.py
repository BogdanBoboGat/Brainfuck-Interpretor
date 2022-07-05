def add():
    lst[index] += 1

def sub():
    lst[index] -= 1

def right():
    global index
    if index == len(lst) - 1:
        return
    index += 1

def left():
    global index
    if index == 0:
        return
    index -= 1

def dot():
    print(chr(lst[index]), end='')

def coma():
    inp = input()
    try:
        lst[index] = int(inp)
    except:
        lst[index] = ord(inp)

if __name__ == '__main__':
    lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    index = 0
    charPos = 0

    while True:
        inp = input()
        while charPos < len(inp):
            if inp[charPos] == '+':
                add()
            elif inp[charPos] == '-':
                sub()
            elif inp[charPos] == '>':
                right()
            elif inp[charPos] == '<':
                left()
            elif inp[charPos] == '.':
                dot()
            elif inp[charPos] == ',':
                coma()
            elif inp[charPos] == '[':
                if lst[index] == 0:
                    while inp[charPos] != ']':
                        charPos += 1
            elif inp[charPos] == ']':
                if lst[index] != 0:
                    while inp[charPos] != '[':
                        charPos -= 1
            charPos += 1