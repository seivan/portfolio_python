<!--
Contains a list of all techniques used and parses retrieve_techniques()
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
<div id="page_header"> Techniques : ${len(techniques)} </div>
<div id="main">
<div py:for="technique in technique_stats">
<div id="headline"> ${technique['name']}, count: ${technique['count']}.</div>
<div py:for="project in technique['projects']">
<div id="content"><a href="project?id=${project['id']}">${project['name']}</a></div>
</div></div>
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
