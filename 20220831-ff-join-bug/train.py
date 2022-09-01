import featureform as ff

client = ff.ServingClient(local=True)

train_data = client.training_set("traindata", "default")

for row in train_data:
    print("Features:")
    print(row.features())
    print("Label:")
    print(row.label())
