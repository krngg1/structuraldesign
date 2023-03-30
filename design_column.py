#!/usr/bin/env python
import cgi
import requests

print("Content-Type: text/html\n\n")
form = cgi.FieldStorage()

# Get input values from form
b = form.getvalue("b")
h = form.getvalue("h")
L = form.getvalue("L")
fck = form.getvalue("fck")
fy = form.getvalue("fy")
P = form.getvalue("P")
Zone_Factor = form.getvalue("Zone_Factor")
S_DS = form.getvalue("S_DS")
R = form.getvalue("R")

# Call your Python script on GitHub with input values
url = "https://raw.githubusercontent.com/krngg1/structuraldesign/main/column.py"
params = {
    "b": b,
    "h": h,
    "L": L,
    "fck": fck,
    "fy": fy,
    "P": P,
    "Zone_Factor": Zone_Factor,
    "S_DS": S_DS,
    "R": R
}
response = requests.get(url, params=params)

# Print the output from your Python script
print(response.text)
