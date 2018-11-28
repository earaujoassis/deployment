import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deployment",
    version="0.1.0",
    license="MIT",
    author="Ewerton Carlos Assis",
    author_email="earaujoassis@gmail.com",
    description="Git-based deployment scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/earaujoassis/deplo",
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),
    python_requires='>=2.6, <4',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'deployment=deployment:main',
        ],
    },
    project_urls={
        'Source': 'https://github.com/earaujoassis/deployment',
        'Tracker': 'https://github.com/earaujoassis/deployment/issues',
    },
)
