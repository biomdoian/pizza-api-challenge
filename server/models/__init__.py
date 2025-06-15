from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
      "fk": "fk_%(table_name)s_%(column_names)s_%(referred_table_name)s",
    })
db = SQLAlchemy(metadata=metadata)
