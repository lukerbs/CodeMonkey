from setuptools import setup, find_packages

setup(
    name="scriptmonkey",
    version="2.0.1",
    description="A simple CLI utility for copying files and directory trees to clipboard for easy sharing with LLMs.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lukerbs/ScriptMonkey",
    author="Luke Kerbs",
    author_email="LDK.kerbs@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["rich", "pyperclip"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "scriptmonkey=scriptmonkey.core:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "clipboard",
        "file sharing",
        "directory tree",
        "development tools",
        "python tools",
        "LLM helper",
        "code sharing",
        "project structure",
        "file utility",
        "developer tools",
    ],
    include_package_data=True,
)
