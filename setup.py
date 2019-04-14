from distutils.core import setup, Extension

keyfinder_module = Extension(
    'keyfinder._internal',
    sources=['keyfinder.cpp'],
    include_dirs=['/usr/local/include'],
    library_dirs=['/usr/local/lib'],
    libraries=['keyfinder', 'avcodec', 'avformat', 'avutil', 'swresample'],
    extra_compile_args=['-std=c++11'],
)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='keyfinder',
    version='1.0',
    description='Determine the key of an audio file',
    long_description=long_description,
    long_description_content_type="text/markdown",
    ext_modules=[keyfinder_module],
    packages=['keyfinder'],
    author='Evan Purkhiser',
    author_email='evanpurkhiser@gmail.com',
    url="https://github.com/evanpurkhiser/keyfinder-py",
    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
    ]
)
