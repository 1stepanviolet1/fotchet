from setuptools import setup, Extension
from Cython.Build import cythonize


setup(
    ext_modules=cythonize([
        Extension(
            name='parser',
            sources=['parser.pyx']
        )
    ])
)
