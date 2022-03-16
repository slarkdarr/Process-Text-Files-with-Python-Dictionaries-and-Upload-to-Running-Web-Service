#! /usr/bin/env python3

import os
import requests

directory = '/data/feedback'                        # Directory of the feedback files

keys = ['title', 'name', 'date', 'feedback']        # List of keys
for filename in os.listdir(directory):
    infile = os.path.join(directory, filename)      # Filename appended with its directory

    # Read each line of the file
    with open(infile, 'r') as f:
        contents = f.readlines()

    feedback_dictionary = dict(zip(keys, contents))  # Assign each line to its respective key on the dictionary
    response = requests.post('http://34.132.141.97/feedback/', data=feedback_dictionary)     # Make POST request to the URL

    # Check out the response status
    print(response.status_code)
    print(response.request.url)
    print(response.request.body, end='\n\n')
