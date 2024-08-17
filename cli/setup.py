from setuptools import setup, find_packages

setup(
    name='superfast-cli',  # Name of your CLI tool
    version='0.1.1',  # Version of your tool
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        'click>=8.0',  # Specify the Click version
    ],
    entry_points={
        'console_scripts': [
            'fast=your_cli_tool.cli:cli',  # Replace 'your_cli_tool.cli:cli' with your actual module and function
        ],
    },
    include_package_data=True,
    description='A CLI tool for generating project files',  # Short description of your CLI tool
    long_description=open('README.md').read(),  # Read the long description from README
    long_description_content_type='text/markdown',  # Specify the format of the long description
    author='Viktor',  # Your name
    author_email='limphanith.dev@example.com',  # Your email address
    # url='https://github.com/yourusername/your_repo',  # URL of your project repository
    license='MIT',  # License for your project
)
