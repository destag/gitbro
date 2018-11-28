import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='gitbro',
    version='0.1.0.dev0',
    author='Przemysław Pietras',
    author_email='przemyslawp94@gmail.com',
    description='Utility for managing many git repos at once',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=[
        'git',
    ],
    url='https://github.com/destag/at-date',
    license='MIT License',
    packages=setuptools.find_packages(exclude=['test', 'docs']),
    entry_points={
        'console_scripts': ['gitbro=gitbro.cli:main'],
    }
)
