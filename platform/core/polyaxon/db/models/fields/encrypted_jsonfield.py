from django.contrib.postgres.fields import JSONField

import encryptor


class EncryptedJSONField(JSONField):
    def get_db_prep_value(self, value, connection=None, prepared=False):
        value = super().get_db_prep_value(value=value, connection=connection, prepared=prepared)
        return encryptor.encrypt(value)

    def to_python(self, value):
        if value is not None and isinstance(value, str):
            value = encryptor.decrypt(value)
        return super().to_python(value)

    def get_prep_lookup(self, lookup_type, value):
        raise NotImplementedError(
            '{} lookup type for {} is not supported'.format(lookup_type, self))
