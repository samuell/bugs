import featureform as ff

client = ff.ServingClient(local=True)

foo = client.features([("foo", "default")], {"person": "samuel"})
bar = client.features([("bar", "default")], {"person": "samuel"})

print("-"*7 + "Foo" + "-"*7)
print(foo)

print("-"*7 + "Bar" + "-"*7)
print(bar)
