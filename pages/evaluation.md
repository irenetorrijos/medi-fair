# Evaluation Criteria
To evaluate submissions, we use the Area Under the Receiver Operating Characteristic Curve (ROC AUC).

The Receiver Operating Characteristic Curve is a curve of the True Positive Rate against the False Positive Rate.

![]()

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Roc_curve.svg/1024px-Roc_curve.svg.png" width=300>

The ROC AUC is a common metric for binary classification problems, but can be used for multiclass classification problems by using a one-vs-all approach, which is what we do here.

We compute one "forward" ROC AUC, where the positive class is the "A causes B" class, and one "backward" ROC AUC, where the positive class is the "B causes A" class. The final score is the average of the two ROC AUCs.

```python
def forward_auc(labels, predictions):
    target_one = [1 if x==1 else 0 for x in labels]
    score = roc_auc_score(target_one, predictions)
    return score

def reverse_auc(labels, predictions):
    target_neg_one = [1 if x==-1 else 0 for x in labels]
    neg_predictions = [-x for x in predictions]
    score = roc_auc_score(target_neg_one, neg_predictions)
    return score
		
forward = forward_auc(truth_data.Target, submit_data.Target)
backward = reverse_auc(truth_data.Target, submit_data.Target)
score = (forward + backward) / 2.0
```