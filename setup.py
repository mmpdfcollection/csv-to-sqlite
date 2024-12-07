from setuptools import setup, find_packages

setup(
    name="csv-to-sqlite",  # Unique name for your library on PyPI
    version="1.0.0",  # Start with 1.0.0 and increment for updates
    description="A library for importing CSV files into SQLite databases with optional GUI support",
    long_description=open("README.md").read(),  # Add a detailed README.md file
    long_description_content_type="text/markdown",  # Specify Markdown format for README
    author="MMPDF Collection",
    author_email="mmpdfcollection@gmail.com",
    url="https://github.com/mmpdfcollection/csv-to-sqlite.git",  # GitHub repository URL
    packages=find_packages(),  # Automatically find all Python packages in your project
    include_package_data=True,  # Include files specified in MANIFEST.in
    install_requires=[  # Remove tkinter if it's included by default
        # "tkinter",  # Uncomment if tkinter is not installed by default on certain systems
    ],
    classifiers=[  # Add classifiers to specify package details for PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify minimum Python version
    entry_points={  # If you have CLI commands for your library
        "console_scripts": [
            "csv-to-sqlite-gui=csv_to_sqlite.gui:run_gui",  # CLI command to run GUI
        ],
    },
)
