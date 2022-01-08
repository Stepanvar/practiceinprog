#include "header.h"
#include "unistd.h"
void    ft_mas(void)
{
    int mas[10];
    int i;

    i = 0;
    while(i < 10)
    {
        ft_putint(mas[i]);
        ft_putchar(' ');
        i++;
    }
    i = 0;
    while(i < 10)
    {
        mas[i] = i;
        if (i >= 5)
            mas[i] = i * i;
        i++;
    }
    i--;
    while(i > 0)
    {
        printf("\n%d element of mas is ", i);
        ft_putint(mas[i]);
        i--;
    }
}
