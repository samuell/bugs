# Entity matching bug in FeatureForm

## How to reproduce

### Setting up the feature store

```
git clone https://github.com/samuell/bugs.git
cd 02-ff-entity-match
poetry install
poetry shell
featureform apply --local defs.py
```

### Trying to run training

```
python client.py
```

### Expected behaviour

Should get this output

```bash
-------Foo-------
0.002
-------Bar-------
0.004
-------FooPlusBar-------
0.006
```

### Actual bevariour

Got this:

```bash
-------Foo-------
0.002
-------Bar-------
0.004
-------FooPlusBar-------
Traceback (most recent call last):
  File "/home/sal/proj/sav/2022/bug-reproductions/02-ff-entity-match/client.py", line 15, in <module>
    fooplusbar = client.features([("fooplusbar", "default")], {"person": "samuel"})
  File "/home/sal/.cache/pypoetry/virtualenvs/20220903-ff-entity-match-9koWNEX7-py3.9/lib/python3.9/site-packages/featureform/serving.py", line 104, in features
    return self.impl.features(features, entities)
  File "/home/sal/.cache/pypoetry/virtualenvs/20220903-ff-entity-match-9koWNEX7-py3.9/lib/python3.9/site-packages/featureform/serving.py", line 304, in features
    all_features_list = self.add_feature_dfs_to_list(feature_variant_list, entity_id)
  File "/home/sal/.cache/pypoetry/virtualenvs/20220903-ff-entity-match-9koWNEX7-py3.9/lib/python3.9/site-packages/featureform/serving.py", line 319, in add_feature_dfs_to_list
    raise ValueError(
ValueError: Could not set entity column. No column name person exists in compute_fooplusbar-default
```

### Other info

If using the entity column name (`person_id`) instead of the entity name
(`person`) for the feature based on a transformation, we get output, but not
correct values:

*Expected output:*

```bash
-------Foo-------
0.002
-------Bar-------
0.004
-------FooPlusBar-------
0.006
```

*Actual output"*

```bash
-------Foo-------
0.002
-------Bar-------
0.004
-------FooPlusBar-------
0.001
```
