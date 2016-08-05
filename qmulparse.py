import numpy as np
import pandas as p
import datetime as d
import glob as g
import os
from datetime import datetime as dd

inventory = None
header = ['School', 'Observer', 'Date', 'Time', 'Teacher', 'Student', 'Teaching', 'Masking', 'RaisingVoice', 'Noise', 'NoiseSource', 'Learning', 'Distracted', 'Internal/External', 'ReasonForDistraction']

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
				output.append(np.nan)
				output.append(np.nan)
				output.append(np.nan)
				output.append(1)
		elif self.etype == 'Teacher':
			output.append(1)
			output.append(np.nan)
			if self.raw[0] == 'Teaching':
				output.append(1)
			elif self.raw[0] == 'Masking':
				output.append(np.nan)
				output.append(1)
			elif self.raw[0] == 'Raising Voice':
				output.append(np.nan)
				output.append(np.nan)
				output.append(1)
		elif self.etype == 'Student':
			output.append(np.nan)
			output.append(1)
			output.append(np.nan)
			output.append(np.nan)
			output.append(np.nan)
			output.append(np.nan)
			output.append(np.nan)
			if self.raw[1] == 'Learning':
				output.append(1)
			elif self.raw[1] == 'Distracted':
				output.append(np.nan)
				output.append(1)
				output.append(self.raw[2])
		print output

def main(x):
	os.chdir(x)
	for file in g.glob('*.csv'):
		data = p.read_csv(file, header=None)
		for row in data.values.tolist():
			entry = RowEntry(row)
			entry.rawparse()

main('C:\Users\Scott\Documents\GitHub\ACRP\TabData')