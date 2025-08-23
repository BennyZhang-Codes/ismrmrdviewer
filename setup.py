from setuptools import setup, find_packages

setup(
    name='ismrmrdviewer',
    version='0.2.1',
    packages=find_packages(),
    license='LICENSE.txt',
    author='Kristoffer Langel and Knudsen',
    author_email='kristofferlknudsen@gradientsoftware.net',
    description='Simple tool for viewing ISMRMRD data.',
    install_requires=[
        "contourpy==1.3.3",
        "cycler==0.12.1",
        "fonttools==4.59.1",
        "h5py==3.14.0",
        "ismrmrd==1.14.1",
        "kiwisolver==1.4.9",
        "matplotlib==3.10.5",
        "numpy==2.3.2",
        "packaging==25.0",
        "pillow==11.3.0",
        "pyparsing==3.2.3",
        "PySide6==6.9.1",
        "PySide6_Addons==6.9.1",
        "PySide6_Essentials==6.9.1",
        "python-dateutil==2.9.0.post0",
        "shiboken6==6.9.1",
        "six==1.17.0",
        "typing_extensions==4.14.1",
        "xsdata==25.7"
    ],
    entry_points={
        'gui_scripts' : [ 'ismrmrdviewer=ismrmrdviewer.__main__:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
