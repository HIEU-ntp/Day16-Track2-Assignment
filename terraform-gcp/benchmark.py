import time
import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score, precision_score, recall_score
import lightgbm as lgb

start_time = time.time()
df = pd.read_csv('creditcard.csv')
load_time = time.time() - start_time

X = df.drop('Class', axis=1)
y = df['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test, reference=train_data)

params = {
    'objective': 'binary',
    'metric': 'auc',
    'boosting_type': 'gbdt',
    'verbosity': -1,
    'n_jobs': -1,
    'seed': 42
}

train_start = time.time()
model = lgb.train(params, train_data, valid_sets=[test_data], num_boost_round=1000, early_stopping_rounds=50, verbose_eval=False)
train_time = time.time() - train_start

y_pred = model.predict(X_test)
y_pred_label = (y_pred > 0.5).astype(int)

metrics = {
    'load_time': load_time,
    'train_time': train_time,
    'best_iteration': model.best_iteration,
    'auc_roc': roc_auc_score(y_test, y_pred),
    'accuracy': accuracy_score(y_test, y_pred_label),
    'f1_score': f1_score(y_test, y_pred_label),
    'precision': precision_score(y_test, y_pred_label),
    'recall': recall_score(y_test, y_pred_label),
}

# Inference latency (1 row)
single_row = X_test.iloc[[0]]
start_inf = time.time()
_ = model.predict(single_row)
metrics['inference_latency_1row'] = time.time() - start_inf

# Inference throughput (1000 rows)
batch = X_test.iloc[:1000]
start_inf = time.time()
_ = model.predict(batch)
metrics['inference_throughput_1000rows'] = 1000 / (time.time() - start_inf)

print(json.dumps(metrics, indent=2))
with open('benchmark_result.json', 'w') as f:
    json.dump(metrics, f, indent=2)
