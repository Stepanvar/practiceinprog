# import tools to create the C extension
from distutils.core import setup, Extension

module_name = 'func_module'
# the files your extension is comprised of
c_files = ['func_module.c']

extension = Extension(
    module_name,
    c_files
)

setup(
    name=module_name,
    version='1.0',
    description='The package description',
    author='stepanvar',
    author_email='zsteve2911@gmail.com',
    url='https://my.web.site/some_page',
    ext_modules=[extension]
)
