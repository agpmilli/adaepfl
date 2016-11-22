"""
Helper function to apply reduction for each column of the dataframe grouped by a key.

Example of call:

grouped_df = original_df.groupby('some_column')

aggregating_functions = [
    (['column1'], np.mean, 
    (['column2', 'column3'], sum),
    ([('column_name_new_df', 'column_4_from_original_df'), ('column_name_2_new_df', 'column_5_from_original_df')], np.std)
]

#new_df['column1'] = original_df['column1'].apply(np.mean)
#new_df['column2'] = original_df['column2'].apply(sum)
#new_df['column3'] = original_df['column3'].apply(sum)
#new_df['column_name_new_df'] = original_df['column_4_from_original_df'].apply(np.std)
#new_df['column_name_2_new_df'] = original_df['column_5_from_original_df'].apply(np.std)
reducted_df = aggregate_dyads_to_players(grouped_df, aggregating_functions)

@param - df : the dataframe grouped by a key
@param - columns_functions: a list of tuples (columns, function_to_apply). If any element in columns is itself a tuple, the function will be applied from a column in the original df, into a new column. Otherwise it is assumed the function in the original df will be applied to the same column name in the resulting df (see example).

@return - the new dataframe grouped with reduction functions applied.
"""
def aggregate_dyads_to_players(df, columns_functions):
    new_df = df.copy()
    for columns, function in columns_functions:
        for column in columns:
            if(type(column) is tuple):
                new_df[column[0]] = df[column[1]].apply(function)
            else:
                new_df[column] = df[column].apply(function)
    return new_df
