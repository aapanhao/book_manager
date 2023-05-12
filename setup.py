import setuptools  # type: ignore

setuptools.setup(
    name="book_manager",
    version="1.0.0",
    packages=setuptools.find_packages(),
    package_data={
        'NAME': ['*.pyi'],
    },
)
