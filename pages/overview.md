# The MEDI-FAIR competition

## Background
Understanding the causal relationships between variables is a central goal in many fields, ranging from the social and behavioral sciences to the natural and physical sciences. It is especially common in medical studies, as understanding the causal relationship between genetic or environmental factors and the occurrence or severity of a disease is the first step in developing strategies for prevention, diagnosis and treatment. The latest fairness principles are grounded in causality, acknowledging the widespread belief that incorporating causality is imperative in effectively addressing the problem of fairness.

One established way to establish causal relationships is to do randomized controlled trials (RCTs), in which the subjects are randomly assigned into a test group and a control group, and where the potential cause and effect factors occur in a controlled environment. RCTs are considered the best approach to establish causal relationships, because they are designed to minimize risks of bias and confounding.

Confounding occurs when a third factor causes both the supposed exposure and outcome. When this third factor is unknown, it is possible to make false assumptions about causal relationships, or over-evaluate a weak causal relationship.

But when experimentation through RCTs is not possible, causal relationships have to be infered using available observational data, through causal discovery algorithms. However, reconstructing a causal graph from empirical observational data can be challenging, as it is often difficult to disentangle the true causal relationships from the influence of unknown confounding factors, mediators, and sample bias.

## Goal

The goal of this challenge is to recover the causal direction of the relationship between two variables A and B. 4 scenarios are possible:
- A causes B
- B causes A
- A and B are both consequences of a common cause C
- A and B are independant

For simplicity, we merge the last two scenarios. The participants are asked to produce a confidence score between -inf and +inf, where a positive score indicates that A causes B, and a negative score indicates that B causes A. The higher (or lower in the negative case) the score, the higher the confidence in the answer. A score close to 0 indicates that A and B are independant, or that A and B are both consequences of a common cause.

## Challenge phases

### Phase 1: development phase
The study phase will be used to develop the methodology and the system. The participants are provided with causal pairs, divided in a training and validation set. The causal direction is provided for the training set, but not for the validation set. The participants must make predictions on the validation set that they will submit to codabench.

### Phase 2: evaluation phase
The public data, in addition to the training and validation set, also contains a testing set. It is in a password protected archive. The password will be published on this page when this phase starts. On this phase, participants can only make one submission. It will be evaluated in the same way as the development phase. This is to validate that the participants didn't overfit the validation set.

## Instructions to register
- Click "My Submissions" tab 
- Accept terms and conditions
- Click register button

## Reward 
As this is an educational challenge, there is no reward offered for this competition.

## The MEDI-FAIR team
The main team is composed of:
- [Benjamin Maudet](https://github.com/DaRealNim) (team leader)
- Irene Torrijos

We had the help from these wonderful people:
- [Isabelle Guyon](https://guyon.chalearn.org)
- [Ihsan Ullah](https://ihsaan-ullah.github.io/)
- [Lisheng Sun](https://scholar.google.com/citations?user=_8h_NEcAAAAJ&hl=en)
- [Kristin Bennett](https://homepages.rpi.edu/~bennek/)

The team can be contacted at [medi-fair@chalearn.org.](mailto:medi-fair@chalearn.org)

## Credit
Causal pairs : Isabelle Guyon
<!--Phase 2 data : [Liu, Tianyu; Fan, Wenhui; Wu, Cheng (2019), “Data for: A hybrid machine learning approach to cerebral stroke prediction based on imbalanced medical-datasets”, Mendeley Data, V1, doi: 10.17632/x8ygrw87jw.1](https://doi.org/10.17632/x8ygrw87jw.1)-->