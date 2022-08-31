import featureform as ff

client = ff.ServingClient(local=True)

train_data = client.training_set("traindata", "default")

for features, labels in train_data:
    print("Features:")
    print(features)
    print("Labels:")
    print(labels)
