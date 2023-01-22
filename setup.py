from setuptools import setup, find_packages

setup(
    name="TOPSIS-102003105",
    version="1.0.0",
    license="MIT",
    description="A Python package to find TOPSIS for Multi-Criteria Decision Analysis Method",
    long_description=open('README.txt').read() + '\n\n' +
    open('CHANGELOG.txt').read(),
    long_description_content_type="text/markdown",
    author="Aditya Kuthiala",
    author_email="adityakuthiala1806@gmail.com",
    url="https://github.com/AdiK1806/Topsis-Aditya-102003105",
    keywords=['topsis', 'TIET' ,'Thapar'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pandas', 'tabulate'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)
