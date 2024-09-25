from transformers import BertTokenizer, BertModel
from sklearn.cluster import KMeans
import torch

# 1. 사전 학습된 BERT 모델과 토크나이저 로드
model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# 2. 예시 문장 리스트
sentences = ["I love machine learning.", 
             "Artificial intelligence is fascinating.", 
             "I enjoy reading about deep learning.", 
             "Football is a great sport.", 
             "I play soccer every weekend."]

# 3. 문장 임베딩 추출 (BERT 사용)
inputs = tokenizer(sentences, return_tensors='pt', padding=True, truncation=True)
with torch.no_grad():
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state[:, 0, :].numpy()  # [CLS] 토큰 임베딩 사용

# 4. K-Means로 클러스터링
kmeans = KMeans(n_clusters=2)
labels = kmeans.fit_predict(embeddings)

# 5. 결과 출력
for i, sentence in enumerate(sentences):
    print(f"Sentence: '{sentence}' is in cluster {labels[i]}")
