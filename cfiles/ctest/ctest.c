#include "unistd.h"
int ft_test_sentptr(int argc, char *argv[])
{
    int flag, first_num;

    flag = 1;
    argc++;
    first_num = 10;
    if (*argv[1] == '-')
        {
            flag = -1;
            argv[1]++;
        }
    while(*argv[1])
        {
            first_num = first_num * 10 + (*argv[1] - 48);
            argv[1]++;
        }
    return (flag);
}
int main(int argc, char *argv[])
{
    int i;
    i = ft_test_sentptr(argc, argv);
    write(1, argv[1], 1);
    return (i);
}