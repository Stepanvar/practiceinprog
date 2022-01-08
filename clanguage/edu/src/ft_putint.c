#include "header.h"
void ft_putint(int num)
{
    char    c;
    int     remain;

    if (num < 10)
    {
         c = num + 48;
         write(1, &c, 1);
    }
    else
    {
        remain = num % 10;
        c = remain + 48;
        ft_putint(num / 10);
        write(1, &c, 1);

    }
}
