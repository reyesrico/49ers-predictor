from decision_tree import decisionTree
import pandas as pd
from sklearn.model_selection import train_test_split

class Predictor:

  ## CONSTRUCTOR
  def __init__(self):
    self.X = None
    self.y = None
    self.X_train = None
    self.X_test = None
    self.y_train = None
    self.y_test = None

  ## GENERATE DATA
  @classmethod
  def generateData(self):
    scores_data = pd.read_csv('https://raw.githubusercontent.com/reyesrico/shared-files/main/spreadspoke_scores.csv')

    data_to_delete = ['schedule_date', 'stadium', 'niners_game', 'weather_detail', 'stadium_neutral',
      'spread_favorite', 'over_under_line', 'schedule_season', 'tie_game', 'local_won', 'team_favorite_id']

    # To Review
    worst_data = ['weather_temperature', 'score_home', 'score_away']

    data_to_delete = data_to_delete + worst_data

    for data in data_to_delete:
      del scores_data[data]

    # Columns Definition
    bool_cols = scores_data.columns[scores_data.dtypes=='bool'].tolist()
    numerical_cols = scores_data.columns[scores_data.dtypes=='int64'].tolist()
    categorical_cols = scores_data.columns[scores_data.dtypes=='object'].tolist()
    multi_valued_colmmns = scores_data[categorical_cols].nunique()[scores_data[categorical_cols].nunique() > 2].index.tolist()

    # Transforming bool cols to 0s and 1s.
    for column in bool_cols:
      scores_data[column] = scores_data[column].replace({False:0, True:1})

    scores_data = scores_data.fillna(0)

    # Transform multivalued columns
    scores_adjusted_data = pd.get_dummies(data = scores_data, columns=multi_valued_colmmns, drop_first=True)
    scores_adjusted_data

    # Generating Y value (If 49ers won) and X values
    self.y = scores_adjusted_data.pop("49ers_won")
    self.X = scores_adjusted_data

  ## TRAIN DATA
  @classmethod
  def trainData(self):
    self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size = 0.25)

  ## PREDICT DATA
  @classmethod
  def predict(self, teamNumber, weekNumber, isPlayoff, isSuperBowl, is49ersLocal, weatherWindMPH, weatherHumidity):
    #self._generateData()
    #self._trainData()
    return decisionTree(self.X_train, self.X_test, self.y_train, self.y_test, teamNumber, weekNumber, isPlayoff, isSuperBowl, is49ersLocal, weatherWindMPH, weatherHumidity)
