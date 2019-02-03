from decimal import Decimal,\
                    InvalidOperation
from sqlalchemy import BigInteger,\
                       Boolean,\
                       Float,\
                       Integer,\
                       Numeric
from utils.human_ids import dehumanize

class Populate():

    def __init__(self, **options):
        if options and 'from_dict' in options and options['from_dict']:
            self.populateFromDict(options['from_dict'])

    def is_relationship_item(self, key, value):
        return key.endswith('Id') \
           and hasattr(self.__class__, key[:-2]) \
           and isinstance(value, (int, str))

    def populateFromDict(self, dct, skipped_keys=[]):
        data = dct.copy()

        if data.__contains__('id'):
            del data['id']

        cols = self.__class__.__table__.columns._data

        for key in data.keys():

            data_value = data.get(key)

            if data_value == '':
                continue

            if (key == 'deleted') or (key in skipped_keys):
                continue

            if cols.__contains__(key):
                col = cols[key]

                if self.is_relationship_item(key, data_value):
                    value = dehumanize(data_value)
                    setattr(self, key, value)
                    continue

                value = data_value

                if isinstance(value, str) and isinstance(col.type, Boolean):
                    if value == 'True':
                        setattr(self, key, True)
                        continue
                    elif value == 'False':
                        setattr(self, key, False)
                        continue
                    else:
                        raise TypeError('Invalid value for %s: %r' % (key, value),
                                        'boolean',
                                        key)

                if isinstance(value, str) and isinstance(col.type, (BigInteger, Integer)):
                    try:
                        setattr(self, key, int(value))
                        continue
                    except InvalidOperation as io:
                        raise TypeError('Invalid value for %s: %r' % (key, value),
                                        'integer',
                                        key)

                elif isinstance(value, str) and isinstance(col.type, (Float, Numeric)):
                    try:
                        setattr(self, key, Decimal(value))
                        continue
                    except InvalidOperation as io:
                        raise TypeError('Invalid value for %s: %r' % (key, value),
                                        'decimal',
                                        key)

                setattr(self, key, value)
