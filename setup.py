import setuptools
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="test-package-id67",
    version="0.0.2",
    author="er",
    author_email="david.hermann@gmail.com",
    packages=["test_package_id67"],
    description="A sample test package",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/eroell/test_package",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)
