#include "header.h"
void    ft_char(void)
{    
    char    c1; //, c2, c3, c4;
    int     num;

    num = 1;
    c1 = num + 48;
    write(1, &c1, 1);
    /*c2 = 0x22;
    c3 = 042;
    c4 = '"';
    ft_putchar(c1);
    ft_putchar('2' + '2');
    ft_putchar('9' + '9' + '9' + '2');
    ft_putchar(1 + '3');
    ft_putchar('1' + '0');
    ft_putchar(c2);
    ft_putchar(c3);
    ft_putchar(c4);*/
}