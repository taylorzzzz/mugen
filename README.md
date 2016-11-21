# mvgen

A music video generator based on beat patterns

Built with [essentia](https://github.com/MTG/essentia) and [moviepy](https://github.com/Zulko/moviepy)

## Installation

1 - [Install Miniconda](http://conda.pydata.org/miniconda.html) (A Python package manager)

2 - [Install Homebrew](http://brew.sh/) (General purpose package manager for mac)

3 - Create mvgen virtual environment

`conda env create -f environment.yml`

4 - Activate mvgen environment

`source activate mvgen`

5 - Make sure most recent version of Xcode is installed

6 - [Install Essentia](http://essentia.upf.edu/documentation/installing.html) For OS X Via Homebrew 

7 - Move Essentia package from Homebrew to your mvgen conda environment

`cp -r /usr/local/lib/python2.7/site-packages/essentia /Users/myuser/miniconda/envs/mvgen/lib/python2.7/site-packages/essentia`

8 - [Fix matplotlib](http://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python)

9 - Download [scherroman/moviepy](https://github.com/scherroman/moviepy) from github.

10 - Install moviepy into mvgen conda environment (from downloaded moviepy directory)

`(sudo) python setup.py install`

## Examples

