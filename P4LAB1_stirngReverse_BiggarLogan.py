a = input()

quit_txt = ['done', 'Done', 'd']

while a not in quit_txt:
    print(a[::-1])
    a = input()