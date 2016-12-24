# Index a scraped site by recreating URL structure from wget tree and inserting into DB

from argparse import ArgumentParser
from urllib import request
from bs4 import BeautifulSoup
import os
import re

parser = ArgumentParser()

parser.add_argument("domain", help="The domain to construct URL's against.")
parser.add_argument("directory", help="Path to the scraped directory to index.")


arguments = parser.parse_args()

def url_gen(base_url, path):
    """Takes a base url and generates a list of URLs for files on a scraped site by 
    reading the structure and appending it.

    base_url: The websites domain.

    path: Absolute path to the scraped directory to index."""
    file_listing = os.listdir(path)
    files = []
    directories = []
    for filename in file_listing:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            directories.append(filename)
        elif os.path.isfile(filepath):
            files.append(filepath)
        else:
            raise Exception
    # Generate the full list of URL's by recursion
    for directory in directories:
        new_base_url = os.path.join(base_url, directory)
        new_path = os.path.join(path, directory)
        files += url_gen(new_base_url, new_path)
    return files

def index(path, base_url, database_url):
    """Take a path and the database URL, construct the information needed to input
    pages into full text search, then insert it into the database.

    path - Path to the scraped directory to index.

    base_url - The domain to construct url's against.

    database_url - The database to connect to for data insertion."""
    retrieval_date = os.stat(path).st_mtime
    files = url_gen(base_url, path)
    documents = []
    for filepath in files:

        document_file = open(filepath)
        try:
            document_html = document_file.read()
        except UnicodeDecodeError:
            document_file.close()
            document_file = open(filepath, encoding="latin-1")
            document_html = document_file.read()
        document_soup = BeautifulSoup(document_html, "html.parser")
        document_text = ""
        for paragraph in document_soup.find_all("p"):
            try:
                paragraph_text = paragraph.string
                # THIS DOES NOT SANITIZE THE HTML, JUST MAKES IT READABLE
                # SANITIZATION HAPPENS AT INFORMATION RETRIEVAL
                # ASSUME EVERYTHING IN THE DATABASE IS MALICOUS
                paragraph_clean = re.sub('<[^<]+?>', '', paragraph_text)
                document_text += (paragraph_clean + "\n")
            except TypeError:
                continue
        document = {}
        document["url"] = filepath.replace("index.html", "")
        document["site"] = base_url
        document["retrieval_date"] = retrieval_date
        document["creation_date"] = os.stat(filepath).st_mtime
        try:
            document["title"] = document_soup.title.contents[0].strip("\n")
        except AttributeError:
            document["title"] = ""
        document["text"] = document_text

        documents.append(document)
    print(documents[-1])
            
index(arguments.directory, arguments.domain, None)
