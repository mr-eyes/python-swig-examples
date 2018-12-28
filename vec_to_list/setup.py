import distutils
from distutils.core import setup, Extension

bar = Extension("_bar",
                sources=['bar.i', 'foo.cxx', 'bar.cxx', ],
                swig_opts=['-Wall', '-c++'],
                )
#sources = ['bar.i','foo.cxx','bar.cxx'],

setup(
    name='bar',
    ext_modules=[bar, ],
)
