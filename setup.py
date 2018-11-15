from distutils.core import setup, Extension

keyfinder_module = Extension(
    'keyfinder._internal',
    sources=['keyfinder.cpp'],
    include_dirs=['/usr/local/include'],
    library_dirs=['/usr/local/lib'],
    libraries=['keyfinder', 'avcodec', 'avformat', 'avutil', 'avresample'],
    extra_compile_args=['-std=c++11'],
)

setup(
    name='keyfinder',
    version='1.0',
    description='Determine the key of an audio file',
    ext_modules=[keyfinder_module],
    packages=['keyfinder'],
    author='Evan Purkhiser',
    author_email='evanpurkhiser@gmail.com'
)
