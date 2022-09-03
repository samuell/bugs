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
    entity_column="person",
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
    ],
    timestamp_column="time",
)


@local.df_transformation(variant="default", inputs=[("dummydata", "default")])
def compute_fraction(df):
    newdf = df
    newdf["fraq"] = df["foo"] / df["bar"]
    return newdf[["time", "person", "fraq"]]


compute_fraction.register_resources(
    entity=person,
    entity_column="person",
    inference_store=local,
    labels=[
        {
            "name": "fraction",
            "variant": "default",
            "column": "fraq",
            "type": "float32",
        },
    ],
    timestamp_column="time",
)


ff.register_training_set(
    "traindata",
    "default",
    label=("fraction", "default"),
    features=[("foo", "default"), ("bar", "default")],
)
