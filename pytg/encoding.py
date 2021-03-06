# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'luckydonald'
import sys

if sys.version < '3': # python 2.7
	text_type = unicode
	binary_type = str
	native_type = binary_type
	long_int = long
	def to_native(x):
		return to_binary(x)
else: # python 3
	text_type = str
	binary_type = bytes
	native_type = text_type
	long_int = int
	def to_native(x):
		return to_unicode(x)


def to_binary(x, force=False):
	if isinstance(x, text_type):
		return x.encode("utf-8")
	elif isinstance(x, binary_type):
		return x
	else:
		return to_binary(str(x))


def to_unicode(x):
	if isinstance(x, binary_type):
		if x == b'\\':
			return u"\\"
		return x.decode("utf-8")
	elif isinstance(x, text_type):
		return x
	else:
		return to_unicode(str(x))

