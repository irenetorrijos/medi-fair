#!/usr/bin/env python

# Score calculation script.
# Author : Benjamin Maudet
# Thanks to Isabelle Guyon for the OVR ROC AUC code


import sys
import os
import os.path
import numpy as np
import json
import pandas as pd

from sklearn.metrics import roc_auc_score

print("[*] Starting scoring program")

input_dir = sys.argv[1]
output_dir = sys.argv[2]

print("[*] Input directory: %s" % input_dir)
print("[*] Output directory: %s" % output_dir)

submit_dir = os.path.join(input_dir, 'res')   #where the results will be
truth_dir = os.path.join(input_dir, 'ref')   #solution is here

print("[*] Submit directory: %s" % submit_dir)
print("[*] Truth directory: %s" % truth_dir)




# Implement the symmetric score of the challenge
def forward_auc(labels, predictions):
    target_one = [1 if x==1 else 0 for x in labels]
    score = roc_auc_score(target_one, predictions)
    return score

def reverse_auc(labels, predictions):
    target_neg_one = [1 if x==-1 else 0 for x in labels]
    neg_predictions = [-x for x in predictions]
    score = roc_auc_score(target_neg_one, neg_predictions)
    return score

if not os.path.isdir(submit_dir):
    print("[-] %s doesn't exist" % submit_dir)

if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    scores = {
        'forward_auc': -1,
        'reverse_auc': -1,
        'score': -1,
    }

    
    print("[*] Opening output file")
    output_filename = os.path.join(output_dir, 'scores.json')
    output_file = open(output_filename, 'w')

    print("[*] Reading files from %s and %s" % (truth_dir, submit_dir))
    truth_file = os.path.join(truth_dir, "solution.csv")
    truth_data = pd.read_csv(truth_file, index_col=0)

    submit_file = os.path.join(submit_dir, "results.csv")
    submit_data = pd.read_csv(submit_file, index_col=0)

    # Check that the index of the solution and the submission are the same
    if not np.all(truth_data.index == submit_data.index):
        print("[-] The index of the solution and the submission are not the same")
    else:
        forward = forward_auc(truth_data.Target, submit_data.Target)
        backward = reverse_auc(truth_data.Target, submit_data.Target)
        score = (forward + backward) / 2.0
        print("Forward AUC: %f" % forward)
        print("Reverse AUC: %f" % backward)
        print("Score: %f" % score)

        scores['forward_auc'] = forward
        scores['reverse_auc'] = backward
        scores['score'] = score

    print("[*] Writing scores to %s" % output_filename)
    output_file.write(json.dumps(scores))
    output_file.close()

    print("[*] Done")