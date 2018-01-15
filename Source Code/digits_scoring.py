#Uses python3
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

def sum_digits(d):
   s = 0
   while d:
       s, d = s + d % 10, d // 10
   return s

def score_digits(x):
    if len(str(x)) == 1:
        score = sum_digits(int(x))/len(str(x))
    if len(str(x)) == 2:
        score = sum_digits(int(x))/len(str(x))
        compensation = (int(str(x)[1]) + 0.1 - int(str(x)[0]))/10
        score = score + compensation
    if len(str(x)) == 3:
        score = sum_digits(int(str(x)[:2]))/len(str(x)[:2])
        if int(str(x)[1]) <= int(str(x)[0]):
            if int(str(x)[2]) < int(str(x)[0]):
                compensation_1 = (int(str(x)[1]) - int(str(x)[0]))/10
                compensation_2 = (int(str(x)[2]) - int(str(x)[0]))/100
            if int(str(x)[2]) >= int(str(x)[0]):
                compensation_1 = (int(str(x)[1]) + 0.1 - int(str(x)[0]))/10
                compensation_2 = (int(str(x)[2]) + 0.01 - int(str(x)[0]))/100
        if int(str(x)[1]) > int(str(x)[0]):
            if int(str(x)[2]) <= int(str(x)[0]):
                compensation_1 = (int(str(x)[1]) - int(str(x)[0]))/10
                compensation_2 = (int(str(x)[2]) - int(str(x)[0]))/100
            if int(str(x)[2]) > int(str(x)[0]):
                compensation_1 = (int(str(x)[1]) + 0.1 - int(str(x)[0]))/10
                compensation_2 = (int(str(x)[2]) + 0.01 - int(str(x)[0]))/100
        score = score + compensation_1 + compensation_2
    if len(str(x)) == 4:
        score = sum_digits(int(x))/len(str(x))
    return score

def largest_number(a):
    global starttime, endtime
    starttime = time.clock()
    digits = {}
    res = ""
    #for n in range(int(str(max(a))[0]), 0,-1):
    for n in range(9, 0,-1):
        for i in a:
            #print(i, a)
            if str(i).startswith(str(n)):
                digits.setdefault(n, []).append((i, score_digits(int(i))))
    sorted_digits = sorted(digits.items(), key=lambda tup: tup[0], reverse=True)
    for k, v in sorted_digits:
        sa = sorted(v, key=lambda tup: tup[1], reverse=True)
        for f,g in sa:
            res += f
    endtime = time.clock()
    return res

if __name__ == '__main__':
    userinput = get_num('numbers.txt')
    data = userinput.split()
    a = data
    min_a = min(a)
    max_a = max(a)
    num_of_inputs = len(a)
    print('LARGEST NUMBER: ',largest_number(a))
    print('DIGITS SCORING')
    print('RUNNING TIME: ', endtime-starttime)
    print('NUM OF Inputs: ',len(a))
    print('STR RANGE:', min_a,'-',max_a)
    input()
