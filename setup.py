from setuptools import setup, find_packages

setup(
    name='ismrmrdviewer',
    version='0.3.0',
    packages=find_packages(),
    include_package_data=True,
    license='LICENSE.txt',
    modified='Jinyuan Zhang',
    author='Kristoffer Langel and Knudsen',
    author_email='kristofferlknudsen@gradientsoftware.net',
    description='Simple tool for viewing ISMRMRD data.',
    install_requires=[
        "contourpy>=1.3.3",
        "cycler>=0.12.1",
        "fonttools>=4.61.1",
        "h5py>=3.15.1",
        "ismrmrd>=1.14.2",
        "kiwisolver>=1.4.9",
        "matplotlib>=3.10.8",
        "numpy>=2.4.2",
        "packaging>=26.0",
        "pillow>=12.1.1",
        "pyparsing>=3.3.2",
        "PySide6>=6.10.2",
        "python-dateutil>=2.9.0",
        "six>=1.17.0",
        "typing_extensions>=4.15.0",
        "xsdata>=26.2"
    ],
    entry_points={
        'gui_scripts' : [ 
            'ismrmrdviewer=ismrmrdviewer.__main__:main' 
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)