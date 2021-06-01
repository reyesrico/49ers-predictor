def currentTeams():
  return {
    1: 'Atlanta Falcons',
    2: 'Baltimore Ravens',
    3: 'Buffalo Bills',
    4: 'Carolina Panthers',
    5: 'Chicago Bears',
    6: 'Cincinnati Bengals',
    7: 'Cleveland Browns',
    8: 'Dallas Cowboys',
    9: 'Denver Broncos',
    10: 'Detroit Lions',
    11: 'Green Bay Packers',
    12: 'Houston Texans',
    13: 'Indianapolis Colts',
    14: 'Jacksonville Jaguars',
    15: 'Kansas City Chiefs',
    16: 'Los Angeles Rams',
    17: 'Miami Dolphins',
    18: 'Minnesota Vikings',
    19: 'New England Patriots',
    20: 'New Orleans Saints',
    21: 'New York Giants',
    22: 'New York Jets',
    23: 'Oakland Raiders',
    24: 'Philadelphia Eagles',
    25: 'Phoenix Cardinals',
    26: 'Pittsburgh Steelers',
    27: 'San Diego Chargers',
    28: 'Seattle Seahawks',
    29: 'Tampa Bay Buccaneers',
    30: 'Tennessee Titans',
    31: 'Washington Football Team'
  }

def generateTeamValues(teamNumber):
  teams = {
    'opposite_team_Atlanta Falcons': 0, 'opposite_team_Baltimore Colts': 0,
    'opposite_team_Baltimore Ravens': 0, 'opposite_team_Buffalo Bills': 0,
    'opposite_team_Carolina Panthers': 0, 'opposite_team_Chicago Bears': 0,
    'opposite_team_Cincinnati Bengals': 0, 'opposite_team_Cleveland Browns': 0,
    'opposite_team_Dallas Cowboys': 0, 'opposite_team_Denver Broncos': 0,
    'opposite_team_Detroit Lions': 0, 'opposite_team_Green Bay Packers': 0,
    'opposite_team_Houston Oilers': 0, 'opposite_team_Houston Texans': 0,
    'opposite_team_Indianapolis Colts': 0, 'opposite_team_Jacksonville Jaguars': 0,
    'opposite_team_Kansas City Chiefs': 0, 'opposite_team_Los Angeles Chargers': 0,
    'opposite_team_Los Angeles Raiders': 0, 'opposite_team_Los Angeles Rams': 0,
    'opposite_team_Miami Dolphins': 0, 'opposite_team_Minnesota Vikings': 0,
    'opposite_team_New England Patriots': 0, 'opposite_team_New Orleans Saints': 0,
    'opposite_team_New York Giants': 0, 'opposite_team_New York Jets': 0,
    'opposite_team_Oakland Raiders': 0, 'opposite_team_Philadelphia Eagles': 0,
    'opposite_team_Phoenix Cardinals': 0, 'opposite_team_Pittsburgh Steelers': 0,
    'opposite_team_San Diego Chargers': 0, 'opposite_team_Seattle Seahawks': 0,
    'opposite_team_St. Louis Cardinals': 0, 'opposite_team_St. Louis Rams': 0,
    'opposite_team_Tampa Bay Buccaneers': 0, 'opposite_team_Tennessee Titans': 0,
    'opposite_team_Washington Football Team': 0, 'opposite_team_Washington Redskins': 0
  }

  teamName = 'opposite_team_' + currentTeams()[teamNumber]
  teams[teamName] = 1
  return list(teams.values())

def generateWeekValues(weekNumber):
  weeks = {
    'schedule_week_10': 0,
    'schedule_week_11': 0,
    'schedule_week_12': 0,
    'schedule_week_13': 0,
    'schedule_week_14': 0,
    'schedule_week_15': 0,
    'schedule_week_16': 0,
    'schedule_week_17': 0,
    'schedule_week_18': 0,
    'schedule_week_2': 0,
    'schedule_week_3': 0,
    'schedule_week_4': 0,
    'schedule_week_5': 0,
    'schedule_week_6': 0,
    'schedule_week_7': 0,
    'schedule_week_8': 0,
    'schedule_week_9': 0,
    'schedule_week_Conference': 0,
    'schedule_week_Division': 0,
    'schedule_week_Superbowl': 0,
    'schedule_week_Wildcard': 0
  }

  weeks['schedule_week_' + str(weekNumber)] = 1
  return list(weeks.values())

def generateObjToPredict(teamNumber, weekNumber, isPlayoff, isSuperBowl, is49ersLocal, weatherWindMPH, weatherHumidity):
  basic = [isPlayoff, is49ersLocal, weatherWindMPH, weatherHumidity]
  weeks = generateWeekValues(weekNumber)
  teams = generateTeamValues(teamNumber)

  res = basic + weeks + teams
  return [res]


def getTeams():
  teams = currentTeams()
  resp = []
  for key in teams:
    obj = { 'id': key, 'name': teams[key] }
    resp.append(obj)
  
  return resp
