#!/usr/bin/python

import sys
import webbrowser

google = "https://www.google.com.br/?gws_rd=cr&ei=IWfLUsnIMcrSsASoiYGIAQ#q="
youtube = "http://www.youtube.com/results?search_query="
url = ""

if sys.argv[1] == "google":
	url = google+sys.argv[2]
else:
	url = youtube+sys.argv[2]

webbrowser.open(url)
sys.exit()