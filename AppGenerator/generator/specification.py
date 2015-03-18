'''
Created on Mar 13, 2015

@author: zeljko.bal
'''

from lxml import objectify

def from_xml_file(file_path):
    with open(file_path, 'r') as fileobject:
        return objectify.parse(fileobject).getroot()
    
def from_xml_string(xml):
    return objectify.fromstring(xml)
