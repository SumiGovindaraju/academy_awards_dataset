import json
import os
import re
import csv

# source: https://stackoverflow.com/a/18262324
path = os.getcwd() + '/academy_awards'

with open('academy_awards.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Year', 'Award', 'Name 1', 'Name 2', 'Won'])

    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r') as f:
            match = re.search(r"^[0-9]*", filename)

            year = 1929 - 1 # year of first ceremony - 1
            
            if match:
                year += int(match.group(0))

            awards = json.load(f)

            for award in awards:
                for candidate in award['candidates']:
                    award_name = award['name'].strip()
                    nominee = candidate['target'][0].strip() if len(candidate['target']) == 1 else None
                    film = candidate['for'][0].strip() if len(candidate['for']) == 1 else None

                    writer.writerow([year, award_name, film, nominee, int(candidate['won'])])