#define PY_SSIZE_T_CLEAN
#include <Python.h>
int fib(int n)
{
  if (n <= 1)
    return n;
  return fib(n-1) + fib(n-2);
}

static PyObject*	c_fib(PyObject *self, PyObject *args)
{
	int n;
	if (!PyArg_ParseTuple(args, "i", &n))
		return NULL;
	n = fib(n);
	return PyLong_FromLong(n);

}

float Q_rsqrt(float number)
{
	long num;
	float x2, y;
	const float threehalfs = 1.5F;

	x2 = number * 0.5F;
	y = number;
	num = * (long*) &y;
	num = 0x5f3759df - ( num >> 1 );
	y = * (float*) &num;
	y = y * (threehalfs - (x2 * y * y));
	return (y);
}

static PyObject*	c_Q_rsqrt(PyObject *self, PyObject *args)
{
	float n;
	if (!PyArg_ParseTuple(args, "f", &n))
		return NULL;
	n = Q_rsqrt(n);
	return PyFloat_FromDouble(n);

}

PyMethodDef module_methods[] =
{
	{"c_fib", c_fib, METH_VARARGS, "Method description"}, 
	{"c_Q_rsqrt", c_Q_rsqrt, METH_VARARGS, "Method description"}, {NULL}// this struct signals the end of the array
};

struct PyModuleDef func_module =
{
    PyModuleDef_HEAD_INIT, // Always initialize this member to PyModuleDef_HEAD_INIT
    "func_module", // module name
    "Module description", // module description
    -1, // module size (more on this later)
    module_methods // methods associated with the module
};

// function that initializes the module
PyMODINIT_FUNC PyInit_func_module()
{
    return PyModule_Create(&func_module);
}
