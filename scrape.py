# Script to choose a scraper when given a URL for the fortforecast search engine

from argparse import ArgumentParser
import importlib
import sys
import re

sys.path.append("scrapers")

parser = ArgumentParser()

parser.add_argument("url", help="The URL to scrape from.")
parser.add_argument("-s",help="Treat the URL as a site and attempt to mirror it locally.")

arguments = parser.parse_args()

script_choices_file = open("script_choices.tsv")
script_choices = script_choices_file.readlines()

for line in script_choices:
    try:
        (regex, script_filename) = line.split("\t")
    except ValueError:
        print("Script choice '{}' has too many tabs in its line.".format(line))

    if re.search(regex, arguments.url):
        # Import script and run it with flags
        script = importlib.import_module(script_filename)
        script.main()
        quit()
    else:
        continue

script = importlib.import_module("generic")
script.main()
quit()
