import mimesis.random
from mimesis import Field, Fieldset, Schema
from mimesis.enums import Gender, TimestampFormat
from mimesis.locales import Locale

field = Field(Locale.EN_CA, seed=0xff)
fieldset = Fieldset(Locale.EN_CA, seed=0xff)

restaurant_schema_definition = lambda: {
    "name": field("words", quantity=2, key=lambda x: ' '.join(x).title()),
    "address": field("address"),
    "city": field("city"),
    "zip": field("zip_code"),
    "country": field("default_country")
}

if __name__ == "__main__":
    schema = Schema(schema=restaurant_schema_definition, iterations=100)
    schema.create()
    values = list(schema)
    pass