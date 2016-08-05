import numpy as np
import pandas as p
import datetime as d
import glob as g
import os
from datetime import datetime as dd

inventory = None

class RowEntry(object):
	def __init__(self, row):
		self.data = row
		self.observer = row[0]
		self.date = row[2]
		self.time = row[3]
		self.etype = row[1]
		self.raw = row[4:]

	def rawparse(self):
		output = [np.nan, self.observer, self.date, self.time, self.etype]
		if self.etype == 'Session':
			if self.raw[0] == 'Teacher':
				output.append(1)
			elif self.raw[0] == 'Student':
				output.append(np.nan)
				output.append(1)
			else:
				output.append(np.nan)
				output.append(np.nan)
				output.append(1)
		print output

def main(x):
	os.chdir(x)
	for file in g.glob('*.csv'):
		data = p.read_csv(file, header=None)
		for row in data.values.tolist():
			entry = RowEntry(row)
			entry.rawparse()

main('C:\Users\sam\PyScripts\TabData')