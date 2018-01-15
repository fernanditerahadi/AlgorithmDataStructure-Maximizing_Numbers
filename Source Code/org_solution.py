#Uses Python3
import sys, time

def get_num(txt):
    n, m = 0, 0
    while n < 1:
        try:
            filehandle = open(txt,'r', encoding="utf8").read()
            n += 1
        except:
            print('numbers.txt is not found')
            userinput = input('Continue (Y/N) ?')
            if userinput.lower() == 'y':
                print('')
                continue
            else:
                quit()
    loc_1 = filehandle.find('Result:')
    loc_2 = filehandle.find('Random number code')
    while m < 1:
        if loc_1 >= 1 and loc_2 >= 1:
            new_filehandle = filehandle[loc_1+len('Result:\n'):loc_2]
            m += 1
        else:
            print('Error reading file')
            userinput = input('Continue (Y/N) ?')
            if userinput.lower() == 'y':
                print('')
                continue
    numbers = ""
    for line in new_filehandle:
        something = line.replace('\n', '.')
        numbers = numbers + something
    new_numbers = numbers.replace('.', ' ')
    return new_numbers

def largest_number(a):
    global starttime, endtime
    starttime = time.clock()
    res = ""
    while len(a) > 0:
        sMax = find_safe_max_number(a)
        res += sMax
        a.remove(str(sMax))
    endtime = time.clock()
    return res

def find_safe_max_number(a):
    max_ = a[0]
    for x in a:
        max_ = safe_max(max_, x)
    return max_

def safe_max(max_, x):
    A = str(max_) + str(x)
    B = str(x) + str(max_)
    if int(A) > int(B):
        return str(max_)
    if int(A) < int(B):
        return str(x)
    if int(A) == int(B):
        return str(max_)

if __name__ == '__main__':
    userinput = get_num('numbers.txt')
    data = userinput.split()
    a = data
    min_a = min(a)
    max_a = max(a)
    num_of_inputs = len(a)
    print('LARGEST NUMBER: ',largest_number(a))
    print('ORIGINAL SOLUTION')
    print('RUNNING TIME: ', endtime-starttime)
    print('NUM OF Inputs: ',num_of_inputs)
    print('STR RANGE:', min_a,'-',max_a)
    input()
