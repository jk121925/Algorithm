import torch
import torch.nn as nn
import torch.nn.functional as F
from transformer import MultiHeadAttentionLayer, PositionWiseFeedForwardLayer, EncoderBlock,Encoder,Transformer, calculate_similarity
import torch.optim as optim
max_len = 10
threshold = 0.7
epochs = 10
reviewed_labels = {}

def tokenize(text):
    tokens = text.lower().split()
    return tokens

def build_vocab(text):
    vocab = {word:idx for idx,word in enumerate(tokenize(text),1)}
    return vocab

def build_vocab_sentences(sentences):
    vocab = {}
    for sentence in sentences:
        for word in tokenize(sentence):
            if word not in vocab:
                vocab[word] = len(vocab)+1
    return vocab

def update_vocab(vocab,text):
    tokens = tokenize(text)
    for token in tokens:
        if token not in vocab:
            vocab[token] = len(vocab)
    return vocab

def sentences_to_indices(sentence,vocab):
    return [vocab[word] for word in tokenize(sentence)]

def pad_sentence(indices, max_len):
    return indices + [0] * (max_len - len(indices))

sentences = [
    "PyTorch is a powerful library for deep learning.",
    "C# is a powerful library for GPU scheduling.",
    "this is test sentence for comparing text in something."
]
init_vocab = build_vocab_sentences(sentences)
indices = [sentences_to_indices(sentence,init_vocab) for sentence in sentences]
mask_tensors = [torch.tensor(pad_sentence(indice,max_len)).unsqueeze(0) for indice in indices]
print(mask_tensors)
embedding_dim = 16
vocab_size = len(init_vocab)
d_model = embedding_dim
n_heads = 8
n_layers = 6

self_attention = MultiHeadAttentionLayer(d_model=d_model,h=n_heads,qkv_fc=nn.Linear(d_model,d_model),out_fc=nn.Linear(d_model,d_model))
position_ff = PositionWiseFeedForwardLayer(fc1=nn.Linear(d_model,d_model),fc2=nn.Linear(d_model,d_model))
encoder_block = EncoderBlock(self_attention=self_attention, position_ff=position_ff)

encoder = Encoder(encoder_block=encoder_block,n_layer=n_layers)

transformer = Transformer(encoder=encoder)
embedding = nn.Embedding(num_embeddings=len(init_vocab) + 1, embedding_dim=embedding_dim)
embedding_list = [embedding(input_tensor) for input_tensor in mask_tensors]

src_maskList = [transformer.make_src_mask(mask_tensor) for mask_tensor in mask_tensors]
# print(src_maskList)
# print(len(src_maskList))
# print("src_mask_list size : ",src_maskList[0].size())
# print(src_maskList[0])
# print(len(embedding_list))
# print("embedding_list size : ",embedding_list[0].size())
data_set = list(zip(src_maskList,embedding_list))

# for i, (mask, embedding) in enumerate(data_set):
#     print(f"Batch {i+1}")
#     print(mask.size())
#     print(embedding.size())
#     temp_ans = transformer(embedding,mask)
#     print(temp_ans.size())


optimizer = optim.Adam(transformer.parameters(), lr = 0.001)
print(transformer.parameters())
critierion = nn.BCELoss()

# [epoch,prediction]
labels = {
    (0, 1): [1,0],  # 첫 번째 문장과 두 번째 문장은 유사하지 않음
    (0, 2): [1,0],  # 첫 번째 문장과 세 번째 문장은 유사
    (1, 2): [1,0]   # 두 번째 문장과 세 번째 문장은 유사하지 않음
}

similarity_pair = {}

for epoch in range(epochs):
    total_loss = 0
    for i in range(len(embedding_list)):
        for j in range(i+1,len(embedding_list)):
            optimizer.zero_grad()

            output_i = transformer(embedding_list[i],src_maskList[i])
            output_j = transformer(embedding_list[j],src_maskList[j])

            similarity_pred = calculate_similarity(output_i,output_j)
            # print(similarity_pred)
            print(f"문장 {i}와 문장 {j}의 유사도: {similarity_pred.item()}")
            labels[(i,j)][1] = (labels[(i,j)][1] + similarity_pred.item())/ (labels[(i,j)][0] +1)
            labels[(i,j)][0] +=1
            if labels[(i,j)][1] >= threshold:
                similarity_pair[epoch] = [sentences[i],sentences[j]]
            print("labels[(i,j)]",labels)
            label = torch.tensor(labels[(i,j)][1], dtype = torch.float32)
            loss = critierion(similarity_pred,label)

            loss.backward(retain_graph=True)
            optimizer.step()

            total_loss += loss.item()

    print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")

print(similarity_pair)

for epoch, pair in similarity_pair.items():
    print(f"{epoch} : {pair}")


