#include "header.h"
static	char ft_right_field(char c, int i, int j)
{
	if (j == 0 || j == 19 || i == 0 || i == 9)
		c = '#';
	else
		c = ' ';
	return (c);
}

static void	ft_print_field(char mas[10][21], int x, int y, t_apple apple)
{

	int	i;
	int	j;

	i = 0;
	j = 0;
	while (i < 10)
	{
		j = 0;
		while (j < 20)
		{
			mas[i][j] = ft_right_field(mas[i][j], i, j);
			if (i == y && j == x)
				ft_putchar_fd('@', 1);
			else if (i == apple.ay && j == apple.ax)
				ft_putchar_fd('*', 1);
			else
				ft_putchar_fd(mas[i][j], 1);
			j++;
		}
		ft_putchar_fd('\n', 1);
		i++;	
	}
}

static void	ft_pos_dog(char mas[10][21], int x, int y)
{
	int			ox;
	int			oy;
	char		key;
	t_apple		apple;

	srand(time(NULL));
	apple.ax = 5;
	apple.ay = 3;
	while (1)
	{
		key = getch();
		ox = x;
		oy = y;
		if (key == 'w') y--;
		else if(key == 'a') x--;
		else if(key == 's') y++;
		else if(key == 'd') x++;
		else
			return ;
		if (mas[y][x] == '#')
		{
			y = oy;
			x = ox;
		}
		if (x == apple.ax && y == apple.ay)
		{	
			apple.ax = rand() % 18 + 1;
			apple.ay = rand() % 8 + 1;
		}
		system("cls");
		ft_print_field(mas, x, y, apple);
	}
}

int	main(void)
{
	int			x;
	int			y;
	char		mas[10][21];
	int			d;
	t_apple		apple;

	x = 10;
	y = 5;
	apple.ax = 5;
	apple.ay = 3;
	ft_print_field(mas, x, y, apple);
	ft_pos_dog(mas, x, y);
}