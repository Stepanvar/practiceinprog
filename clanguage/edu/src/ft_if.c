#include "header.h"
int ft_if(void)
{
    int t;
    char c;

    t = 0;
    c = 'a';
    while (t < 30)
    {
        if (t < 20)
        {
            write(1, "less then 20\n", 13);
            if (t < 10)
            {
                c = t + '0';
                write(1, &c, 1);
            }
        }
        else
        {
            write(1, "bigger then 20\n", 15);
        }
        t++;
    }
    return (t);
}
