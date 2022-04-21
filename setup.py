"""Package Setup File"""
import setuptools

#TODO: Fill in dependecies here
REQUIREMENTS = []

# Requirements for running unit tests
TEST_REQUIREMENTS = ["pytest", "pytest-cov"]

# Development requirements
EXTRAS_REQUIRE = {
    "dev": ["black", "pylint", "pre-commit"] + TEST_REQUIREMENTS,
}

def get_readme():
    """Returns contents of README.md."""
    try:
        with open("README.md", "r", encoding="utf-8") as readme_file:
            return readme_file.read()
    except OSError:
        return "Error: Cannot read from README.md!"

setuptools.setup(
    # Author info
    author="Lukas Koning",
    author_email="lfkoning@gmail.com",

    # Package info
    name="demo-project",
    version="0.0.1",

    description="Demo CLI om project aan te maken",
    long_description=get_readme(),
    keywords="demo, projectmap, cli",
    url="https://github.com/LFKoning/demo-project.git",

    # See: https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],

    # Dependency specifications
    install_requires=REQUIREMENTS,
    extras_require=EXTRAS_REQUIRE,
    tests_require=TEST_REQUIREMENTS,

    package_dir={"demo-project": "src/demo_project"},
    packages=setuptools.find_packages("src"),
    test_suite="tests",
    include_package_data=True,
    package_data={"demo-project": ["package_data/*"]},
    entry_points={"console_scripts": ["dqchecks = demo_project.cli:main"]},
)
