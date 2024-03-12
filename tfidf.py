import sys, os, time,json
module_path = os.path.abspath("C:/Users/73018/Desktop/dSearch/dSearch_module")
sys.path.append(module_path)
import module_preprocessing as PRE
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

explain_txt = """
This program will extract keyword from text
there are four options
    1. folder_path 
        COMMAND INPUT : -i [folder_path]
        DEFAULT VALUE : ./
        input is set target folder extract keyword from "only" pptx
        program run on recursivly track the folder and fun all child folder
    2. min : -m [minimun number about existing keyword]
        COMMAND INPUT : -m [minimun number]
        DEFAULT VALUE : 2
        About keyword this will take the threshold for keyword Count
    3. output_name
        COMMAND INPUT : -o [output_path]
        DEFAULT VALUE : output
        output_name will run for excel
    4. ngram
        COMMAND INPUT : -n [ngram max number]
        DEFAULT VALUE : None
        if you want to take the ngram algorithm in tfidf this will be parameter for ngram"""


def tfidf_cal_func_stat(folder_path="./", min=2, output_name="output", ngram=None):
    extract_text_df = pd.DataFrame(
        list(PRE.folder2data(folder_path).items()), columns=["location", "keyword"]
    )
    keyword = extract_text_df["keyword"].tolist()
    location = extract_text_df["location"].tolist()
    if ngram is None:
        tfidf_vectorizer = TfidfVectorizer(min_df=min)
    else:
        tfidf_vectorizer = TfidfVectorizer(min_df=min, ngram_range=ngram)

    count_vector = CountVectorizer()
    cv = count_vector.fit_transform(keyword)
    cv_temp = sorted(
        count_vector.vocabulary_.items(), key=lambda x: x[1], reverse=False
    )
    cv_temp_list = [x[0] for x in cv_temp]
    cv_df = pd.DataFrame(cv.toarray(), columns=cv_temp_list)

    tfidf_vectorizer.fit(keyword)
    word_id_list = sorted(
        tfidf_vectorizer.vocabulary_.items(), key=lambda x: x[1], reverse=False
    )
    word_list = [x[0] for x in word_id_list]

    tf_idf_df = pd.DataFrame(
        tfidf_vectorizer.transform(keyword).toarray(), columns=word_list
    )
    reverse_tf_idf_df = tf_idf_df.transpose()
    reverse_tf_idf_df["word"] = reverse_tf_idf_df.index
    reverse_tf_idf_df.rename_axis("index").reset_index()
    tf = pd.DataFrame.from_dict(tfidf_vectorizer.vocabulary_, orient="index").rename(
        columns={0: "tf"}
    )
    tf["word"] = tf.index
    tf.rename_axis("index").reset_index()
    print(tfidf_vectorizer.vocabulary)
    reverse_tf_idf_df["tf_idf_cal"] = reverse_tf_idf_df.mean(axis=1) * 10000
    return [reverse_tf_idf_df, cv_df]


def tfidf_cal_func(folder_path="./", min=2, output_name="output", ngram=None):
    extract_text_df = pd.DataFrame(
        list(PRE.folder2data(folder_path).items()), columns=["location", "keyword"]
    )
    keyword = extract_text_df["keyword"].tolist()
    location = extract_text_df["location"].tolist()
    if ngram is None:
        tfidf_vectorizer = TfidfVectorizer(min_df=min)
    else:
        tfidf_vectorizer = TfidfVectorizer(min_df=min, ngram_range=ngram)

    tfidf_vectorizer.fit(keyword)
    word_id_list = sorted(
        tfidf_vectorizer.vocabulary_.items(), key=lambda x: x[1], reverse=False
    )
    word_list = [x[0] for x in word_id_list]

    tf_idf_df = pd.DataFrame(
        tfidf_vectorizer.transform(keyword).toarray(), columns=word_list
    )
    reverse_tf_idf_df = tf_idf_df.transpose()
    text_ranking_dict = {}
    for num in range(0, len(location)):
        temp = reverse_tf_idf_df[num].sort_values(ascending=False)
        temp_index_list = temp.index.tolist()
        text_ranking_dict[location[num]] = temp_index_list
        text_ranking_dict[location[num] + " weight"] = temp.tolist()
    result_data = pd.DataFrame(text_ranking_dict)
    result_data.to_csv("./" + output_name + ".csv", encoding="utf-8-sig")
    return result_data


# tfidf_cal_func("./03.Clean Room", 1, "test_output_file", (1,2))


def tfidf_analysis(folder_path="./", min=2, ngram=None):
    start = time.time()
    extract_text_df = pd.DataFrame(
        list(PRE.folder2data(folder_path).items()), columns=["location", "keyword"]
    )
    end = time.time()
    print(f"this is folder extrating time {end-start}")
    keyword = extract_text_df["keyword"].tolist()
    location = extract_text_df["location"].tolist()
    if ngram is None:
        tfidf_vectorizer = TfidfVectorizer(min_df=min)
    else:
        tfidf_vectorizer = TfidfVectorizer(min_df=min, ngram_range=ngram)

    tfidf_vectorizer.fit(keyword)
    matrix = tfidf_vectorizer.fit_transform(keyword)
    
    
    return [keyword, location, tfidf_vectorizer, matrix]




