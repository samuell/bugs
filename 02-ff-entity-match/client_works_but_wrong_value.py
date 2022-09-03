import featureform as ff

client = ff.ServingClient(local=True)


print("-"*7 + "Foo" + "-"*7)
foo = client.features([("foo", "default")], {"person": "samuel"})
print(f"{foo[0]:.3f}")

print("-"*7 + "Bar" + "-"*7)
bar = client.features([("bar", "default")], {"person": "samuel"})
print(f"{bar[0]:.3f}")

print("-"*7 + "FooPlusBar" + "-"*7)
fooplusbar = client.features([("fooplusbar", "default")], {"person_id": "samuel"})
print(f"{fooplusbar[0]:.3f}")
