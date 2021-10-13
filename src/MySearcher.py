import csv
import math
from SearchResult import SearchResult
import pythainlp
from pythainlp.tokenize import word_tokenize

from Song import Song

class MySearcher:
    
    my_dict = None
    song_album = list()

    def __init__(self, filename, lexitron_name = None):
        self._filename = filename
        self._lexitron = lexitron_name
        if not lexitron_name is None:
            with open(lexitron_name, encoding = "utf-8") as file:
                self.my_dict = pythainlp.util.Trie(file.readlines())
        self.song_album = self.parseSong(self._filename)

    def parseSong(self, dataset_name):
        song_list = list()
        with open(dataset_name, encoding = "utf-8") as file:
            dataset = csv.reader(file, delimiter = "\t")
            for row in dataset:
                song_id = row[0]
                title = row[1][row[1].index(":") + 1:]
                genre = row[2][row[2].index(":") + 1:]
                lyric = row[3][row[3].index(":") + 1:]
                token_list = word_tokenize(lyric, engine = "longest", custom_dict = self.my_dict)
                song = Song(song_id, title, genre, lyric, token_list)
                song_list.append(song)

        return song_list

    def tokenizeQuery(self, query):
        token_list = word_tokenize(query, engine = "longest", custom_dict = self.my_dict)
        return token_list

    def TFIDFSearch(self, query, k, genre = None):
        vocab = set()
        doc_freq = dict()
        inv_doc_freq = dict()
        new_album = list()
        search_result_list = list()
        ranked_result_list = list()

        query_tokens = self.tokenizeQuery(query)
        print('query_tokens: ', query_tokens)

        # search for only specific type
        if not genre is None:
            for song in self.song_album:
                if song.genre == genre:
                    new_album.append(song)
        else:
            new_album = self.song_album
        
        # find inverse document frequncy for each term
        for song in new_album:
            for token in song.tokens:
                vocab.add(token)
                if not token in doc_freq.keys():
                    song_id_list = list()
                    song_id_list.append(song.id)
                    doc_freq[token] = song_id_list
                    idf = math.log10(float(len(new_album)))
                    inv_doc_freq[token] = idf
                else:
                    doc_freq[token].append(song.id)
                    idf = math.log10(float(len(new_album) / float(len(doc_freq[token]))))
                    inv_doc_freq[token] = idf
        
        for q in query_tokens:
            vocab.add(q)

        # find term frequency and cosine similarity
        for song in new_album:
            qd = 0
            q2 = 0
            d2 = 0
            cos = 0
            for term in vocab:
                q_freq = query_tokens.count(term)
                d_freq = song.tokens.count(term)

                q_tf = 0.0 if q_freq == 0 else 1.0 + math.log10(q_freq)
                q_weight = 0.0 if q_tf == 0 or q_freq == 0 else q_tf * inv_doc_freq[term]

                d_tf = 0.0 if d_freq == 0 else 1.0 + math.log10(d_freq)
                d_weight = 0.0 if d_tf == 0 else d_tf * inv_doc_freq[term]

                qd += q_weight * d_weight
                q2 += math.pow(q_weight, 2.0)
                d2 += math.pow(d_weight, 2.0)
                # print(q_freq, d_freq, q_tf, d_tf, qd, q2, d2)

            if not q2 == 0 and not d2 == 0:
                cos = qd / (math.sqrt(q2) * math.sqrt(d2))
            
            song_result = SearchResult(song, cos)
            search_result_list.append(song_result)
        

        search_result_list = sorted(search_result_list, key = keyFunction, reverse = True)

        if k > len(search_result_list):
            search_result_list = search_result_list[: len(search_result_list)]
        else:
            search_result_list = search_result_list[: k]
        
        for result in search_result_list:
            if not result.score == 0.0:
                ranked_result_list.append(result)

        return ranked_result_list

# def cmp(this, that):
#     if this.score == that.score:
#         return ((this.song.id > that.song.id) - (this.song.id < that.song.id))

#     return ((this.score > that.score) - (this.score < that.score))

def keyFunction(item):
    return item.score






