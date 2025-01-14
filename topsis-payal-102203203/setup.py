from setuptools import setup, find_packages

setup(
    name='topsis',
    version='0.1.0',
    author='Your Name',
    author_email='your_email@example.com',
    description='A Python package for TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/topsis-package',
    packages=find_packages(),
    install_requires=['numpy', 'pandas'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
