#include "header.h"
void    ft_calc(int argc, char *argv[])
{
    int first_num;
    int second_num;

    first_num = 0;
    second_num = 0;
    if (argc == 4)
    {
        first_num = ft_calc_inint(argv[1]);
        second_num = ft_calc_inint(argv[3]);
        if(*argv[2] == '-')
            ft_putint(first_num - second_num);
        if(*argv[2] == '+')
            ft_putint(first_num + second_num);
        if(*argv[2] == '*')
            first_num = first_num * second_num;
        if(*argv[2] == '/')
            ft_putint(first_num / second_num);
        if (*argv[2] != '-' && *argv[2] != '+' && *argv[2] != '/' && *argv[2] != '*')
            write(1, "incorrect enter\n", 17);
    }
    else
        write(1, "incorrect amount argc\n", 22);
}