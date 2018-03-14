#encoding: UTF-8
import re

pattern = re.compile(r'world')

match = pattern.search('hello world! this is own world')

if match:
	print match.group()
