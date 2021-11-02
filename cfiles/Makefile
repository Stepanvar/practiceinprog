SRCS = hello.c
NAME = hello
GCC = gcc
#HEAD = header.h
OBJS = $(SRCS:.c=.o)
FLAGS = -Wall -Wextra -Werror
RM = del /f
.Phony: clean fclean re all
$(NAME): $(OBJS)
	$(GCC) $(FLAGS) -o $(NAME) $(OBJS)
.c.o: $(SRCS) 
	$(GCC) $(FLAGS)  -o $(OBJS) -c $(SRCS)
all: $(NAME) $(OBJS) 
clean: fclean
	$(RM) $(OBJS)
fclean:
	$(RM) $(NAME).exe
re:
	fclean all
	
