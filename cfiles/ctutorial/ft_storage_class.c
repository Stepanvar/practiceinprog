#include "header.h"
extern int i = 5;
void    ft_storage_class(void)
{
    printf("%d", i);
    auto int i;
    i = 10;
    printf("%d", i);
    register char *str = "what the fuck am i listening?";
    ft_putstr(str);

}