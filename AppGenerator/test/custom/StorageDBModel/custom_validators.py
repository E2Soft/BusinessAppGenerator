

"""
	Created: 2015-03-27 19:32:07.553747
	
	@author: PCX
	
	EDIT THESE FUNCTIONS TO IMPLEMENT CUSTOM OPERATIONS
	FOR YOUR APPLICATION.
	
"""





from django.core.exceptions import ValidationError
def Drzava_nazivDrzava_validator(value):
	# if not valid:
	#	raise ValidationError('message')
	if 'kosovo' in value.lower():
		raise ValidationError('Kosovo nije drzava!!')
		