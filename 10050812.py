import pandas as pd
import os
from datetime import datetime
import psycopg2
from dotenv import load_dotenv

load_dotenv()
abs_path = os.path.abspath(os.path.dirname(__file__))
now = datetime.now().strftime("%Y%m%d")
file_path = os.path.join(abs_path,"data")
print(file_path)
print(abs_path)
# YYYYMMDD_dataset.parquet
if not os.path.exists(file_path):
    os.mkdir(file_path)

column = ["c_dix1","c_dix2","similarity","group"]
global_standard_pointer = 1
global_comparsion_pointer = 1
# 워크 플로우 :
# 1. DB에서 쿼리를 진행 -> choice 데이터 추출
# 2. 데이터 전처리

CONNECTIONCONIFG = {
    'host':"localhost",
    'database':"testdb",
    'user':"postgres",
    'password':"1q2w3e4r!@#"
}

connection = psycopg2.connect(**CONNECTIONCONIFG)
cursor = connection.cursor()

sentences = [
    (1, "The sky is clear and the weather is perfect today."),
    (2, "Its a beautiful day with clear skies and warm sunshine."),
    (3, "I love the sunny days in the middle of autumn."),
    (4, "The weather today is so pleasant and bright."),
    (5, "He enjoys walking in the park on sunny afternoons."),
    (6, "Today is a great day to be outside enjoying nature."),
    (7, "The weather outside is absolutely stunning right now."),
    (8, "She prefers spending her time reading books indoors."),
    (9, "Reading a book by the window during a rainy day is my favorite thing to do."),
    (10, "It started raining heavily in the middle of the night."),
    (11, "He couldnt resist taking a nap on such a rainy afternoon."),
    (12, "The heavy rain made the roads slippery and dangerous."),
    (13, "I couldnt sleep last night because the rain was so loud."),
    (14, "The coffee shop is my favorite place to relax and unwind."),
    (15, "She finds peace in quiet moments spent alone."),
    (16, "Taking a long walk in nature helps me clear my mind."),
    (17, "A peaceful morning walk by the lake is refreshing."),
    (18, "He loves walking along the beach, listening to the sound of waves."),
    (19, "Spending time at the beach is always relaxing."),
    (20, "The sound of waves and the cool breeze create a perfect atmosphere.")
]

def sentences_to_df(sentences):
    df = pd.DataFrame({
        'sentences' : [s for _, s in sentences],
        'similarity' : None,
        'group' : [g for g, _ in sentences]
    })
    
    df.to_parquet(os.path.join(abs_path,f"{now}_output.parquet"))
    return df

def load_last():
    dirpath, dirnames, filenames = os.walk(file_path)
    
def union(parent,a,b):
    if parent[a] < parent[b]:
        parent[b] = parent[a]
        # parent node, smaller_index, bigger_index
        return parent[a]
    else:
        parent[a] = parent[b]
        return parent[b]

def find(parent,a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]


sentences_to_df(sentences)
df = pd.read_parquet(os.path.join(abs_path,f"{now}_output.parquet"))
print(df)
try:
    cursor.execute("SELECT * FROM choice_pointer;",)
    ans = cursor.fetchone()
    global_standard_pointer = int(ans[0])
    global_comparsion_pointer = int(ans[1])
except Exception as e:
    print(e)

# for s in sentences:
#     cursor.execute(f"INSERT INTO choice (choice) VALUES ('{s[1]}');")
#     connection.commit()

try:
    cursor.execute("SELECT * FROM choice")
    choices = cursor.fetchall()
    choices = [(0,"dummy")] + choices
    print(choices)
    end_max = choices[-1][0]

    # for i in range(1,21):
    #     cursor.execute(f"INSERT INTO choice_relation (index,parent) VALUES ({i},{i})")
    #     connection.commit()
    cursor.execute("SELECT * FROM choice_relation")
    choice_relation = cursor.fetchall()
    choice_parent = {i:value for i,value in choice_relation}
    print(choice_parent)
    while global_standard_pointer != global_comparsion_pointer:
        print("staret",global_standard_pointer,global_comparsion_pointer)
        print(choices[global_standard_pointer])
        print(choices[global_comparsion_pointer])
        temp_ans = input("y/n")
        if temp_ans == "y":
            parent= union(choice_parent,global_standard_pointer,global_comparsion_pointer)
            cursor.execute(f"UPDATE choice_relation set parent={parent} WHERE index = {global_comparsion_pointer}")
            cursor.execute(f"INSERT INTO choice_relation_vec (idx1,idx2,similarity) VALUES ({global_standard_pointer},{global_comparsion_pointer},{1})")
            cursor.execute(f"UPDATE rank set depth = depth + 1 where index={parent}")
            while True:
                cursor.execute(f"INSERT INTO choice_relation_vec (idx1,idx2,similarity) VALUES ({global_standard_pointer},{global_comparsion_pointer},{0})")
                if global_comparsion_pointer == end_max:
                    break
                global_comparsion_pointer +=1
        else:
            cursor.execute(f"INSERT INTO choice_relation_vec (idx1,idx2,similarity) VALUES ({global_standard_pointer},{global_comparsion_pointer},{0})")
        # 포인터 변경: 비교하는 포인터가 마지막이거나, 유저가 yes를 누른 경우 다음 standar_pointer로 변경
        if global_comparsion_pointer == end_max:
            global_standard_pointer +=1
            global_comparsion_pointer = global_standard_pointer + 1
        # 그렇지 않을 경우 comparsion_pointer만 변경
        else:
            global_comparsion_pointer+=1
        cursor.execute(f"UPDATE choice_pointer set standard_pointer={global_standard_pointer},comparsion_pointer={global_comparsion_pointer}")
        connection.commit()
        print(global_standard_pointer,global_comparsion_pointer)
except Exception as e:
    print(e)


