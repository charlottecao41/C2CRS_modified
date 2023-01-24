import json
import pickle

# train = json.load(open('data/dataset/redial/nltk/train_data.json'))
# valid = json.load(open('data/dataset/redial/nltk/valid_data.json'))
# test = json.load(open('data/dataset/redial/nltk/test_data.json'))

movie_dict = {}

for i in ['train','valid','test']:
    data = json.load(open(f'data/dataset/redial/nltk/{i}_data.json','r',encoding='utf-8'))
    for conv in data:
        for utt in conv['dialog']:
            if utt['movies'] != []:
                #find words start with @
                words = []
                for k in utt['text']:
                    if k[0]=='@':
                        words.append(k)
                for movie in utt['movies']:
                    if movie not in movie_dict:
                        movie_dict.update({movie:words[utt['movies'].index(movie)]})

file = open('movie_link_to_id.pkl','wb')
pickle.dump(movie_dict,file)
