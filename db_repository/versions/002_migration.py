from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
doctor = Table('doctor', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('title', String),
    Column('street', String),
    Column('city', String),
    Column('region', String),
    Column('postal_code', String),
    Column('latitude', Float),
    Column('longitude', Float),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['doctor'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['doctor'].drop()
