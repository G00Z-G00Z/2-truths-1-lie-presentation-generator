from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="truths-and-lies-cli",
    version="1.0.2",
    description="Two Truths and a Lie Game presentation generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="G00Z-G00Z",
    author_email="edygomezgg4@gmail.com",
    url="https://github.com/G00Z-G00Z/2-truths-1-lie-presentation-generator",
    py_modules=["truths_and_lies"],
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "pydantic==2.5.2",
        "python-pptx==0.6.23",
    ],
    entry_points={
        "console_scripts": [
            "tlpg-cli=truths_and_lies.cli:cli",
        ],
    },
)
