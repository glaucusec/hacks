import requests
import urllib.parse
import argparse, json
from bs4 import BeautifulSoup
import pdfkit, sys

def find_api():
    f = open("api.json")
    data = json.load(f)
    global api_key 
    api_key = data['key']

def read_from_file(read_file_name):
    f = open(str(read_file_name), "r")
    content = f.read()
    f.close()
    return content

def output_as_html(content, filename):
    content = send_request(content)
    soup = BeautifulSoup(content, 'html.parser')
    pretty_content = soup.prettify()
    try:
        f = open(filename + ".html", 'w')
        f.write(pretty_content)
    finally:
        f.close()

def output_as_pdf(content, filename):
    content = send_request(content)
    pdfkit.from_string(content, str(filename) + ".pdf")
    
def send_request(content):
    global api_key
    url = "https://bionic-reading1.p.rapidapi.com/convert"
    body = urllib.parse.urlencode({
        "content":str(content),
        "response_type":"html",
        "request_type":"html",
        "fixation": "1",
        "saccade": "10"
    })
    header = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Host":"bionic-reading1.p.rapidapi.com",
        "X-RapidAPI-Key": api_key
    }
    rqst = requests.request("POST", url, data=body, headers=header)
    return rqst.text


find_api()

parser = argparse.ArgumentParser(
    description="Convert the text to bionic readable.",
)
parser.add_argument("-f", "--file", type=str, help="Read from file")
parser.add_argument("-o", "--output", type=str, help="Write the reponse to file")
args = parser.parse_args()

if args.file:
    content = read_from_file(args.file)
    return_text = send_request(content)
    if not args.output:
        print(return_text)
    
if args.output:
    if args.output:
        name = args.output.split(".")
        if len(name) != 2:
            sys.exit("Incorret output file format.\n (eg: file.html, file.pdf)")
        else:
            if name[1] == "html":
                output_as_html(content, name[0])
            elif name[1] == "pdf":
                output_as_pdf(content, name[0])
