import featureform as ff

client = ff.ServingClient(local=True)

temp = client.training_set("traindata", "default")
temp = temp.repeat(1)
temp = temp.shuffle(1)
temp = temp.batch(1)

for feat_batch, label_batch in train_data:
    print("FEATURE BATCH:")
    print(feat_batch)
    print("LABEL BATCH:")
    print(label_batch)
