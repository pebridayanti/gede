#!/usr/bin/python

import shapefile

class Gede(object):
	def __init__(self,bandung):
		self.sf = shapefile.Reader(bandung)
		
	def selectTempat(self,Universitas Nurtanio):
		i =0 
		for a in self.sf.records():
				if a[1] == Universitas Nurtanio:
						return i
				i=i+1
				
	def __init__(self,Medan):
		self.sf = shapefile.Reader(Medan)
		
	def selectTempat(self, Masjid Raya):
		i =0
		for a in self.sf.records():
				if a[1] == Masjid Raya:
						return i
				i=i+1
				
	def __init__(self,Medan):
		self.sf = shapefile.Reader(Medan)
		
	def selectTempat(self, Lapangan Benteng):
		i =0
		for a in self.sf.records():
				if a[1] == Lapangan Benteng:
						return i
				i=i+1


	def __init__(self,Bandar Lampung):
		self.sf = shapefile.Reader(Bandar Lampung)
		
	def selectTempat(self, Mall Kartini):
		i =0
		for a in self.sf.records():
				if a[1] == Mall Kartini:
						return i
				i=i+1
				
	def __init__(self,Jakarta):
		self.sf = shapefile.Reader(Jakarta)
		
	def selectTempat(self, Dufan):
		i =0
		for a in self.sf.records():
				if a[1] == Dufan:
						return i
				i=i+1

