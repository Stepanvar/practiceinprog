#define PY_SSIZE_T_CLEAN
#include "stdio.h"
#include "stdlib.h"
#include <Python.h>
static PyObject*	c_fib(PyObject *self, PyObject *args)
{
	int n;
	if (!PyArg_ParseTuple(args, "i", &n))
		return NULL;
	n = fib(n);
	return PyLong_FromLong(n);

}
void 
{
	char	*str;
	int		a, t, g, c;

	a = t = g = c = 0;
	write(1, "enter str\n", 10);
	str = calloc(10000, sizeof(char));
	scanf("%s", str);
	while(*str)
	{
		if(*str == 'A')
			a++;
		else if(*str == 'T')
			t++;
		else if(*str == 'G')
			g++;
		else if(*str == 'C')
			c++;
		str++;
	}
	printf("%d %d %d %d", a, c, g, t);
	return (0);
	
}