import mimesis.random
from mimesis import Field, Fieldset, Schema
from mimesis.enums import Gender, TimestampFormat
from mimesis.locales import Locale

field = Field(Locale.EN, seed=0xff)
fieldset = Fieldset(Locale.EN, seed=0xff)

schema_definition = lambda: {
    "restaurant_id": field("integer_number", start=1, end=99),
    "dish_id": field("integer_number", start=1, end=1999),
    "drink_id": field("integer_number", start=1, end=1999),
}

order_schema = Schema(schema=schema_definition, iterations=1)
