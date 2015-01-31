#!/bin/bash
#Copyright (C) 2007  Paul Sharrad

#This file is part of Karoshi Server.
#
#Karoshi Server is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Karoshi Server is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with Karoshi Server.  If not, see <http://www.gnu.org/licenses/>.

#
#The Karoshi Team can be contacted at: 
#mpsharrad@karoshi.org.uk
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk
############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
TIMEOUT=86400
fi
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Home Folders"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'



#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/home_folders.cgi" method="post"><div id="actionbox3"><div id="titlebox"><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>
<td style="vertical-align: top;"><div class="sectiontitle">'$"Home Folders"'</div></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Home_Folders"><img class="images" alt="" src="/images/help/info.png"><span>'$"This displays the server that hosts the home folders for each group."'</span></a></td><td><a href="gluster_control.cgi"><input class="button" type="button" style="min-width: 135px;" name="" value="'$"Gluster Volume Control"'"></a></td></tr></tbody></table><br></div><div id="infobox">
  <table class="standard" style="text-align: left; height: 91px;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: 140px;"><b>'$"Primary Group"'</b></td><td style="width: 180px;"><b>'$"Server"'</b></td><td style="width: 180px;"><b>'$"Change"'</b></td><td style="width: 140px;"><b>'$"Primary Group"'</b></td><td style="width: 180px;"><b>'$"Server"'</b></td><td><b>'$"Change"'</b></td></tr>
'
START_LINE=yes
ICON1=/images/submenus/system/computer.png
for PRI_GROUP in /opt/karoshi/server_network/group_information/*
do
PRI_GROUP=`basename $PRI_GROUP`
unset GLUSTERVOL
source /opt/karoshi/server_network/group_information/$PRI_GROUP

#Check for gluster volume
[ -z "$GLUSTERVOL" ] && GLUSTERVOL=notset
if [ -d /opt/karoshi/server_network/gluster-volumes/$GLUSTERVOL ]
then
	ICON1=/images/submenus/system/gluster.png
else
	ICON1=/images/submenus/system/computer.png
fi

if [ $START_LINE = yes ]
then
echo '<tr><td style="vertical-align: top;">'$PRI_GROUP'</td><td style="vertical-align: top;">'`echo $SERVER | sed 's/,/<br>/g'`'</td><td style="vertical-align: top;"><a class="info" href="javascript:void(0)"><input name="_PRIGROUP_'$PRI_GROUP'_SERVER_'$SERVER'_" type="image" class="images" src="'$ICON1'" value="_PRIGROUP_'$PRI_GROUP'_SERVER_'$SERVER'_"><span>'$"Change Server"'<br><br>'$PRI_GROUP'<br><br>'`echo $SERVER | sed 's/,/<br>/g'`'</span></a></td>'
START_LINE=no
else
echo '<td style="vertical-align: top;">'$PRI_GROUP'</td><td style="vertical-align: top;">'$SERVER'</td><td style="vertical-align: top;"><a class="info" href="javascript:void(0)"><input name="_PRIGROUP_'$PRI_GROUP'_SERVER_'$SERVER'_" type="image" class="images" src="'$ICON1'" value="_PRIGROUP_'$PRI_GROUP'_SERVER_'$SERVER'_"><span>'$"Change Server"'<br><br>'$PRI_GROUP'<br><br><br>'`echo $SERVER | sed 's/,/<br>/g'`'</span></a></td></tr>'
START_LINE=yes
fi
done

echo '</tbody>
  </table><br><br>
</div></div>
</form>
</div></body>
</html>'
exit

