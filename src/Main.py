import os

from MySearcher import MySearcher

if __name__ == "__main__":
    parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_folder = os.path.join(parent_path, "dataset")
    dataset_path = os.path.join(dataset_folder, "dataset.txt")
    lexitron_folder = os.path.join(parent_path, "lexitron")
    lexitron_path = os.path.join(lexitron_folder, "lexitron.txt")
    my_searcher = MySearcher(dataset_path, lexitron_path)
    result = my_searcher.TFIDFSearch("วันเพ็ญเดือนลอยกระทง", 5)
    
    for res in result:
        print(res)
