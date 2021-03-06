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
HEIGHT=25
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
  <title>'$"Change Global Language"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/remote_management_change_global_language2.cgi" method="post"><div id="actionbox"><div class="sectiontitle">'$"Change Global Language"'</div>
  <br>
  <table class="standard" style="text-align: left;" >
    <tbody>
      <tr>
        <td style="width: 180px;">
'$"Language"'</td>
        <td>'


[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs

#Generate dropdown list of langauges
echo '<select name="___LANGCHOICE___" style="width: 185px; height: '$HEIGHT'px;"><option label="blank"></option>'
echo '<option value="ar_AE.UTF-8">العربية</option>
<option value="cs_CZ.UTF-8">Čeština</option>
<option value="da_DK.UTF-8">Dansk</option>
<option value="de_DE.UTF-8">Deutsch</option>
<option value="el_GR.UTF-8">Eλληνικά</option>
<option value="en_EN.UTF-8">English</option>
<option value="es_ES.UTF-8">Español</option>
<option value="fr_FR.UTF-8">Français</option>
<option value="hi_IN.UTF-8">हिन्द</option>
<option value="he_IL.UTF-8">עברית</option>
<option value="it_IT.UTF-8">Italiano</option>
<option value="ko_KO.UTF-8">한국어</option>
<option value="nb_NO.UTF-8">Bokmål</option>
<option value="nl_NL.UTF-8">Nederlands</option>
<option value="pl_PL.UTF-8">Polski</option>
<option value="pt_PT.UTF-8">Português</option>
<option value="ru_RU.UTF-8">Pусский</option>
<option value="sv_FI.UTF-8">Svenska</option>
<option value="zh_CN.UTF-8">语</option> ' | sed 's/"'$LANG'"/"'$LANG'" selected="selected" style="color:green"/g'

echo '</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the language that you want for the Web Management."'<br><br>'$"This will affect all general web management pages."'</span></a></td>
      </tr>
    </tbody>
  </table>
  <br>
</div>
<div id="submitbox">
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div>
</form>
</div></body>
</html>
'
exit
