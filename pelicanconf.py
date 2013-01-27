#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from pelican.plugins import related_posts, sitemap

AUTHOR = u'Frode Danielsen'
AUTHOR_EMAIL = u'frode@danielsen.net'
SITENAME = u'head-spinoff'
SITEURL = 'http://frode.danielsen.net/blog'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

PLUGINS = [related_posts, sitemap,]

# Blogroll
LINKS =  (('Thore, my dad', 'http://thore.no'),
          ('Ruben, my brother', 'http://rubendanielsen.com'),
          ('Stian, my colleague', 'http://blogg.prestholdt.no'),
          ('Eliksir, my company', 'http://e5r.no'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/fdanielsen'),
          ('Instagram', 'http://instagram.com/fdanielsen'),
          ('Facebook', 'http://facebook.com/FrodeDanielsen'),
          ('LinkedIn', 'http://no.linkedin.com/in/fdanielsen'),)

TWITTER_USERNAME = u'fdanielsen'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

THEME = u'notmyidea'

DISQUS_SITENAME = u'headspinoff'
GOOGLE_ANALYTICS = u'UA-38018419-2'

DEFAULT_PAGINATION = 10
