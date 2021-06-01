import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

## Logistic Regression
def logisticRegression(X_test, y_test):

  # fit a model
  clf = LogisticRegression(penalty='l2', max_iter=250).fit(X_train, y_train)

  # predict probabilities
  predictions = clf.predict_proba(X_test)[:, 1]

  y_pred = clf.predict(X_test)

  # calculate scores
  auc = roc_auc_score(y_test, predictions)
  print(auc)

  # calculate roc curves
  fpr, tpr, _ = roc_curve(y_test, predictions)

  plt.figure(figsize=(15, 10))
  # plot horizontal line 
  plt.plot([0, 1], [0, 1], linestyle='--')
  # plot the roc curve for the model
  plt.plot(fpr, tpr, label='ROC curve (AUC = %0.2f)' % auc)
  # axis labels
  plt.xlabel('FPR')
  plt.ylabel('TPR')
  # show the legend
  plt.legend(loc='lower right')
  # show the plot
  plt.show()

  feature_importance = abs(clf.coef_[0])
  # feature_importance = 100.0 * (feature_importance / feature_importance.max())
  sorted_idx = np.argsort(feature_importance)
  pos = np.arange(sorted_idx.shape[0]) + .5

  featfig = plt.figure(figsize=(10, 15))
  featax = featfig.add_subplot(1, 1, 1)
  featax.barh(pos, feature_importance[sorted_idx], align='center')
  featax.set_yticks(pos)
  featax.set_yticklabels(np.array(X.columns)[sorted_idx], fontsize=8)

  plt.show()
