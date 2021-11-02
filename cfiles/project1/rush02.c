#include "header.h"
int main()
{
	int	fd;
	int re;
	char c;
	int i;
	char buf[SIZE + 1];
	char str[100];
	int	k;
	int	v;
//	s_node *dict;

	fd = open("number.dict", O_RDWR );
	re = 1;
	c = '0';
	i = 0;
	k = 0;
	v = 0;
//	str = (char *)malloc(sizeof(char) * 1024);
//	buf = (char *)malloc(sizeof(char) * 4096);
//	dict = (s_node *)malloc(sizeof(s_node) * 1024); 
//	*str = '\0';
//	str++;
	
	while (re != 0)
	{
		re = read(fd, &buf, SIZE);
		buf[re] = '\0';
	   	if (buf[i] == ':' || buf[i] == ' ' || i == SIZE)
		{
			continue;
		}
//		k = 0;
//		v = 0;
		
		while (('0' <= buf[i] && buf[i] <= '9') || i < SIZE)
		{
//			dict[0].key[k] = buf[i];
			str[i] = buf[i];
			printf("%c", str[i]);
			i++;
//			k++;
		}
/*		dict.key[k] = '\0';
//		dict[i].key[k] = '\0';
		while ('A' <= *buf && *buf <= 'z')
		{
			dict[i].value[v] = *buf;
			printf("%c", dict[i].key[v]);
			buf++;
			v++;
		}*/
//		dict[i].value[v] = '\0';
//		printf("%s\n", dict->key);
//		dict++;
		}
	
	close(fd);
	return (0);
}
