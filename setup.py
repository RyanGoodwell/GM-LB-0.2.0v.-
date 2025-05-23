from setuptools import setup, find_packages

setup(
    name="game_library",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        'pygame>=2.0.0'
    ],
    author="RyanGoodwell",
    author_email="rubahagoodwell@gmail.com",
    description="A simple game development library",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
