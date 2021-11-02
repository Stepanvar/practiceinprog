#ifndef HEADER_H
# define HEADER_H
# include <unistd.h>
# include <stdlib.h>
# include <fcntl.h>
# include <sys/types.h>
# include <sys/uio.h>
# include <stdio.h>
# define SIZE 20
typedef struct s_dict
{
	char key[200];
	char value[200];	
} s_node;
#endif
