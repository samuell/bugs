# Entity matching bug in FeatureForm

## How to reproduce

### Setting up the feature store

```
git clone https://github.com/samuell/bugs.git
git checkout 1.1.12
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

Should see some numerical values no the screen.

```bash
```

### Actual bevariour

Got this:

```bash
```
