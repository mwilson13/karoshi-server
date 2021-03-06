#!/bin/bash
#Copyright (C) 2007  Paul Sharrad
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#The Karoshi Team can be contacted at: 
#mpsharrad@karoshi.org.uk
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
DATE_INFO=`date +%F`
DAY=`echo $DATE_INFO | cut -d- -f3`
MONTH=`echo $DATE_INFO | cut -d- -f2`
YEAR=`echo $DATE_INFO | cut -d- -f1`

[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html>
<html><head>
  <title>'$"Student Internet Logs"'</title><META HTTP-EQUIV="refresh" CONTENT="300; URL=/cgi-bin/blank.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
<script language="JavaScript" src="/all/calendar2/calendar_eu.js"></script>
        <!-- Timestamp input popup (European Format) -->
<link rel="stylesheet" href="/all/calendar2/calendar.css">
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

if [ $MOBILE = yes ]
then
echo '<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
	<script src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: www.dynamicdrive.com
		* Visit Dynamic Drive at www.dynamicdrive.com for full source code
		***********************************************/
	</script>
	<script>
	// <![CDATA[
	var myMenu;
	window.onload = function() {
		myMenu = new SDMenu("my_menu");
		myMenu.init();
	};
	// ]]>
	</script>'
fi

echo '</head><body><div id="pagecontainer">'

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_staff
else
DIV_ID=actionbox2
fi

echo '<form action="/cgi-bin/staff/dg_view_student_user_logs.cgi" name="testform" method="post">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then

echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"User Internet Logs"'</span>
<a href="/cgi-bin/staff/mobile_menu.cgi">'$"Internet Menu"'</a>
</div></div><div id="mobileactionbox">
'
else
echo '<div id="'$DIV_ID'"><b>'$"Student Internet Logs"'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Internet logs are updated every three minutes."'</span></a>
<br><br>'
fi

if [ $MOBILE = yes ]
then
echo '<div id="suggestions"></div>
'$"Username"'<br>
<input tabindex= "3" style="width: 200px;" name="_USERNAME_" AUTOCOMPLETE = "off" size="14" type="text" id="inputString" onkeyup="lookup(this.value);"><br>
'$"Log Date"'<br>'

echo "
<!-- calendar attaches to existing form element -->
	<input type=\"text\" value=\"$DAY-$MONTH-$YEAR\" size=14 maxsize=10 name=\"_DATE_\" /></td><td style=\"vertical-align: top; text-align: center;\">
	<script language=\"JavaScript\">
	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': '_DATE_'
	});

	</script><br><br>
"

else
echo '<table class="standard" style="text-align: left;" >
	<tbody>
		<tr>
			<td style="width: 180px; height: 35px">
				'$"Username"'
			</td>
			<td>
				<div id="suggestions"></div>
				<input tabindex= "3" style="width: 200px;" name="_USERNAME_" AUTOCOMPLETE = "off" size="14" type="text" id="inputString" onkeyup="lookup(this.value);">
			</td>
			<td>
				<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the name of the student that you want to check the internet logs for."'</span></a>
			</td>
			<td colspan="1" rowspan="4" style="vertical-align: top;">
				<div id="photobox"><img alt="photo" src="/images/blank_user_image.jpg" width="140" height="180"></div>
			</td>
		</tr>'
echo '<tr><td style="vertical-align: top;">'$"Log Date"'</td><td style="vertical-align: top;">'
echo "<!-- calendar attaches to existing form element -->
	<input type=\"text\" value=\"$DAY-$MONTH-$YEAR\" size=14 name=\"_DATE_\"></td><td style=\"vertical-align: top; text-align: center;\">
	<script>
	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': '_DATE_'
	});

	</script></td></tr>
		<tr><td colspan="3">&nbsp;</td></tr>
		<tr><td colspan="3">&nbsp;</td></tr>
	</tbody>
</table>
<br>"
fi

if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
fi

echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></div></form></div></body></html>'
exit

########################
#Unique key
########################
#EXna_590_5SdCl8Pl1JpOIxgZ
