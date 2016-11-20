import preprocessing_helper as pprh
import pandas as pd
import numpy as np
from statistics import mode

def from_dyads_to_players_aggregate(df):
    aggregate = df.groupby(['playerShort'])
    aggregate = pprh.groups_to_lists(aggregate, 'playerShort')
    data = pprh.drop_columns(aggregate,['birthday', 'player', 'photoID', 'Alpha_3', 'refCountry', 'nIAT', 'nExp','index', 'refNum', 'rater1', 'rater2'])
    data['height'] = pprh.replace_nan(data['height'])
    data['weight'] = pprh.replace_nan(data['weight'])

    unique_height = pd.DataFrame(data['height'].apply(lambda row: len(set(row))))
    player_nan_height = unique_height[unique_height['height']==0]
    unique_weight = pd.DataFrame(data['weight'].apply(lambda row: len(set(row))))
    player_nan_weight = unique_weight[unique_weight['weight']==0]

    list_diff = set(list(player_nan_weight.index.values) + list(player_nan_height.index.values))
    data = data.drop(list_diff)

    data['y'] = data['y'].apply(lambda x: int(x[0]))
    data['club'] = data['club'].apply(lambda x: x[0])
    data['leagueCountry'] = data['leagueCountry'].apply(lambda x: x[0])
    data['height'] = data['height'].apply(lambda x: x[0])
    data['weight'] = data['weight'].apply(lambda x: x[0])
    #majority vote
    data['position'] = data['position'].apply(mode)
    data['position'].fillna("Unknown", inplace=True)
    data['games'] = data['games'].apply(lambda x: sum(x))
    data['victories'] = data['victories'].apply(lambda x: sum(x))
    data['ties'] = data['ties'].apply(lambda x: sum(x))
    data['defeats'] = data['defeats'].apply(lambda x: sum(x))
    data['goals'] = data['goals'].apply(lambda x: sum(x))
    #data['yellowCards'] = data['yellowCards'].apply(lambda x: sum(x))
    #data['yellowReds'] = data['yellowReds'].apply(lambda x: sum(x))
    #data['redCards'] = data['redCards'].apply(lambda x: sum(x))
    data['seIAT'] = data['meanIAT'].apply(np.std)
    data['seExp'] = data['meanExp'].apply(np.std)
    data['meanIAT'] = data['meanIAT'].apply(np.mean)
    data['meanExp'] = data['meanExp'].apply(np.mean)
    data['yellowCardsPonder'] = data['yellowCardsPonder'].apply(lambda x: sum(x))
    data['yellowRedsPonder'] = data['yellowRedsPonder'].apply(lambda x: sum(x))
    data['redCardsPonder'] = data['redCardsPonder'].apply(lambda x: sum(x))
    data.drop('refScore', axis=1, inplace=True)
    data.dropna(inplace=True)
    return data
