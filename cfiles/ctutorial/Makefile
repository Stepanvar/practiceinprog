SRCS = $(wildcard ft_*.c)
NAME = exec
GCC = gcc
HEAD = header.h
OBJS = $(SRCS:.c=.o)
FLAGS = -Wall -Wextra -Werror
RM = rm -rf
.Phony: clean fclean all
$(NAME): $(OBJS)
	$(GCC) $(FLAGS) $(OBJS) $(HEAD) -o $(NAME)
.c.o: $(SRCS) 
	$(GCC) $(FLAGS) -c -o $@ $< 
all: $(NAME) $(OBJS) 
clean: fclean
	$(RM) $(OBJS)
fclean:
	$(RM) $(NAME).exe
re:
	clean all
	
