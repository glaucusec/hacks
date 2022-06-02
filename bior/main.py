import requests
import urllib.parse
import argparse, json


def find_api():
    f = open("api_key.json")
    data = json.load(f)
    global api_key 
    api_key = data['key']

def read_from_file(read_file_name):
    f = open(str(read_file_name), "r")
    content = f.read()
    f.close()
    return content
    
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
        if name[1] == "html":
            print("html")
        elif name[1] == "pdf":
            print("pdf")
    # write_file_name = args.output
    # print(write_file_name)
