SRCS = ft_memset.c
NAME = ft_memset
GCC = gcc
#HEAD = header.h
OBJS = $(SRCS:.c=.o)
FLAGS = -Wall -Wextra -Werror
RM = del /f
.Phony: clean fclean re all
$(NAME): $(OBJS)
	$(GCC) $(FLAGS) -o $(NAME) $(OBJS)
.c.o: $(SRCS) 
	$(GCC) $(FLAGS) -c -o $@ $<
all: $(NAME) $(OBJS) 
clean: fclean
	$(RM) $(OBJS)
fclean:
	$(RM) $(NAME).exe
re:
	fclean all
	
