SRCS = $(wildcard *.c)
NAME = types
GCC = gcc
HEAD = header.h
OBJS = $(SRCS:.c=.o)
FLAGS = -Wall -Wextra -Werror
RM = del /f
.Phony: clean fclean re all
.SUFFIXES: .c .o
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
	fclean all
	
