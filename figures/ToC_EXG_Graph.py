fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8,6))

variants = ['39D66H', '43D66H', '61D66H']
for variant in variants:
    pH, yb = np.loadtxt('../data/titration_curves_{}.dat'.format(variant), unpack=True, usecols=(0,1), skiprows=2)
    ax.plot(pH, yb, marker='o', linestyle='dashed', linewidth=3, markersize=10)

# Axis limits
ax.set_xlim(2, 9.6)
ax.set_ylim(0, 1.07)

# Axis Labels
ax.text(5.1, -0.1, 'pH', fontsize=22)
ax.set_ylabel('Fraction of H⁺ Dissociation', fontsize=22, labelpad=10)
ax.text(2.1, 0.98, 'Aspartic Acid Titration', fontsize=22)

# Tick fontsize
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(16)

# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)

ax.patch.set_alpha(0.0)

fig.tight_layout()
#fig.savefig('figures/ToC_figure_graph.png', dpi=1200, bbox_inches='tight', transparent=True)
