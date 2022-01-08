#include "header.h"
#include "limits.h"
void    ft_limits(void)
{
    printf("char bit: %d\n", CHAR_BIT);
    printf("char min: %d\n", CHAR_MIN);
    printf("char max: %d\n", CHAR_MAX);
    printf("overflow : %d\n", INT_MAX + 1);
    printf("int bit: %d\n", sizeof(int);
    printf("int min: %d\n", INT_MIN);
    printf("int max: %d\n", INT_MAX);
}
