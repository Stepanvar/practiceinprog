square = ['#', '#', '#', '\n', '#', ' ', '#', '\n']
for i in range(4):
    square.append(square[i])
for x in square:
    print(x, end='')
symb = '#' #input('enter symbol for borders\n')
length = 3 #int(input('enter length of field\n'))
width = 3 #int(input('enter width of field\n'))
def border_vert_line(symb, width):
    print (symb * width)
def draw_field(symb:'symbol for walls', length, width):
    """ draw needed field"""
    border_vert_line(symb, width)
    for i in range(length - 2):
        print(symb + ' ' * (width - 2) + symb)
    border_vert_line(symb, width)
draw_field(symb, length, width)

