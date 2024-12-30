import json
import argparse
from collections import Counter

parser=argparse.ArgumentParser(
    description='''Given a json data file and the high and low placements, return the deck types ordered by percentage used.''')
parser.add_argument('file', help='JSON data file to process')
parser.add_argument('high', type=int, help='highest placing')
parser.add_argument('low', type=int, help='lowest placing')
args=parser.parse_args()

def filter_placing(x):
    return x['placing'] <= args.low and x['placing'] >= args.high

def filter_decklist(x):
    return x['decklist'] != ""

def get_decktype(x):
    return x['decklist']['pokemon'][0]['name']

with open(args.file, 'r') as f:
    data = f.read()

parsed_data = json.loads(data)
filtered_data = list(map(get_decktype, filter(filter_decklist, filter(filter_placing, parsed_data))))

count = Counter(filtered_data)

for value, c in count.most_common():
    print("{: <30} {: >.2f}%".format(value, c / len(filtered_data) * 100))
