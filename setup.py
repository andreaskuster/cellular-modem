import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cellular-modem",
    version="0.0.1",
    author="Andreas Kuster",
    author_email="mail@andreaskuster.ch",
    description="dummy short package description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andreaskuster/cellular-modem",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Natural Language :: English"
    ],
    python_requires='>=3.0',
)