import setuptools

setuptools.setup(
    name='listify',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
