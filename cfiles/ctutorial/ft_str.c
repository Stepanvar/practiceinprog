#include "header.h"
void    ft_str(void)
{
    char    *str1;
    //char    c;
    //char    *str2;

    str1 = "i want to eat your soul";
    //str2 = "and invoke you as my summon";
    //str2 = str1;
    write(1, str1, 1);
    printf("%p", str1);

}