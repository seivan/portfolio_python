<!--
Takes id as a argument and calls on lookup_project() to return it
-->

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<link type="text/css" rel="stylesheet" href="style/style.css" />
<style type="text/css">
</style>
<meta name="description" content="Portfolio - TDP003" />
<meta name="keywords" content="Seivan Heidari, Johan Nordstrom, tdp003" />
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
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
<div id="page_header"> Project: ${project_id['project_name']} </div>
<br />
<div id="main">
<img src="${project_id['big_image']}" width="50"
height="50"></img>
<br /><b></b>${project_id['long_description']}<br />
<br /><b>Course ID : </b>${project_id['course_id']}
<br /><b>Course Name : </b>${project_id['course_name']}
<br /><b>Star Date : </b>${project_id['start_date']}
<br /><b>End Date : </b>${project_id['end_date']}
<br /><b>Group Size : </b>${project_id['group_size']}
<br /><b>Academic Credits : </b>${project_id['academic_credits']}
<br /><b>Project ID : </b>${project_id['project_no']}
<br /><b>Techniques used</b>
<p py:for="technique in project_id['techniques_used']">
${technique}
</p>
</div>
</div>
<div id="footer">
<p>Copyright &copy; Seivan Heidari and Johan Nordström - all rights reserved.
<br>By reading this fine print your soul is now the exclusive property of Heidari and Nordström.</br>
Unauthorized use of our shizzle, images, materials, souls, odors, and oxygen is strongly discouraged. We know where you sleep.
</p>
</div>
</body>
</html>
