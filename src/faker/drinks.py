import mimesis.random
from mimesis import Field, Fieldset, Schema
from mimesis.enums import Gender, TimestampFormat
from mimesis.locales import Locale

field = Field(Locale.EN_CA, seed=0xff)
fieldset = Fieldset(Locale.EN_CA, seed=0xff)

schema_definition = lambda: {
        "dish": field("dish", key=lambda x: x.replace(r"'", r"''")),
        "total": field("price", minimum=12, maximum=38)
    }


if __name__ == "__main__":
    schema = Schema(schema=schema_definition, iterations=2000)
    schema.create()
    values = list(schema)
    for x in values:
        print(f"('{x['dish']}', {x['total']}),")
    pass