def tfidf_analysis_threading(folder_path="./", min=2, ngram=None):
    start = time.time()
    extract_text_df = pd.DataFrame(
        list(PRE.folder2data_threading(folder_path).items()), columns=["location", "keyword"]
    )
    end = time.time()
    print(f"this is folder extrating time {end-start}")
    keyword = extract_text_df["keyword"].tolist()
    location = extract_text_df["location"].tolist()
    if ngram is None:
        tfidf_vectorizer = TfidfVectorizer(min_df=min)
    else:
        tfidf_vectorizer = TfidfVectorizer(min_df=min, ngram_range=ngram)

    tfidf_vectorizer.fit(keyword)
    matrix = tfidf_vectorizer.fit_transform(keyword)
    return [keyword, location, tfidf_vectorizer, matrix]

def tfidf_DB_threading(folder_path="./",min=2,ngram=None):

    start = time.time()
    extract_text_df = pd.DataFrame(
        list(PRE.folder2data_threading(folder_path).items()), columns=["location", "keyword"]
    )
    end = time.time()
    print(f"this is folder extrating time {end-start}")
    keyword = extract_text_df["keyword"].tolist()
    location = extract_text_df["location"].tolist()
    if ngram is None:
        tfidf_vectorizer = TfidfVectorizer(min_df=min)
    else:
        tfidf_vectorizer = TfidfVectorizer(min_df=min, ngram_range=ngram)

    tfidf_matrix = tfidf_vectorizer.fit_transform(keyword)
    feature_name = tfidf_vectorizer.get_feature_names_out()
    result_dic = {}

    for i in range(len(location)):
        doc_dict = {}
        for j, feature in enumerate(feature_name):
            tfidf_value = tfidf_matrix[i,j]
            if tfidf_value>0:
                doc_dict[feature] = {
                    "tf": tfidf_matrix[i,j],
                    "idf": tfidf_vectorizer.idf_[j],
                    "tf-idf": tfidf_matrix[i,j] * tfidf_vectorizer.idf_[j]
                }
        result_dic[location[i]] = doc_dict
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(result_dic,f,ensure_ascii=False, indent=4)



if __name__ == "__main__":
    print(sys.argv)
    if ("-h" in sys.argv or "-help" in sys.argv or "h" in sys.argv) and len(
        sys.argv
    ) == 2:
        print(explain_txt)
    else:
        input_name = "./"
        min_val = 2
        output_name = "output"
        ngram = None
        if "-i" in sys.argv:
            input_name = sys.argv[sys.argv.index("-i") + 1]
        if "-o" in sys.argv:
            output_name = sys.argv[sys.argv.index("-o") + 1]
        if "-m" in sys.argv:
            min_val = sys.argv[sys.argv.index("-m") + 1]
        if "-n" in sys.argv:
            ngram = (1, int(sys.argv[sys.argv.index("-m") + 1]))
        start = time.time()
        print("*" * 50, "root folder {} extrating start".format(input_name), "*" * 50)
        tfidf_cal_func(
            folder_path=input_name,
            min=int(min_val),
            output_name=output_name,
            ngram=ngram,
        )
        print("*" * 50, "root folder {} extrating end".format(input_name), "*" * 50)
        end = time.time()
        print("total extrating time : {} sec".format(end - start))


# trouble shooting :
# 폴더나 pptx가 아님에도 pptx가 붙어 있으면 문제가 생기는 듯


# temp_text = pd.DataFrame(list(PRE.folder2data("./03.Clean Room").items()),columns=['location',"keyword"])
# # print(pandas.DataFrame(list(folder2data("./03.Clean Room").items()),columns=['location',"keyword"]))
# text = temp_text['keyword'].tolist()
# location = temp_text['location'].tolist()

# # text.to_csv('./init_preprocess.csv', encoding='utf-8-sig')
# tfidf_vectorizer = TfidfVectorizer(min_df =1, ngram_range = (1, 2)).fit(text)
# print("*"*100)
# word_id_list = sorted(tfidf_vectorizer.vocabulary_.items(), key=lambda x: x[1], reverse=False)
# word_list = [x[0] for x in word_id_list]

# # 용이한 시각화를 위하여 데이터프레임 변환
# tf_idf_df = pd.DataFrame(tfidf_vectorizer.transform(text).toarray(), columns = word_list)
# tf_idf_df.to_csv('./tfidf_structure.csv', encoding = 'utf-8-sig')
# print(tf_idf_df)

# # tf_idf_df.transpose().to_csv('./tfidf_reverse_structure.csv',encoding = 'utf-8-sig')
# reverse_tf_idf_df = tf_idf_df.transpose()
# text_ranking = {}
# for num in range(0,97):
#     temp = reverse_tf_idf_df[num].sort_values(ascending = False)
#     temp_list = temp.index.tolist()
#     text_ranking[location[num]] = temp_list
#     text_ranking[location[num]+'weight'] = temp.tolist()
# result_data = pd.DataFrame(text_ranking )
# result_data.to_csv("./result_data1.csv", encoding = 'utf-8-sig')

# print("*"*100)
# vector = tfidf_vectorizer.transform(text).toarray()
# vector = np.array(vector)
# print(vector)
# print(vector.shape)
