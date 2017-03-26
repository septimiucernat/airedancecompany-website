#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'AIRE Dance Company'
SITENAME = 'AIRE Dance Company'
SITEURL = 'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = 'Art Inspired by Rhythm of Emotions'

PATH = 'content'

TIMEZONE = 'Europe/Bucharest'


#THEME = '/home/3pillar.corp/silvian.cretu/git/pelican-themes/twenty-html5up'

#THEME = '/home/3pillar.corp/silvian.cretu/git/pelican-themes/svbhack'
#USER_LOGO_URL = SITEURL + '/images/logo.png'
SITELOGO = '/images/logo.png'
FAVICON = '/images/favicon.ico'

#THEME = '/home/3pillar.corp/silvian.cretu/git/pelican-themes/hyde'

THEME = '/home/3pillar.corp/silvian.cretu/Documents/pelican/themes/Flex-2.1.0'

#THEME = '/home/3pillar.corp/silvian.cretu/git/pelican-themes/backdrop'
#PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

DEFAULT_LANG = 'ro'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('cursuri', 'https://airedancecompany.ro/category/cursuri.html'),
         ('orar', 'https://airedancecompany.ro/category/orar.html'),
         ('blog', 'https://airedancecompany.ro/category/blog.html'),
         ('contact', 'https://airedancecompany.ro/contacteaza-ne.html'),
         ('despre', 'https://airedancecompany.ro/despre-aire-dance-company.html'))

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/AireDanceCompany/'),
          ('linkedin', 'https://www.linkedin.com/company/aire-dance-company'),
          ('twitter', 'https://twitter.com/AIREDC'),
          ('rss', 'https://airedancecompany.ro/feeds/all.atom.xml'))

DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 1000

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

BROWSER_COLOR = '#ffffff'
PLUGIN_PATHS = ['/home/3pillar.corp/silvian.cretu/git/pelican-plugins']
PLUGINS = ['extended_sitemap', 'minification', 'representative_image', 'google_embed']
GMAPS_KEY = 'AIzaSyDKJRkX0kRwS5sHSC0hc4zzim9k0zHtSp0'

STATIC_PATHS = ['images']

EXTENDED_SITEMAP_PLUGIN = {
    'priorities': {
        'index': 1.0,
        'articles': 0.8,
        'pages': 0.5,
        'others': 0.4
    },
    'changefrequencies': {
        'index': 'daily',
        'articles': 'weekly',
        'pages': 'monthly',
        'others': 'monthly',
    }
}

GOOGLE_ANALYTICS = 'UA-93021614-1'

ADD_THIS_ID = 'ra-58b9e014323692f3'

ROBOTS = 'index, follow'

# PYGMENTS_STYLE = 'monokai'
#

#
# THEME = '../flex'
# PATH = 'content'
# TIMEZONE = 'America/New_York'
# DEFAULT_LANG = 'en'
# OG_LOCALE = 'en_US'
# LOCALE = 'en_US'
#
# DATE_FORMATS = {
#     'en': '%B %d, %Y',
# }
#
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None
#
# USE_FOLDER_AS_CATEGORY = False
# MAIN_MENU = True
#
# LINKS = (('Portfolio', 'http://alexandrevicenzi.com'),)
#

#
# MENUITEMS = (('Archives', '/archives.html'),
#              ('Categories', '/categories.html'),
#              ('Tags', '/tags.html'),)
#
# CC_LICENSE = {
#     'name': 'Creative Commons Attribution-ShareAlike',
#     'version': '4.0',
#     'slug': 'by-sa'
# }
#
# COPYRIGHT_YEAR = 2016
#
# DEFAULT_PAGINATION = 10
#
# PLUGIN_PATHS = ['./pelican-plugins']
#
# SITEMAP = {
#     'format': 'xml',
#     'priorities': {
#         'articles': 0.6,
#         'indexes': 0.6,
#         'pages': 0.5,
#     },
#     'changefreqs': {
#         'articles': 'monthly',
#         'indexes': 'daily',
#         'pages': 'monthly',
#     }
# }
#
# DISQUS_SITENAME = "alexandrevicenziblog"
#
# STATUSCAKE = {
#     'trackid': 'SL0UAgrsYP',
#     'days': 7,
#     'rumid': 6852,
#     'design': 6,
# }
#
#
# EXTRA_PATH_METADATA = {
#     'extra/custom.css': {'path': 'static/custom.css'},
# }
#
# CUSTOM_CSS = 'static/custom.css'
#
# USE_LESS = True
