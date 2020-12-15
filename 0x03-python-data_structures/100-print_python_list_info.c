#include "Python.h"

void print_python_list_info(PyObject *p)
{
	int i, size;
	struct _typeobject *type;

	if (PyList_Check(p))
	{
		size = PyList_Size(p);
		printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < size; i++)
		{
			type = Py_TYPE(PyList_GetItem(p, i));
			printf("Element %d: %s\n", i, type->tp_name);
		}
	}
}
