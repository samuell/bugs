import featureform as ff

cli = ff.ServingClient(local=True)

dataset = cli.training_set("all_features", "default")

for row in dataset:
    print(row.features())
