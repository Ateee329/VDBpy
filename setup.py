from setuptools import setup, find_packages

setup(
    name='VDBpy',
    version='0.1.3',
    packages=find_packages(),
    description='A simple vector database allows difference search methods (consine similarity and euclidean distance ect.)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Justin He',
    author_email='justin.he814@gmail.com',
    url='https://github.com/Ateee329/VDBpy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
