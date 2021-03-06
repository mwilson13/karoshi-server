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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Bulk User Creation - View Passwords"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/bulk_user_creation_view_passwords.cgi" method="post"><div id="actionbox">

<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: top;"><b>'$"Bulk User Creation - View Passwords"'</b></td>
<td style="vertical-align: top;">
<button class="button" formaction="bulk_user_creation_upload_fm.cgi" name="BulkUserCreation" value="_">
'$"Bulk User Creation"'
</button>
</td>
<td style="vertical-align: top;">
<button class="button" formaction="bulk_user_creation_import_enrollment_numbers_fm.cgi" name="ImportEnrolmentNumbers" value="_">
'$"Import enrolment numbers"'
</button>
</td></tr>
</tbody></table><br>
'$"View the new passwords for a group of users."'<br>
  <br>
  <table class="standard" style="text-align: left;">
    <tbody>
      <tr>
        <td style="width: 180px;">'$"Primary Group"'</td>
        <td>'
/opt/karoshi/web_controls/group_dropdown_list
echo '
        </td>
      </tr>
    </tbody>
  </table>
</div>
<div id="submitbox">
  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div>
</form>
</div></body>
</html>
'
exit
