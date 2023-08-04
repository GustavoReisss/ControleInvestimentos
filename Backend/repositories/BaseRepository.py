from pony.orm import db_session, select, commit
from pony.orm.core import ObjectNotFound

from pony.orm import db_session

class BaseRepository:
    def __init__(self, entity):
        self.entity = entity

    @db_session
    def get(self, user_id):
        try:
            user = self.entity[user_id]
            return user
        except ObjectNotFound:
            return None

    @db_session
    def get_all(self, **filters):
        print("filters", filters)
        query = select(u for u in self.entity)

        for field, value in filters.items():
            if '__like' in field:
                field_name = field.split('__like')[0]
                query = query.filter(lambda item: value.lower() in getattr(item, field_name).lower())
                continue

            query = query.filter(lambda u: getattr(u, field) == value)

        return query[:]

    @db_session
    def create(self, data):
        entity = self.entity(**data)
        commit()
        return entity

    @db_session
    def update(self, user_id, data):
        user = self.entity[user_id]
        user.set(**data)
        commit()
        return user

    @db_session
    def delete(self, user_id):
        user = self.entity[user_id]
        user.delete()
        commit()
