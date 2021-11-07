#include "header.h"
void    ft_float(void)
{
    float   pi;

    pi = 314159E-5;
    printf("%f\n", pi);
    printf("%f\n", pi);
    pi = 314159E-5l;
    printf("%f", pi);
    pi = 314159E-5L;
    printf("%f", pi);
}