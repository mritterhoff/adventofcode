import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pdb

import pprint

f = [x for x in open("in.txt").read().strip().split('\n')]


print(f)

peeps = []
scores = []
for l in f:
	s = [ x for x in l.split(' ') if len(x) > 0 and x != '(AoC++)']
	s.pop(0)
	peeps.append(' '.join(s[2:]))
	scores.append(int(s[0]))

pprint.pp(list(zip(peeps, scores)))


plt.style.use('ggplot')



y_pos = np.arange(len(peeps))
# pdb.set_trace()

ax = plt.gca()
ax.set_ylim([min(scores), max(scores)])

plt.bar(y_pos, scores, align='center', alpha=0.5)
plt.xticks(y_pos, peeps, rotation=90)
plt.title('Ranks')
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.2)

plt.show()