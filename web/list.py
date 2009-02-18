#! -*- coding: utf-8 -*- 		 
# /list page for portfolio 
# shows all projects within portfolio
# and lets the user search for projects and sort them

import site
import kid
import os
import sys
import data
import operator
from operator import itemgetter
path = os.path.dirname(__file__)
sys.path.append(path)
kid.enable_import(path=path)    


def index(sort_by='start_date', sort_order='asc', techniques=None, search=None, search_fields=None):
    '''
    Save results of functions from our data module into variables 
    and send it to our kid template 
    '''

    project_count = data.project_count()[1]
    projects = data.retrieve_projects(sort_by, sort_order, techniques, search, search_fields)[1]
    techniques = data.retrieve_techniques()[1]
    template = kid.Template(file=os.path.dirname(__file__) + os.sep + 'templates' + os.sep + 'list', cache=0, projects=projects, project_count=project_count, techniques=techniques, cache=0) 
    template.cache = False
    site.cache = False
    return template.serialize(output='xhtml-strict')
