#include "time.h"
#include "stdlib.h"
#include "stdio.h"
#include <fcntl.h>

int	ft_checkargc(int argc)
{
	if (1 == argc)
	{
		write(2, "File name missing.\n", 19);
		return (1);
	}
	if (argc > 2)
	{
		write(2, "Too many arguments.\n", 20);
		return (1);
	}
	return (0);
}

int main(int argc, char *argv[])
{
	int		fd;
	char	*str;
	int		size;
	int		i;

	size = 1;
	srand(time(NULL));
	if (ft_checkargc(argc))
		return (1);
	str = "\n\n\n\n\n\n\n!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~";
	fd = open(argv[1], O_RDWR | O_APPEND);
	while (size < 128)
	{
		i = rand() % 100;
		size += write(fd, &(str[i]), 1);
	}
	close(fd);
	return (1);
}