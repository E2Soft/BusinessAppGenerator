

"""
	Created: 2015-03-27 19:32:07.562748
	
	@author: PCX
	
	EDIT THESE FUNCTIONS TO IMPLEMENT CUSTOM OPERATIONS
	FOR YOUR APPLICATION.
	
"""






def calculate_Kategorija_broj_artikala(obj):
	# return the calculated value to be presented in the view, the value will be calculated each time the object is presented
	# object type is Kategorija, field type is Integer
	return len(obj.artikal_set.all())