# -*- coding: utf-8 -*-
import re
import codecs
import sys

sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)
text=u'中华人民国共和国 福建省 人民 '
pattern=re.compile(ur'\w+',re.UNICODE)
match=pattern.findall(text)
for item in match:
	print item.decode('utf-8')
