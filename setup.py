
from setuptools import setup, find_packages

setup(
    name='Calculating sma and rsi’,
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
    "tqdm",
    "six",
    "requests",
],
entry_points={
    'console_scripts': [
        'calculate_rsi = your_package_name.main:calculate_rsi_function',
    ],
},
    author=Muhammet Isa Bagci',
    description='Description of your package',
    url="https://github.com/mjbagci/Calculating-SMA-and-RSI/edit/main/setup.py"
)
