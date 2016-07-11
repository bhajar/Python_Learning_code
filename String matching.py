import numpy as np
from sklearn.metrics import jaccard_similarity_score

y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]
jaccard_similarity_score(y_true, y_pred)


jaccard_similarity_score(y_true, y_pred, normalize = False)
?jaccard_similarity_score

http://bommaritollc.com/2014/06/30/advanced-approximate-sentence-matching-python/
http://nbviewer.jupyter.org/urls/gist.github.com/mjbommar/e2a019e346b879c13d3d/raw/74a206c2629d6e661645e18369f05f6c79d15b65/fuzzy-sentence-matching-python.ipynb
https://infoscience.epfl.ch/record/161961/files/Lhuillery%20RP2009b.pdf

