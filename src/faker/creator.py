from mimesis import Locale
from mimesis.schema import CallableSchema, Schema
from typing import Any, Callable


def create_schema(schema_definition: CallableSchema, elementslocale: Locale = Locale.EN):
    schema = Schema(schema_definition, iterations=100)
    return schema