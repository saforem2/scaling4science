r"""°°°
# `scaling4science`
°°°"""
#|%%--%%| <UccbxQm8jb|pcnGYLGd0I>

%load_ext autoreload
%autoreload 2
import numpy as np
import matplotlib.pyplot as plt

#|%%--%%| <pcnGYLGd0I|30AGIq1s6L>

import os
import datetime
from typing import Tuple
from pathlib import Path
from scaling4science import set_plot_style
set_plot_style()


#|%%--%%| <30AGIq1s6L|C7cavSj0Vg>

import os
import datetime
import scaling4science

from pathlib import Path

import seaborn as sns

sns.set_context('talk')
set_plot_style()

def save_figure(
        fname: str,
        outdir: os.PathLike,
):
    pngdir = Path(outdir).joinpath('pngs')
    svgdir = Path(outdir).joinpath('svgs')
    pngdir.mkdir(exist_ok=True, parents=True)
    svgdir.mkdir(exist_ok=True, parents=True)
    pngfile = pngdir.joinpath(f'{fname}.png')
    svgfile = svgdir.joinpath(f'{fname}.svg')
    print(f'Saving figures to: {outdir}' + '/{pngs,svgs}/' + f'{fname}*')
    _ = plt.savefig(pngfile, dpi=400, bbox_inches='tight')
    _ = plt.savefig(svgfile, dpi=400, bbox_inches='tight')

#|%%--%%| <C7cavSj0Vg|vlqbbwT8cM>

labels = ('32', '64', '128')

data = {
    '25B': {
        'Old': (28, 32, 32),
        'Nvidia': (14, 46, 52),
        'New': (128, 384, 448),
    },
    '33B': {
        'Old': (36, 42, 42),
        'Nvidia': (26, 48, 52),
        'New': (192, 448, 512),
    }
}

#|%%--%%| <vlqbbwT8cM|duhZuxvxVz>

x = np.arange(len(labels))
width = 0.25
multiplier = 0

outdir = Path(
    scaling4science.__file__
).parent.parent.parent.joinpath('assets')
print(f'Saving figures to: {outdir}')

from scaling4science import COLORS
colors = {
    'Old': COLORS['red'],
    'Nvidia': COLORS['green'],
    'New': COLORS['blue']
}
for model_size, d in data.items():
    multiplier = 0
    figure, axes = plt.subplots(layout='constrained')
    fig = plt.gcf()
    ax = plt.gca()
    for label, value in d.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, value, width, label=label, color=colors[label])
        ax.bar_label(rects, padding=3)
        multiplier += 1

    ax.set_ylabel('Sequence Length (k)', fontsize='large')
    ax.set_xlabel('GPUs', fontsize='large')
    ax.set_title(f'{model_size} Model', fontsize='large')
    ax.set_xticks(x + width, labels)
    ax.legend(loc='best', ncols=1, frameon=True)  # , bbox_to_anchor=(1.05, 1.0))
    # joinpath('seq-len-compare')
    save_figure(fname=f'{model_size}', outdir=outdir)
    # fig.savefig()
    plt.show()


#|%%--%%| <duhZuxvxVz|TrIhisQEl6>

x = np.arange(len(labels))
width = 0.25

for model_size, d in data_alt.items():
    for label, value in d.items():
        multiplier = 0
        fix, ax = plt.subplots(layout='constrained')
        offset = width * multiplier
        rects = ax.bar(x + offset, value, width, label=label)
        ax.bar_label(rects, padding=3)
        multiplier += 1
        ax.set_ylabel('Sequence Length (k)')
        ax.set_xlabe


