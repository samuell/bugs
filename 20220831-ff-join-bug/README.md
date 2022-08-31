# Time-correct join bug

## How to reproduce

### Setting up the feature store

```
git clone https://github.com/featureform/featureform.git
cd 20220831-ff-join-bug
poetry install
poetry shell
featureform apply --local defs.py
```

### Trying to run training

```
python train.py
```

### Expected behaviour

Should see some numerical values no the screen.

### Actual bevariour

Got this stack trace:

```bash
$ python train.py 
Traceback (most recent call last):
  File "/home/sal/proj/sav/2022/bug-reproductions/20220831-ff-join-bug/train.py", line 5, in <module>
    train_data = client.training_set("traindata", "default")
  File "/home/sal/.cache/pypoetry/virtualenvs/20220831-ff-join-bug-JAwT4QYU-py3.9/lib/python3.9/site-packages/featureform/serving.py", line 49, in training_set
    return self._local_training_set(name, version)
  File "/home/sal/.cache/pypoetry/virtualenvs/20220831-ff-join-bug-JAwT4QYU-py3.9/lib/python3.9/site-packages/featureform/serving.py", line 112, in _local_training_set
    trainingset_df = pd.merge_asof(trainingset_df, df.sort_values(['ts']), direction='backward',
  File "/home/sal/.cache/pypoetry/virtualenvs/20220831-ff-join-bug-JAwT4QYU-py3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/home/sal/.cache/pypoetry/virtualenvs/20220831-ff-join-bug-JAwT4QYU-py3.9/lib/python3.9/site-packages/pandas/core/frame.py", line 6259, in sort_values
    k = self._get_label_or_level_values(by, axis=axis)
  File "/home/sal/.cache/pypoetry/virtualenvs/20220831-ff-join-bug-JAwT4QYU-py3.9/lib/python3.9/site-packages/pandas/core/generic.py", line 1779, in _get_label_or_level_values
    raise KeyError(key)
KeyError: 'ts'
```

### First try to fix: Renaming time to ts

- Change all the occurances of "time" to "ts" in `defs.py` and `data.csv`
- Run:
  ```
  rm -rf .featureform && sleep 1 && featureform apply --local defs.py
  python train.py
  ```
  
#### Expected beaviour

- Numerical values as output.

#### Actual behavior

Got this stack trace:

```bash
$ python train.py 
Traceback (most recent call last):
  File "/home/sal/proj/sav/2022/bug-reproductions/20220831-ff-join-bug/train.py", line 5, in <module>
    train_data = client.training_set("traindata", "default")
  File "/home/sal/.cache/pypoetry/virtualenvs/20220831-ff-join-bug-JAwT4QYU-py3.9/lib/python3.9/site-packages/featureform/serving.py", line 49, in training_set
    return self._local_training_set(name, version)
  File "/home/sal/.cache/pypoetry/virtualenvs/20220831-ff-join-bug-JAwT4QYU-py3.9/lib/python3.9/site-packages/featureform/serving.py", line 112, in _local_training_set
    trainingset_df = pd.merge_asof(trainingset_df, df.sort_values(['ts']), direction='backward',
  File "/home/sal/.cache/pypoetry/virtualenvs/20220831-ff-join-bug-JAwT4QYU-py3.9/lib/python3.9/site-packages/pandas/core/reshape/merge.py", line 580, in merge_asof
    op = _AsOfMerge(
  File "/home/sal/.cache/pypoetry/virtualenvs/20220831-ff-join-bug-JAwT4QYU-py3.9/lib/python3.9/site-packages/pandas/core/reshape/merge.py", line 1740, in __init__
    _OrderedMerge.__init__(
  File "/home/sal/.cache/pypoetry/virtualenvs/20220831-ff-join-bug-JAwT4QYU-py3.9/lib/python3.9/site-packages/pandas/core/reshape/merge.py", line 1623, in __init__
    _MergeOperation.__init__(
  File "/home/sal/.cache/pypoetry/virtualenvs/20220831-ff-join-bug-JAwT4QYU-py3.9/lib/python3.9/site-packages/pandas/core/reshape/merge.py", line 681, in __init__
    self._validate_specification()
  File "/home/sal/.cache/pypoetry/virtualenvs/20220831-ff-join-bug-JAwT4QYU-py3.9/lib/python3.9/site-packages/pandas/core/reshape/merge.py", line 1809, in _validate_specification
    raise MergeError(
pandas.errors.MergeError: Incompatible merge dtype, dtype('O') and dtype('O'), both sides must have numeric dtype
```
