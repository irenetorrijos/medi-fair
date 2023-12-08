# Data

## Overview

Training data and validation data are provided in the public_data, that you can downlad from the Files tab. The file structure is the following:
- public_data
    - train_set
        - X_train.csv
        - X_train_info.csv
        - y_train.csv
    - valid_set
        - X_valid.csv
        - X_valid_info.csv
    - test_set.zip

train_set/ contains the training data, for which labels are provided.

valid_set/ contains the validation data, for which labels are not provided. It is the data you must make prediction on to submit your solution on Codabench.

test_set.zip contains the test data. The archive is password protected. The password will be provided to the participants when the development phase ends, to make a final submission and get a final score.

 ## File content
 
 In files that contain data (X_\*.csv), there are three columns
 - SampleID : the name of the pair
 - A : a list of numbers separated by whitespaces (e.g "19226 7619 -2173 5413 6894")
 - B : same as A

In files that contain data information (X_\*_info.csv), there are three columns
- SampleID: the name of the pair
- A type : the data type of variable A (Numerical, Binary, Categorical)
- B type : same as A

In the label file for the training data (y_train), two columns:
- SampleID: the name of the pair
- Target : the causal direction (-1 if B->A, 1 if A->B, 0 otherwise)