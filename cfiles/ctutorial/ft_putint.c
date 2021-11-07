#include "header.h"
void ft_putint(int num)
{
    char    c;
    int     remain;

    if (num % 10 == 0)
         c = num + '0';
    else
    {
        remain = num % 10;
        ft_putint(num / 10);
        c = remain + '0';
        write(1, &c, 1);

    }
/*    str1 = "a\0";
    remain = 0;
    i = 0;
    while (num % 10 != 0)
    {
        remain = num % 10;
        num /= 10;
        *str1 = remain + '0';
        str1++;
        i++;
    }
    *str1 ='\0';
    printf("%s", str1);
    while(i != 0)
    {
        str1--;
        i--;
    }
    printf("%d", i);
    while(str1)
    {
        write(1, str1, 1);
        str1++;
    }*/
}