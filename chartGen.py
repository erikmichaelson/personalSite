import matplotlib.pyplot as plt

def saveChart(skillDict):
	fig, ax = plt.subplots()
	ax.bar(*zip(*skillDict[1].items()))
	ax.set_ylim([0,10])
	plt.savefig(f'{skillDict[0]}.svg')

languages = {'java':8, 'python':8, 'C':6, 'Assembly':5, 'JavaScript':4}
frameworks = {'React':4, 'PHP':8, 'C':6, 'Assembly':5, 'JavaScript':4}
data = {'Pandas':6, 'Stata':5, 'Julia':4, 'SQL':5, 'JavaScript':4}
skills = [('langs', languages), ('frmwks', frameworks), ('data', data)]
for s in skills:
	saveChart(s)
