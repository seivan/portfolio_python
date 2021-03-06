#! -*- coding: utf-8 -*- 		 
# Shows the stats of all techniques and links to the projects using them
import site
import kid
import os
import sys
import data

#path = os.path.dirname(__file__) 
#sys.path.append(path)
#kid.enable_import(path=path)    

def index():
    technique_stats = data.retrieve_technique_stats()[1]
    techniques = data.retrieve_techniques()[1]
    template = kid.Template(file=os.path.dirname(__file__) + os.sep + 'templates' + os.sep + 'techniques', technique_stats=technique_stats, techniques=techniques, cache=0) 
    template.cache = False
    site.cache = False
    return template.serialize(output='xhtml-strict')
