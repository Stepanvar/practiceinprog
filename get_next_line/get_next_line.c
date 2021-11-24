#include <fcntl.h>
#include "stdio.h"
#include "get_next_line.h"

char	*get_next_line(int fd)
{
	char		*buf;
	int			size1;
	//static	int	count = 0;

	size1 = 1;
	buf = (char *)ft_calloc(BUFFER_SIZE, 1);
	while (size1)
	{
		size1 = read(fd, buf, sizeof(char));
		printf("%d", size1);
	}
	return(buf);
}

int	main(void)
{
	int		fd;
	char	*str;

	fd = open("readme.txt", _O_RDONLY);
	str = get_next_line(fd);
	close(fd);
	printf("%s", str);
	return (0);
}