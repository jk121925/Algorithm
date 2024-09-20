from torch import nn
import torch
import copy
import math
import torch.nn.functional as F
class Transformer(nn.Module):

    def __init__(self, encoder):
        super(Transformer,self).__init__()
        self.encoder = encoder
    
    def encode(self,src,src_mask):
        out = self.encoder(src,src_mask)
        return out

    # def decode(self,z,c):
    #     out = self.decoder(z,c)
    #     return out
    
    def forward(self,src,src_mask):
        # print("Transformer forwrad",src, src_mask)
        encoder_out = self.encode(src,src_mask)
        # print("Transformer result tensor size",encoder_out.size())
        return encoder_out
    
    def make_src_mask(self, src):
        pad_mask = self.make_pad_mask(src,src)
        return pad_mask
    
    def make_pad_mask(self, query,key, pad_idx=0):
        # query: (n_batch, query_seq_len)
        # key : (n_batch, key_seq_len)
        query_seq_len, key_seq_len = query.size(1), key.size(1)
        key_mask = key.ne(pad_idx).unsqueeze(1).unsqueeze(2)
        key_mask = key_mask.repeat(1,1,query_seq_len,1)
        query_mask = query.ne(pad_idx).unsqueeze(1).unsqueeze(3)
        query_mask = query_mask.repeat(1,1,1,key_seq_len)
        mask = key_mask & query_mask
        mask.requires_grad = False
        # print("mask_pad_mask",mask.size())
        # print(mask)
        return mask

class Encoder(nn.Module):
    def __init__(self,encoder_block, n_layer):
        super(Encoder,self).__init__()
        self.layer = nn.ModuleList([copy.deepcopy(encoder_block) for _ in range(n_layer)])
        # self.layer = []
        # for i in range(n_layer):
        #     self.layer.append(copy.deepcopy(encoder_block))

    def forward(self,src, src_mask):
        out = src
        for layer in self.layer:
            out = layer(out, src_mask)
        # print("Encoder out forward out size", out.size())
        return out

class EncoderBlock(nn.Module):
    def __init__(self,self_attention, position_ff):
        super(EncoderBlock,self).__init__()
        self.self_attention = self_attention
        self.position_ff = position_ff
        # self.residual = [ResidualConnectionLayer() for _ in range(2)]
        self.residual = nn.ModuleList([ResidualConnectionLayer() for _ in range(2)])

    def forward(self,src,src_mask):
        out = src
        # print("EncoderBlock forward out size",out.size())
        out = self.residual[0](out, lambda out: self.self_attention(query=out, key=out, value=out, mask=src_mask))
        out = self.residual[1](out, self.position_ff)
        # out = self.self_attention(out)
        # out = self.position_ff(out)
        return out

class MultiHeadAttentionLayer(nn.Module):
    
    def __init__(self, d_model, h, qkv_fc,out_fc):
        super(MultiHeadAttentionLayer,self).__init__()
        self.d_model = d_model
        self.h = h
        self.q_fc = copy.deepcopy(qkv_fc)
        self.k_fc = copy.deepcopy(qkv_fc)
        self.v_fc = copy.deepcopy(qkv_fc)
        self.out_fc = out_fc

    
    
    def forward(self, *args, query, key, value, mask=None):
        # query, key, value: (n_batch, seq_len, d_embed)
        # mask: (n_batch, seq_len, seq_len)
        # return value: (n_batch, h, seq_len, d_k)
        # print("MultiheadAttentaion query",query.size())
        # print("MultiheadAttentaion key",key.size())
        # print("MultiheadAttentaion value",value.size())
        # print("MultiheadAttentaion",query)
        n_batch = query.size(0)

        def transform(x,fc): # (n_batch, seq_len, d_embed)
            # print("MultiHeadAttentionLayer-transform-x",x.size())
            out = fc(x) # (n_batch, seq_len, d_embed)
            # print("MultiHeadAttentionLayer-transform-x",fc)
            # print("MultiHeadAttentionLayer-transform-fc(x)",out.size())
            out = out.view(n_batch,-1, self.h, self.d_model//self.h) # (n_batch, seq_len, h, d_k)
            out = out.transpose(1,2) # (n_batch, h, seq_len, d_k)
            # print("MultiHeadAttentionLayer-transform-output",out.size())
            return out
        
        # print("MultiHeadAttentionLayer transform query")
        query = transform(query,self.q_fc)
        # print("MultiHeadAttentionLayer transform key")
        key = transform(key, self.k_fc)
        # print("MultiHeadAttentionLayer transform value")
        value = transform(value, self.v_fc)

        out = self.cal_attention(query,key,value,mask)
        out = out.transpose(1,2)
        out = out.contiguous().view(n_batch,-1,self.d_model)
        out = self.out_fc(out)
        return out
    
    def cal_attention(self, query,key,value,mask):
        # query, key, value (n_batch,seq_len,d_k) -> embed되서 d embeded x 
        # print("cal_attention query",query.size())
        # print("cal_attention mask",mask.size())
        d_k = key.shape[-1]
        # print("cal_cattention d_k",d_k)
        # print(key.transpose(-2,-1).size())
        attention_score = torch.matmul(query,key.transpose(-2,-1))
        attention_score = attention_score / math.sqrt(d_k)

        if mask is not None:
            attention_score = attention_score.masked_fill(mask==0,value=-1e9)
        attention_prob = F.softmax(attention_score,dim=-1)
        out = torch.matmul(attention_prob,value)
        return out


class PositionWiseFeedForwardLayer(nn.Module):
    def __init__(self, fc1,fc2):
        super(PositionWiseFeedForwardLayer,self).__init__()
        self.fc1 = fc1
        self.relu = nn.ReLU()
        self.fc2 = fc2
    
    def forward(self,x):
        out = x
        out = self.fc1(out)
        out = self.relu(out)
        out = self.fc2(out)
        return out

class ResidualConnectionLayer(nn.Module):
    def __init__(self):
        super(ResidualConnectionLayer,self).__init__()
    
    def forward(self,x,sub_layer):
        out = x
        out = sub_layer(out)
        out = out + x 
        return out

def calculate_similarity(embed1, embed2):
    # return F.cosine_similarity(embed1,embed2,dim=-1).mean()
    return F.relu(F.cosine_similarity(embed1,embed2,dim=-1).mean())
    
