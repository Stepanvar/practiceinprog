SRCS	=	$(wildcard *.c)
NAME	=	project
CC		=	gcc
OBJS	=	$(SRCS:.c=.o)
FLAG	=	-Wall -Wextra -Werror
OPTFLAG	=	-L../libft -lft
RM		=	rm -rf
.Phony: clean fclean re all
$(NAME): $(OBJS)
	$(CC) $(FLAG) -o $(NAME) $(OBJS) $(OPTFLAG)
%.o	:	%.c
	$(CC) $(FLAGS) -c $< -o $@
all: $(NAME) $(OBJS) 
clean	:
	$(RM) $(NAME)

fclean	:	clean
	$(RM) $(OBJS)

re	:	fclean all

.PHONY	:	all clean fclean re
	
