import splitfolders

# Split with a ratio.

# it will split the folders automtically into train and test and save them in 
# the same folder with the same name
# 
splitfolders.ratio("data_path", output="output",
    seed=1337, ratio=(.8, .1, .1), group_prefix = None, move = 0 )
