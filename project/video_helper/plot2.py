from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

y_true = np.array([1,1,0, 1, 1, 1, 0, 0, 1, 0, 1,0, 1, 0, 0, 0, 1 , 0, 1, 0])
y_probas = np.array([0.9, 0.8, 0.7, 0.6, 0.55, 0.54, 0.53, 0.52, 0.51, 0.505, 0.4, 0.39, 0.38, 0.37, 0.36, 0.35, 0.34, 0.33, 0.30, 0.1])
# score = np.array([0.9, 0.8, 0.7, 0.6, 0.55, 0.54, 0.53, 0.52, 0.51, 0.505, 0.4, 0.39, 0.38, 0.37, 0.36, 0.35, 0.34, 0.33, 0.30, 0.1])
# y = np.array([1,1,0, 1, 1, 1, 0, 0, 1, 0, 1,0, 1, 0, 0, 0, 1 , 0, 1, 0])
fpr, tpr, thresholds = metrics.roc_curve(y_true, y_probas, pos_label=1)

# Print ROC curve
plt.plot(fpr,tpr)
plt.show()

# Print AUC
auc = np.trapz(tpr,fpr)
print('AUC:', auc)