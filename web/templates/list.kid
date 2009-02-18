<!--
Lists a form for searching, search_fields and techniques
Loops over retrieve_projects (depending on parameters sent from search, search_fields and techniques)
All results are linked to project? and the id of project
-->

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<link type="text/css" rel="stylesheet" href="style/style.css" />
<style type="text/css">
</style>
<meta name="description" content="Portfolio - TDP003" />
<meta name="keywords" content="Seivan Heidari, Johan Nordström, tdp003" />
<title>Portfolio</title>
</head>
<body>
<div id="container">
<div id="menu">
<div id="menu_header">
TDP003
</div>
<div id="menuEntries">
<ul class="menuList">
<li class="menuEntry"> <a href="index.html">&raquo; <strong>Home</strong></a></li>
<li class="menuEntry"> <a href="list">&raquo; <strong>Projects</strong></a></li>
<li class="menuEntry"> <a href="techniques">&raquo; <strong>Techniques</strong></a></li>
<li class="menuEntry"> <a href="index.html">&raquo; <strong>About</strong></a></li>
<li class="menuEntry"> <a href="index.html">&raquo; <strong>Links</strong></a></li>
<li class="menuEntry"> <a href="index.html">&raquo; <strong>SVN</strong></a></li>
<li class="menuEntry"> <a href="index.html">&raquo; <strong>Contact</strong></a></li>
</ul>
</div>
</div>
<div id="page_header"> Projects : ${project_count}  </div>
<br />
<br />
<div id="main">
     <form action="list" method="get">
                          Search for:
                          <input type="text" name="search" value="" />
                          <select name="sort_by">
                              <option value="start_date">Sort By</option>
                          <option value="project_no">Projectnumber</option>
                          <option value="project_name">Projectname</option>
                          <option value="start_date">Startdate</option>
                          <option value="end_date">Enddate</option>
                          <option value="course_id">Course code</option>
                          <option value="course_name">Course Name</option>
                          <option value="academic_credits">Academic Creditsg</option>
                          <option value="short_description">Short Description</option>
                          <option value="long_description">Long Description</option>
                          <option value="group_size">Groupsize</option>
                        </select>
                          <br />
                          Order:
                          <input type="radio" name="sort_order" value="asc" checked="checked" />Ascending 
                          <input type="radio" name="sort_order" value="desc" />Descending
                          <br />
                          <input type="checkbox" name="search_fields" value="project_no" />Projectnumber
                          <input type="checkbox" name="search_fields" value="project_name" />Projectname
                          <input type="checkbox" name="search_fields" value="start_date" />Startdate
                          <input type="checkbox" name="search_fields" value="end_date" />Enddate
                          <input type="checkbox" name="search_fields" value="course_id" />Coursecode<br />
                          <input type="checkbox" name="search_fields" value="course_name" />Coursename
                          <input type="checkbox" name="search_fields" value="academic_credits" />Academic Credits
                          <input type="checkbox" name="search_fields" value="short_description" />Short Description
                          <input type="checkbox" name="search_fields" value="techniques_used"/>Techniques                          
			  <input type="checkbox" name="search_fields" value="long_description" />Long Description
                          
<br />
                          <input type="reset" name="none" value="Clear" />
                          <input type="submit" value="Search" />
    <select name="techniques" multiple="multiple" size="5">			    
<option py:for="tech in techniques" value="${tech}">${tech}</option></select>
<p py:for="project in projects">
<img src ="${project['small_image']}"
align ="left" width="25" height="25"/> 
<a href="project?id=${project['project_no']}">${project['start_date']} ${project['project_name']}<br />${project['short_description']}</a>
</p>
</form>
<br />
<br />
</div>
<div id="footer">
<p>Copyright &copy; Seivan Heidari and Johan Nordström - all rights reserved.
<br>By reading this fine print your soul is now the exclusive property of Heidari and Nordström.</br>
Unauthorized use of our shizzle, images, materials, souls, odors, and oxygen is strongly discouraged. We know where you sleep.
</p>
</div>
</div>
</body>
</html>
