import sys
from time import sleep

if __name__ == '__main__':
    lst = [0]
    index = 0
    charPos = 0

    code = sys.argv[1]
    
    while charPos < len(code):
        
        # use if you want to see how the algorithm works
        # print(f'code[{charPos}] = {code[charPos]}')
        # sleep(1)
        
        if code[charPos] == '+':
            lst[index] += 1
        
        elif code[charPos] == '-':
            if lst[index] > 0:
                lst[index] -= 1
        
        elif code[charPos] == '>':
            if index >= len(lst) - 1:
                lst.append(0)
            index += 1
        
        elif code[charPos] == '<':
            if index > 0:
                index -= 1
        
        elif code[charPos] == '.':
            print(chr(lst[index]), end='')

        elif code[charPos] == ',':
            inp = input()
            try:
                lst[index] = int(inp)
            except:
                lst[index] = ord(inp)

        elif code[charPos] == '[':
            if lst[index] == 0:
                while code[charPos] != ']':
                    charPos += 1
        
        elif code[charPos] == ']':
            if lst[index] != 0:
                while code[charPos] != '[':
                    charPos -= 1
        print(lst)
        charPos += 1
    
    print()