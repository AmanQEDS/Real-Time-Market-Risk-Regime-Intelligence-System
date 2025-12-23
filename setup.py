from __future__ import annotations
from typing import List
from pathlib import Path
from setuptools import setup, find_packages

HYPHEN_E_DOT = "-e ."

BASE_DIR = Path(__file__).parent


def get_requirements(file_path: str) -> List[str]:
    """
    Read requirements.txt and return a list of dependencies.
    Ignore empty lines, comments, and '-e .'
    """
    requirements = []

    with open(BASE_DIR / file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                requirements.append(line)

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


# Read README if available
readme_path = BASE_DIR / "README.md"
long_description = (
    readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
)


setup(
    name="Real Time Market Risk Regime Intelligence System",
    version="0.1.0",
    author="Aman",
    author_email="amankumarverma957@gmail.com",
    description="Real-Time Market Risk Monitoring and Regime Intelligence System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AmanQEDS/Real-Time-Market-Risk-Regime-Intelligence-System",
    packages=find_packages(exclude=("tests", "docs")),
    python_requires=">=3.9",
    install_requires=get_requirements("requirement.txt"),
    include_package_data=True,
    license="MIT",
)
