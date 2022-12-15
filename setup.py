from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent

setup(
    name='mkdocs-exclude-tagged-files',
    version='1.0.1',
    packages=['mkdocs_exclude_tagged_files'],
    url='https://github.com/k4ds3/mkdocs-exclude-tagged-files',
    license='MIT',
    author='Jonas Lorenz <jonas@jonasdoesthings.com>',
    author_email='jonas@jonasdoesthings.com',
    description='A mkdocs plugin that excludes files based on a list of frontmatter tags from being included in the final mkdocs output.',
    long_description=(this_directory / "README.md").read_text(),
    long_description_content_type='text/markdown',
    keywords=['mkdocs', 'mkdocs-plugin'],
    install_requires=['mkdocs'],

    entry_points={
        'mkdocs.plugins': [
            'mkdocs_exclude_tagged_files = mkdocs_exclude_tagged_files.plugin:ExcludeTaggedFilesPlugin',
        ]
    },
)
