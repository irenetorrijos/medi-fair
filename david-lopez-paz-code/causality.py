PATH_X = "../public_data/train_set/X_train.csv"
PATH_Y = "../public_data/train_set/y_train.csv"

import sys
#sys.path.append("/is/ei/dlopez/local/sched/lib/python2.7/site-packages/")

import csv, pickle, numpy as np
from   sklearn.preprocessing import scale
from   sklearn.ensemble      import GradientBoostingRegressor as GBR
from   sklearn.metrics       import roc_auc_score as auc_score
from   sklearn.model_selection   import GridSearchCV
from   scipy.stats           import skew, kurtosis, rankdata

def my_scorer(y,p):
  return (auc_score(y==1,p)+auc_score(y==-1,-p))/2

def entropy(x,m=0.1):
  h = np.histogram(x,np.floor(m*x.shape[0]))
  f = h[0]/float(len(x))
  w = h[1][1:]-h[1][0:-1]
  i = np.where(f!=0)
  return -np.nansum(f[i]*np.log(f[i]/w[i]))

def marginal(x):
  return (entropy(x),
          kurtosis(x),
          skew(x),
          len(set(x)),
          len(x),
          len(set(x))/float(len(x)),
          min(x),
          max(x),
          np.median(x),
          np.var(x),
          np.mean(x))

def featurize_row(row,w):
  r  = row.split(",",2)
  x  = np.array(r[1].split(),dtype=np.float)
  y  = np.array(r[2].split(),dtype=np.float)
  b  = np.ones(x.shape)

  # marginals
  #x  = scale(x)
  #y  = scale(y)
  #dx = np.maximum(np.dot(w[1],np.vstack((x,scale(x*x),b))),0).mean(1)
  #dy = np.maximum(np.dot(w[1],np.vstack((y,scale(y*y),b))),0).mean(1)
  dx = marginal(x) # hand-crafted
  dy = marginal(y)

  # copula projections
  x = rankdata(x)/float(len(x))
  y = rankdata(y)/float(len(y))
  d = np.maximum(np.dot(w[0],np.vstack((x,y,x*x,y*y,x*y,b))),0).mean(1)

  return np.hstack((d,dx,dy))

def featurize(filename,w):
  f = open(filename);
  pairs = f.readlines();
  f.close();
  del pairs[0];
  f   = np.array([featurize_row(row,w) for row in pairs])
  idx = [row.split(",")[0] for row in pairs]
  return (f,idx);

if(len(sys.argv)==1):
  np.random.seed(0);
  k    = 100;
  w    = (np.random.randn(k,6), np.random.randn(k,3))
  x, _ = featurize(PATH_X, w)
  y    = np.genfromtxt(PATH_Y, delimiter=",")[:,1]
  
  grid = {
    'loss'              : ['huber'],
    'n_estimators'      : [500,1000],
    'random_state'      : [0],
    'min_samples_leaf'  : [20],#[10,15,20,25],
    'max_features'      : [1.0],#[0.1,0.2,0.3,0.5,1.0],
    'alpha'             : [0.9],#[0.9,0.95,0.99],
    'max_depth'         : [20],#[20,25],
    'learning_rate'     : [0.01],#[0.02,0.01],
  }

  reg = GridSearchCV(GBR(), grid, n_jobs=4, verbose=100, score_func=my_scorer).fit(x,y)
  print(reg.best_params_)
  print(reg.best_score_)
  pickle.dump((reg.best_estimator_,w), open("classifier.pkl","wb"))

else:
  reg, w = pickle.load(open(".\program\classifier.pkl"))
  x,i    = featurize(".\input\CEnew_test_pairs.csv", w)
  p      = reg.predict(x).flatten()
  writer = csv.writer(open(".\output\CEnew_test_predict.csv", "w"), lineterminator="\n")
  rows   = [x for x in zip(i,p)]
  writer.writerow(("SampleID", "Target"))
  writer.writerows(rows)
