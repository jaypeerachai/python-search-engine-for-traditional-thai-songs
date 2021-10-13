class Song:
    def __init__(self, id, title, genre, lyric, tokens):
        self._id = id
        self._title = title
        self._genre = genre
        self._lyric = lyric
        self._tokens = tokens

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
    
    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, genre):
        self._genre = genre

    @property
    def lyric(self):
        return self._lyric
    
    @lyric.setter
    def lyric(self, lyric):
        self._lyric = lyric

    @property
    def tokens(self):
        return self._tokens
    
    @tokens.setter
    def tokens(self, tokens):
        self._tokens = tokens

    def __str__(self) -> str:
        return "[SONG ID: {}, TITLE: {}, TYPE: {}, LYRIC: {}]".format(self._id, self._title, self._genre, self._lyric)

    