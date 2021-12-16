#include <fcntl.h>
#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"
#include "get_next_line.h"

void	free_mem(char *str[])
{
	int	i;

	i = 0;
	while (str[i])
	{
		free(str[i]);
		i++;
	}
	
}

char	*get_next_line(int fd)
{
	char		**buf;
	int			size1;
	static int	i;

	i = 1;
	size1 = 1;
	if(size1) size1++;
	if (-1 == fd)
		return(NULL);
	buf = (char **)ft_calloc(fd + 1, BUFFER_SIZE + 1);
	if (!buf)
		return (NULL);
	while ((buf[fd][i - 1] != '\n') && size1)
	{
		size1 = read(fd, &(buf[fd][i]), 1);
		printf("%d", size1);
		if (-1 == size1)
		{
			free_mem(buf);
			return (NULL);
		}
		i++;
	}
	return(buf[fd]);
}

// int	main(int argc, char *argv[])
// {
// 	int		fd1;
// 	//int		fd2;
// 	char	*str;

// 	if (argc == 1)
// 		fd1 = 0;
// 	fd1 = open(argv[1], O_RDONLY);
// 	//fd2 = open(argv[2], O_RDONLY);
// 	str = get_next_line(fd1);
// 	printf("%s", str);
// 	// str = get_next_line(fd1);
// 	// printf("%s", str);
// 	close(fd1);
// 	//close(fd2);
// 	return (0);
// }