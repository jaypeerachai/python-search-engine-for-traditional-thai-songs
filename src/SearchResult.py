class SearchResult:
    def __init__(self, song, score):
        self._song = song
        self._score = score
    
    @property
    def song(self):
        return self._song

    @property
    def score(self):
        return self._score

    def __str__(self) -> str:
        return "[score={}]{}".format(self._score, self._song)

    def printOutputFormat(self):
        return "Title: {}\nType: {}\nLyric: {}".format(self._song.title, self._song.genre, self._song.lyric)

    