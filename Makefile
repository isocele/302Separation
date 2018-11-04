##
## EPITECH PROJECT, 2018
## makefile
## File description:
## makefile
##

RM	=	rm -f

all:
		cp 302separation.py 302separation

clean:
		$(RM) 302separation

fclean:		clean

re:		fclean all
