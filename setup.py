from setuptools import setup, find_packages


setup(
    name="bstu_schedule",
    version="0.0.2",
    description="Open webpage with scedule of BSTU",
    license="MIT",
    url="https://github.com/Krai53n/bstu_schedule",
    author="Gregory Backhtin",
    author_email="bakhtin.g.a@gmail.com",
    install_requierements=[
        "selenium",
        "pyyaml",
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    #packages=[
        #"bstu_schedule",
        #"bstu_schedule.web",
        #"bstu_schedule.main",
        #"bstu_schedule.config",
        #"bstu_schedule.constans",
    #],
    packages=find_packages(),
    package_data={
        "": ["*.yaml", "*.exe"],
    },
    entry_points={
        "console_scripts": [
            "schedule = bstu_schedule.main:main",
        ]
    },
)
