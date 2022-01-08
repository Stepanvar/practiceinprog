#include "header.h"
int ft_calc_inint(char *str1)
{
    int num;
    int flag;

    num = 0;
    flag = 1;
    if (*str1 == '-')
        {
            flag = -1;
            str1++;
        }
    while(*str1 != '\0')
        {  
            num = num * 10 + (*str1 - 48);
            str1++;
        }
    return (flag * num);
}
