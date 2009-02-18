#! -*- coding: utf-8 -*- 		 
# Returns a project with specified id 
# Whenever exceptions is caught the user is redirected to a page telling a error has occured.
import site
import kid
import os
import sys
import data
path = os.getcwd() + "/" 
sys.path.append(path)
kid.enable_import(path=path)    

def index(id):
    try:
        id = int(id)
    except ValueError:
        pass        
    project = data.lookup_project(id)[1]
    if project is not None:
        template = kid.Template(file=os.path.dirname(__file__) + os.sep + 'templates' + os.sep + 'project',project_id=project)

    else:
        template = kid.Template(file=os.path.dirname(__file__) + os.sep + 'templates' + os.sep + 'error',project_id=project)
    template.cache = False
    site.cache = False
    return template.serialize(output='xhtml-strict')
