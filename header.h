#ifndef HEADER_H
# define HEADER_H
// This definition is needed for future-proofing your code
// see https://docs.python.org/3/c-api/arg.html#:~:text=Note%20For%20all,always%20define%20PY_SSIZE_T_CLEAN.
# define PY_SSIZE_T_CLEAN
// The actual Python API
# include <Python.h>
# include <unistd.h>
# include <stdio.h>
#endif
