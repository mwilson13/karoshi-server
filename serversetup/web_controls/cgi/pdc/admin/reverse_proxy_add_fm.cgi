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

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

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
  <title>'$"Add Reverse Proxy"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
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

echo '</head>
<body onLoad="start()"><div id="pagecontainer">'

WIDTH1=180
WIDTH2=180
WIDTH3=250
SIZE1=20
SIZE2=40
TABLECLASS=standard
if [ $MOBILE = yes ]
then
	WIDTH1=180
	WIDTH2=90
	WIDTH3=300
	SIZE1=20
	SIZE2=30
	TABLECLASS=mobilestandard
fi

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox
fi

echo '<form action="/cgi-bin/admin/reverse_proxy_add.cgi" method="post">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"Add Reverse Proxy"'</span>
	<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
	</div></div><div id="mobileactionbox">
'
else
	echo '<div id="'$DIV_ID'"><div id=titlebox>'
fi

#Get reverse proxy server
PROXYSERVER=`sed -n 1,1p /opt/karoshi/server_network/reverseproxyserver | sed 's/ //g'`

echo '<table class="'$TABLECLASS'" style="text-align: left;" ><tr>'
[ $MOBILE = no ] && echo '<td style="width: '$WIDTH1'px; vertical-align: top;"><div class="sectiontitle">'$"Add Reverse Proxy"'</div></td>'
echo '<td style="vertical-align: top;">
<button class="button" formaction="reverse_proxy_view_fm.cgi" name="ViewReverseProxies" value="_">
'$"View Reverse Proxies"'
</button>
</td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Reverse_Proxy_Server#Adding_Reverse_Proxy_Entries"><img class="images" alt="" src="/images/help/info.png"><span>'$"The reverse proxy feature allows incoming web connections on port 80 and 443 to pass through the reverse proxy to other servers on your network."'<br><br>'$"This bypasses the need for sub domains and alias tcpip numbers for external access and will also allow all external ssl traffic to use one ssl certificate to authenticate the sites."'</span></a></td>
</tr></tbody></table><br>
  <br>
  <table class="'$TABLECLASS'" style="text-align: left;" >
    <tbody>
      <tr>
        <td style="width: '$WIDTH2'px;">
'$"Target folder"'</td>
        <td><input tabindex= "1" name="_TARGET_" size="'$SIZE1'" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Reverse_Proxy_Server#Adding_Reverse_Proxy_Entries"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the web folder that you want redirected. Leave blank to re-direct the top directory."'<br><br>'$"Example: Joomla is installed at http://www.mysite/joomla"'<br><br>'$"Target folder - joomla"'<br><br>'$"Destination - http://www.mysite"'</span></a>
      </td>
</tr>
      <tr>
        <td>
'$"Destination"'</td>
        <td><input tabindex= "2" name="_DESTINATION_" size="'$SIZE2'" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Reverse_Proxy_Server#Adding_Reverse_Proxy_Entries"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the web address that you want to redirect to."'<br><br>'$"Example: Joomla is installed at http://www.mysite/joomla"'<br><br>'$"Target folder - joomla"'<br><br>'$"Destination - http://www.mysite"'</span></a>
</td>
      </tr>
    </tbody>
  </table><br>
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div>'

[ $MOBILE = no ] && echo '</div>'

echo '</form>
</div></body>
</html>
'
exit
