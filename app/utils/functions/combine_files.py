"""Contains function to combine all JSON batches from one day into one file."""
import os
import json
from app.utils.constants import constants

def combine_files():
    """Combines all JSON files from one day into one file."""
    directory = input('Please enter the directory within'
                        ' the output directory where the files are located:')
    files = os.listdir(os.path.join(constants.OUTPUT_DIRECTORY,directory))
    combined = []
    for file in files:
        with open(os.path.join(constants.OUTPUT_DIRECTORY,directory,file),
                    'r',encoding='utf-8') as f:
            data = json.load(f)
            combined.extend(data)
    with open(os.path.join(constants.OUTPUT_DIRECTORY,directory,'combined.json'),
                'w+',encoding='utf-8') as f:
        f.write(json.dumps(combined))
        f.close()
