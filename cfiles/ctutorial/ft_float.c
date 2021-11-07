#include "header.h"
void    ft_float(void)
{
    float   pi;

    pi = 314159E-5;
    printf("\nf : %f\n", pi);
    pi = 314159E-5l;
    printf("g : %g\n", pi);
    pi = 314159E-5 / 2;
    printf("f / 2: %f\n", pi);
}