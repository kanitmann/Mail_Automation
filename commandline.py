import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--recieverfile', type=str, required=True)
parser.add_argument('-f','--filepath', type=str, required=True)

args = parser.parse_args()

with open(args.recieverfile) as f:
    content = f.read().splitlines()
for line in content:
    os.system('ssmtp ' + line + ' < ' + args.filepath)

print('Mailed all recipients')