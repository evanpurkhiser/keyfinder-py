from keyfinder import notations


class Key(object):
    """
    Key represents a musical key. This object provides mappings of the key to
    various different key notations.
    """
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return self.key

    def standard(self):
        return self.key

    def camelot(self):
        return notations.camelot[self.key]

    def open_key(self):
        return notations.open_key[self.key]


def key(file_path):
    """
    Compute the musical key of an audio file.
    """
    from keyfinder import _internal
    return Key(_internal.key(file_path))
