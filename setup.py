import io
import os

from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

setup(
    name="SSD1306",
    version="1.6.3",
    description="Python library to use SSD1306-based 128x64 pixel OLED displays with a Raspberry Pi.",
    long_description=long_description,
    packages=find_packages(),
    author="Joshua Arulsamy",
    install_requires=["Adafruit-GPIO>=0.6.5"],
    author_email="joshua.gf.arul@gmail.com",
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Development Status :: 4 - Beta",
        # Define that your audience are developers
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    url="https://github.com/jarulsamy/SSD1306/",
    dependency_links=[
        "https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.6.5"
    ],
)
