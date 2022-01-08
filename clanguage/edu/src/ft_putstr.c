#include "header.h"
void    ft_putstr(const char *str)
{
    char	*begin;

    begin = str;
    while(*begin)
    {
        write(1, str, 1);
        begin++;
    }
}
