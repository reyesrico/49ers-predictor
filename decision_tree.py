from sklearn.tree import DecisionTreeClassifier
from helpers import generateObjToPredict

##Decision Tree
def decisionTree(X_train, X_test, y_train, y_test, teamNumber, weekNumber, isPlayoff, isSuperBowl, is49ersLocal, weatherWindMPH, weatherHumidity):

  # Model
  dt_model = DecisionTreeClassifier(max_depth=3)
  # print(dt_model)

  dt_model = dt_model.fit(X_train,y_train)
  pred_dt = dt_model.predict_proba(X_test)[:, 1]

  from sklearn.metrics import classification_report
  pred_dt_binary = dt_model.predict(X_test)
  # print(classification_report(y_test, pred_dt_binary))

  obj = generateObjToPredict(11, 3, 0, 0, 1, 1.0, 52)

  prediction = dt_model.predict(obj)
  # print(prediction)
  
  ls = prediction.tolist()
  
  if ls[0] == 1:
    return True
  return False


# Display Model Tree
def displayTree(dt_model, X_train):
  from sklearn.externals.six import StringIO  
  from IPython.display import Image  
  from sklearn.tree import export_graphviz
  import pydotplus

  dot_data = StringIO()
  export_graphviz(dt_model, out_file=dot_data,  
                  filled=True, rounded=True,
                  special_characters=True, feature_names = X_train.columns.values.tolist(), 
                class_names=['49ers Lose', '49ers Win'])
  graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
  # Image(graph.create_png())
