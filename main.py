import random
import re
#chuong 4
#bai4_1
def bai4_1():
    print('find a number bigger than 4')
    while True:
        n = int(input('is it: '))
        if n > 4:
            print('it True')
            break
        else:
            print('no it isnt, try again')

#bai 4.2
def kiemtradangthuc2(s, i):
    vt, vp = s.split(i)
    vt = eval(vt)
    vp = eval(vp)
    if i == "=":
        if vt == vp:
            print('True')
        return
    if i == '<':
        if vt < vp:
            print('True')
        return
    if i == '>':
        if vt > vp:
            print('True')
        return
    print("No")

def kiemtradangthuc(s):
    for i in s:
        if i == '=':
            kiemtradangthuc2(s, i);
            return
        if i == '<':
            kiemtradangthuc2(s, i);
            return
        if i == '>':
            kiemtradangthuc2(s, i);
            return

def kiemtralower(s):
    if s == s.lower():
        print('True')
    else:
        print('False')

def bai4_2():
    s = input()
    # kiemtradangthuc(s)
    kiemtralower(s)

def bai4_3():
    while True:
        alien_color = 'green'
        s = input('ban quai vat mau: ')
        if s == 'green':
            print('ban duoc cong 5 diem!')
        else:
            # print('ban hut')

def bai4_4():
    while True:
        color = random.randint(1, 3)
        alien_color = 'green'
        if color == 1:
            alien_color = 'green'
        if color == 2:
            alien_color = 'yellow'
        if color == 3:
            alien_color = 'red'
        s = input('bam endter de ban quai vat mau: ')
        if alien_color == 'green':
            print('ban trung quai vat xanh ban duoc cong 5 diem!')
        else:
            print('ban trung quai vat mau khac ban duoc cong 10 diem')

bai4_4()