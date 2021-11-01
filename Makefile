SRCS = c_module.c
NAME = c_module
GCC = gcc
HEAD = header.h
OBJS = $(SRCS:.c=.o)
FLAGS = -Wall -Wextra -Werror
RM = rm -rf
.Phony: clean fclean re all
$(NAME): $(OBJS) $(HEAD)
	$(GCC) $(FLAGS) -o $(NAME) $(OBJS) $(HEAD)
.c.o: $(SRCS) 
	$(GCC) $(FLAGS)  -o $(OBJS) -c $(SRCS)
all: $(NAME) $(OBJS) 
clean:
	$(RM) $(OBJS)
fclean:
	$(RM) $(NAME)
re:
	fclean all
	
