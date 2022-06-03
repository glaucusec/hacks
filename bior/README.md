## BIOR
**bior** is a command line utility which uses **bionic-reading** api to convert a normal text file into Bionic Readable html or pdf file.

### Installation
``` 
git clone https://github.com/glaucusec/hacks.git

cd hacks

python3 main.py -h
```
- For the proper working of **BIOR** you need to get the api-key. [Click here](https://rapidapi.com/bionic-reading-bionic-reading-default/api/bionic-reading1/) and sign up for the api-key.
- Save the api-key into api.json file. 
- Now on you can have 500 requests/day.
### Usage
```
-h - show help
-f --file - read from file
-o --output - write to file
```
### Examples

Write to html file
```
python3 main.py -f file.txt -o output.html
```
Write to pdf file
```
python3 main.py -f file.txt -o output.pdf
```
If no output file is specified it prints the bionic readed text to terminal.


