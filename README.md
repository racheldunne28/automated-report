# Example automated report

This repo contains the minimum code needed to produce an automated pdf report containing stats and figures.

To generate an example report:
1. Install pdflatex on your laptop
1. Clone this repo
1. Put a figure called example_figure.pdf in the figures folder (in reality you would probably generate this using code)
1. Set up and activate a virtual environment in the folder for this repo using [these instructions](https://realpython.com/python-virtual-environments-a-primer/).
1. Make sure you are in the main directory for the repo then run ```pip3 install -r requirements.txt``` in the command line
1. Run ```python3 report_example.py``` in the command line
1. Find the example report in the outputs folder.
