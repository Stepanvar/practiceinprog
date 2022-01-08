#include "header.h"
void    ft_putchar(char symb)
{
    write(1, &symb, 1);
    write(1, "\n", 1);
}
