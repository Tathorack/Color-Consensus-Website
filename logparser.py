#!/usr/bin/env python3
#coding=UTF-8
import argparse
import csv
import re


import imagecolor
import PIL

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source', help='Source log file to parse: Default ./flask.log', default='./flask.log', required=False)
parser.add_argument('-o', '--output', help='Output csv file: Default ./colors.csv', default='./colors.csv', required=False)
parser.add_argument('-i', '--image', help='Output image file: Default ./lines.png', default='./lines.png', required=False)
args = parser.parse_args()

results = []
with open(args.source, 'r') as logfile:
    for line in logfile:
        try:
            if re.search('search:', line):
                line = line.split('search:')[1]
                search = line.split('R:')[0].strip()
                red = int(line.split('R:')[1].split('G:')[0].strip())
                green = int(line.split('G:')[1].split('B:')[0].strip())
                blue = int(line.split('B:')[1].split('HEX:')[0].strip())
                results.append({'name':search, 'red':red, 'green':green, 'blue':blue})
        except Exception as e:
            print(e)
imagecolor.results_save_csv(results, args.output)
im = imagecolor.results_line(results)
im.save(args.image)
