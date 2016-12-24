# Generic scraper for FortForecast search engine

import subprocess
import os

def main(url, site=False):
    """Scrape a document or website.

    - url: The url to scrape from.
    - site: Whether to treat the url as a standalone document or an entire 
    website to mirror."""
    domain = url.split("//")[1].split("/")[0]
    if site:
        wget = subprocess.Popen("wget --mirror --limit-rate=256k --domains={} {}".format(domain, url))
        wget.wait()
        return True
    else:
        try:
            os.mkdir(domain)
        except FileExistsError:
            pass
        os.chdir(domain)
        wget = subprocess.Popen("wget -N {}".format(url))
        wget.wait()
        return True
