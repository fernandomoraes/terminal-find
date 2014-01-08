#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cmd
import webbrowser as browser

class WebFinder(cmd.Cmd):
	"""Faster way to search the web."""

	def do_google(self, line):
		print "google searching..."
		Providers().search_google(line)
		return True

	def do_twitter(self, line):
		print "twitter searching..."
		Providers().search_twitter(line)
		return True

	def do_youtube(self, line):
		print "youtube searching..."
		Providers().search_youtube(line)
		return True

	def do_eof(self, line):
		return True

class Providers():
	GOOGLE = "https://www.google.com/?gws_rd=cr&ei=IWfLUsnIMcrSsASoiYGIAQ#q="
	TWITTER = "https://twitter.com/search?q="
	YOUTUBE = "http://www.youtube.com/results?search_query="

	def search_google(self, search):
		browser.open(Providers().GOOGLE+search)

	def search_twitter(self, search):
		browser.open(Providers().TWITTER+search)

	def search_youtube(self, search):
		browser.open(Providers().YOUTUBE+search)

if __name__ == '__main__':
	WebFinder().cmdloop()
