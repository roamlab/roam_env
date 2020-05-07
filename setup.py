import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="roam_env",
    version="0.0.1",
    author="Gagan Khandate",
    author_email="gagank@cs.columbia.edu",
    description="ROAM Environment Inteface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/roamlab/roam_env",
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires = [
        'confac @ git+https://git@github.com/roamlab/confac#egg=confac',
    ]
)