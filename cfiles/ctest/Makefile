SRCS = $(wildcard *.c)
NAME = exe
GCC = gcc
FLAGS = -Wall -Werror -Wextra
OBJS = $(SRCS:.c=.o)
.Phony: all clean fclean
$(NAME): $(OBJS)
	$(GCC) $(FLAGS) $(OBJS) -o $(NAME)
.c.o: $(SRCS)
	$(GCC) $(FLAGS) -c -o $@ $<
all : $(OBJS) $(NAME)
clean:
	del /f $(OBJS)
fclean: clean
	del /f $(NAME)
re:
	clean all

