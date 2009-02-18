#!/usr/bin/env python			 
#! -*- coding: utf-8 -*- 		 
# Data  Module for Portfolio 		 
# by Seivan Heidari and Johan Nordström 
##########################################

import csv
from operator import itemgetter
import sys
from time import strftime
import os

# All constants used within module is defined here.
#year-month-day hour:minutes:seconds - eg: 08-10-10 23:32:56
current_time=str(strftime("%y-%m-%d %H:%M:%S"))
#Error Codes
csv_not_found = 1
project_not_found = 2
works_ok = 0
#Directories
logfile= os.path.dirname(__file__) + os.sep +'log.txt'
csvfile=  os.path.dirname(__file__) + os.sep +'data.csv'

def log(msg):
        '''
	name:		log \n
	parameter:	msg(string): the message to write down. \n
	description:	Writes all function calls and their errorcodes to logfile definied with current time. \n
        '''
        log = open(logfile, 'a')
        log.write(current_time + msg +'\n')
        log.close()
      	

def init():
        '''
	name:		init \n
	description: 	Reads a csv file and parse all values to unicode and store within a global variable. If a exception is caught, errorcode is outputted and written to log \n 		
	'''
	#Making projects (the input from data.csv) into global so it can be accessed by the other functions
	#init() is called in every local function and then using project to access the data
        global projects
        projects = []

        try:
                in_file = open(csvfile, "r")

        except:  
                log(': init() was called, CSV file not found! \n')
                return csv_not_found
	

        else:
                in_file = open(csvfile, 'r')
                in_file_csv = csv.DictReader(in_file)

                # Convert every value in project dictionary to unicode
		for row in in_file_csv: 
                        projects.append(dict((k,v.decode("utf8")) for k,v in row.iteritems()))

		# Make the techniques field to a list
                for project in projects: 
                        project['techniques_used'] = project['techniques_used'].rsplit(',')

        # If no exceptions was caught write log and return OK
        log(': init() was called, Function returned OK!')
        return works_ok

def project_count():        
	'''
	name:		project_count \n
	description: 	Returns the amount of projects and returns errorcode if csv is not found. \n
	'''
	init()

	if len(projects) <= 0 or projects == (csv_not_found, None) : 
		log(': project_count() was called, CSV file not found!') 
		return (csv_not_found, None)
    
	else: 
		log(': project_count() was called, Function returned OK!')
		return (works_ok, len(projects))

def lookup_project(id):
	'''
	name:		lookup_project \n
	parameter: 	id(integer): the project ID, given from data.csv file or init() \n
	description: 	Returns the a project with specified id as a dictionary \n
	'''
	init()

	if id >= 0 and id < len(projects): 
		log(': project_count() was called, Function returned OK!')
		return (works_ok, projects[id])
    
	elif id>=len(projects):
		log(': project_count() was called, Project not found!')
		return (project_not_found, None)

def retrieve_projects(sort_by='start_date', sort_order='asc', techniques=None, search=None, search_fields=None):
	'''
	name:		retrieve_projects \n
	parameter: 	sort_by(string): sorting depending on the keyvalue from projects, default is 'start_date' \n
	parameter: 	sort_order(string): the sort order, normal if asc, reversed if desc, default is asc. \n
	parameter: 	techniques(list): searching techniques within each project, default is None \n
	parameter: 	search(string): free text search, searches through projects, default is None \n
	parameter: 	search_fields(list): defines what key keyvalue from projects to search through \n
	description: 	This function search for projects depending on what you search for and which search_fields you define to search on. The user can filter which project to show depending on which techniques they used. The output can be choosed to be sorted by user field-wise (sort_by) and either in falling or reverse order. \n
	'''
	
	# When techniques or search_fields is sent in as a string we convert it to a list so it can be iterated on
	if type(search_fields) == type('str'):
        	search_fields = [search_fields]

        if type(techniques) == type('str'):
        	techniques = [techniques]

	init()

	projects_to_search = []
	projects_matching = []

	# When user defines to filter on techniques we'll save all matches, which we'll iterate on when we search
	# If he doesnt choose to filter on techniques we'll iterate on all projects
	if techniques:
    		for project in projects:
        		project_matches = False

       	 		for technique in techniques:
        			if str(technique).lower() in str(project['techniques_used']).lower():
                			project_matches = True
            
        		if project_matches:
        			projects_to_search.append(project)
 	else:
		projects_to_search = projects

	# Search in the projects filtered for the search term and through search_fields
	# If searching isnt defined, return the projects filtered.
	if search:

		for project in projects_to_search:
			project_matches = False

			if search_fields:
        			for field in search_fields:
                    			if unicode(str(search).lower(), 'utf-8') in str(project[field]).lower():
                        			project_matches = True

			else:
        			for value in project.itervalues():
                			if unicode(str(search).lower(), 'utf-8') in str(value).lower():
                				project_matches = True

			if project_matches:
                		projects_matching.append(project)

	else:
		projects_matching = projects_to_search

	
	# Sort all projects that matched in either falling or reversed order and sort on
	# the field user choosed to sort on.
	if sort_order == 'asc':
	        projects_matching = sorted(projects_matching, key=itemgetter(sort_by))
		log(': retrieve_projects() was called, Function returned OK!')
		return (works_ok, projects_matching)    
    
	elif sort_order ==  'desc':
		projects_matching = sorted(projects_matching, reverse=True, key=itemgetter(sort_by))
		log(current_time + ': retrieve_projects() was called, Function returned OK!')
		print "10"
		return (works_ok, projects_matching) 
    
	else:
		log(': retrieve_projects() was called, Project not found!')
		return (project_not_found, None) 


def retrieve_techniques():
	'''
	name:		retrieve_techniques \n
	description: 	Returns techniques used within all projects \n
	'''
	init()

	techniques = []
	project_list = []
	project_list = projects
	
	# Iterate over all projects and save techniques
	for project in projects:
		for technique in project['techniques_used']:
			if techniques.count(technique.lower()) == 0:
				techniques.append(technique.lower())
	return (works_ok, sorted(techniques))
    
	# Log any exceptions
	if techniques == []:
		log(': retrieve_techniques() was called,Project not found!')
		return (project_not_found, None) # Return error code and list as a tuple, 0 = file not found
	else:
		log(': retrieve_techniques() was called, Function returned OK!')
		return (works_ok, techniques) # 1 = Everything is ok



def retrieve_technique_stats():
    '''
    name:		retrieve_techniques_stats \n
    description: 	Returns all techniques and how many times theyre being used and which projects are using them. The result is presented as a dictionary with a list of the projects using the technique. \n
    '''	   
    init()

    tech_stats = []
    
    for technique in retrieve_techniques()[1]:
        used_by = []
        usage_count = 0

        for project in projects:
            if technique in [tech.lower() for tech in project['techniques_used']]:
                used_by.append({'id': project['project_no'], 'name': project['project_name']})
                usage_count += 1
    
        tech_stats.append({'name': technique, 'count': usage_count, 'projects': used_by})
	tech_stats = sorted(tech_stats, key=itemgetter('name'))
    log(': retrieve_technique_stats() was called, Function returned OK!')
    return (works_ok, tech_stats)
	
projects = []
init()

