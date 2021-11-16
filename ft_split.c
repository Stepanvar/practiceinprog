/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ccurie <ccurie@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/11/14 13:37:24 by ccurie            #+#    #+#             */
/*   Updated: 2021/11/16 15:06:20 by ccurie           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stddef.h>
#include "stdlib.h"

static size_t	ft_nbr_word(const char *str, char c)
{
	size_t	count;

	count = 0;
	while (*str)
	{
		while (*str == c)
			str++;
		if (*str != c && *str != '\0')
			count++;
		while (*str != c && *str)
			str++;
	}
	return (count);
}

static void	ft_free(char **mem)
{
	int	i;

	i = 0;
	while (mem[i])
	{
		free(mem[i]);
		i++;
	}
	free(mem);
}

static size_t	ft_word_len(const char *str, char c)
{
	int	i;

	i = 0;
	while (*str == c)
		str++;
	while (*str && *str != c)
	{
		i++;
		str++;
	}
	return (i);
}

static char	**ft_real_split(char const *s, char c)
{
	size_t	word_count;
	size_t	i;
	char	**str;

	if (!s)
		return (NULL);
	word_count = ft_nbr_word(s, c);
	str = ft_calloc(word_count + 1, sizeof(char *));
	if (!str)
		return (0);
	i = 0;
	while (word_count > i)
	{
		while (*s == c)
			s++;
		str[i] = ft_substr(s, 0, ft_word_len(s, c));
		if (!str[i++])
		{
			ft_free(str);
			return (NULL);
		}
		s += ft_word_len(s, c);
	}
	str[i] = NULL;
	return (str);
}

char	**ft_split(char const *s, char c)
{
	char	**str;

	if (!s)
		return (NULL);
	str = ft_real_split(s, c);
	if (!str)
		return (NULL);
	return (str);
}
