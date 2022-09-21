import featureform as ff

ff.register_user("myself").make_default_owner()

local = ff.register_local()

dummydata = local.register_file(
    name="dummydata",
    variant="default",
    description="",
    path="data.csv",
)

person = ff.register_entity("person")

dummydata.register_resources(
    entity="person",
    entity_column="person_id",
    inference_store=local,
    features=[
        {
            "name": "foo",
            "variant": "default",
            "column": "foo",
            "type": "float32",
        },
        {
            "name": "bar",
            "variant": "default",
            "column": "bar",
            "type": "float32",
        },
        {
            "name": "baz",
            "variant": "default",
            "column": "baz",
            "type": "float32",
        },
    ],
    labels=[
        {
            "name": "baz",
            "variant": "default",
            "column": "baz",
            "type": "float32",
        },
    ],
    timestamp_column="time",
)

ff.register_training_set(
    "all_features",
    "default",
    features=[
        ("foo", "default"),
        ("bar", "default"),
        ("baz", "default"),
    ],
    label=("baz", "default"),
)
