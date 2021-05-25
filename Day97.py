def write():
    f = open('File.txt', 'w')
    n = int(input('Enter the no. of words: '))
    res = ''
    for i in range(n):
        res += input('Enter the word: ') + ' '
    print(res)
    f.write(res)
    f.close()

def fileWorking():
    f = open('File.txt', 'r')
    s = f.read()
    f.close()
    string = list(map(str, s.split(' ')))
    length = len(string)
    small, large, count = '', '', 0
    for i in string:
        if len(small) > len(i):
            small = i
        if len(large) < len(i):
            large = i
        count += len(i)
    avg = count//length
    f = open('File.txt', 'w')
    f.write('number of words in file ' + length)
    f.write('smallest word in file ' + small)
    f.write('largest word in file ' + large)
    f.write('avg length of all words ' + avg)
    f.close()

try:
    write()
    fileWorking()
except:
    pass