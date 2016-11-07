#-*-coding:utf-8-*-

def format_name(s):
	return s[0].upper() + s[1:].lower()

print map(format_name,['adam','LISA','barT'])
