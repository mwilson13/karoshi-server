#!/bin/bash
#Copyright (C) 2010  Paul Sharrad

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

##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"UPS Status"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'


function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/ups_add_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
	export MESSAGE=$"You must access this page via https."
	show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox">
<table class="standard" style="text-align: left;" ><tbody>
<tr>
<td style="vertical-align: top;"><div class="sectiontitle">'$"UPS Status"'</div></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=UPS_Status"><img class="images" alt="" src="/images/help/info.png"><span>'$"This shows the status of your ups devices."'</span></a></td>
<td style="vertical-align: top;">
<form action="ups_add_fm.cgi" method="post">
<button class="button" name="_AddUPS" value="_">
'$"Add a UPS"'
</button>
</form>
</td>
<td style="vertical-align: top;">
<form action="ups_slave_add_fm.cgi" method="post">
<button class="button" name="_AddSlaveUPS" value="_">
'$"Add a slave UPS"'
</button>
</form>
</td>
<td style="vertical-align: top;">
<form action="ups_device_add_fm.cgi" method="post">
<button class="button" name="_AddDevice" value="_">
'$"Add a device"'
</button>
</form>
</td>
</tr></table>
<br>'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/ups_status.cgi | cut -d' ' -f1`
#Show UPS status
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:" | sudo -H /opt/karoshi/web_controls/exec/ups_status
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 106 ]
then
	echo $"No UPS devices have been added."
fi
echo '</div></div></body></html>'
exit
