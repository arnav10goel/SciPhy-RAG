# imports
import os
os.environ['CUDA_DEVICE_ORDER'] = 'PCI_BUS_ID'
os.environ['CUDA_VISIBLE_DEVICES'] = '8'
import json
from collections import Counter
import datasets
from tqdm import tqdm
import ast
import requests

import warnings
import pandas as pd
import math
# import networkx as nx
from datetime import datetime
import logging
# from simpletransformers.seq2seq import Seq2SeqModel, Seq2SeqArgs
# import nltk
import random
import numpy as np
import json
from tqdm import tqdm
from collections import Counter
import pickle
# import dgl
# import networkx as nx
import torch
import torch.nn as nn
import torch.nn.functional as F
import csv
# from dgl.nn.pytorch import GraphConv
# from node2vec import Node2Vec
from torch.nn import CrossEntropyLoss
import glob
import pandas as pd
import copy
# import nltk
import ast
from torch import nn
import torch
import copy
import pdb
import tqdm
from transformers import BartModel,BartPretrainedModel,BartConfig
from transformers.models.bart.modeling_bart import Seq2SeqModelOutput,Seq2SeqLMOutput



bert_metric = datasets.load_metric('bertscore')
meteor_metric = datasets.load_metric('meteor')
bleu_metric = datasets.load_metric('bleu')


# Method - 1

# In[5]:

df = pd.read_csv('/media/nas_mount/avinash_ocr/arnav_medha/output_8bit_first750.csv')
print("Shape")
print(df.shape)


#df2 = pd.read_csv('/media/nas_mount/rohan/compared_bart_vs_best_mini.csv')
#print(df2.shape)


# In[14]:


print(df.columns)
input_list = df['output_vicuna']
output_list = df['output']
#with open(f'/media/nas_mount/rohan/kelvin_lu/stylistic_Keyphrase/checkpoints_paper_keys6/18000_ouptuts') as f:
#    input_list = ast.literal_eval(f.read())

#with open(f'/media/nas_mount/rohan/kelvin_lu/stylistic_Keyphrase/checkpoints_paper_keys6/18000_target') as f:
#    output_list = ast.literal_eval(f.read())


# In[360]:


def preprocess(input_list,output_list):
    nil = []
    nol = []
    for i,j in zip(input_list,output_list):
        if type(i) == float or type(j) == float:
            continue
        if i.strip() != '' and j.strip()!='':
#            nil.append(i)
#            nol.append(j)
             nil.append(i.replace('<s>','').replace('</s>','').replace('<pad>','').replace('</pad>',''))
             nol.append(j.replace('<s>','').replace('</s>','').replace('<pad>','').replace('</pad>',''))
    return nil,nol


# In[361]:


input_list,output_list = preprocess(input_list,output_list)


# # In[362]:


# print(len(input_list))


# # In[363]:


# print(len(output_list))


# # In[364]:

# print('BERT')
# vals = bert_metric.compute(predictions=input_list,references=output_list,lang='en')
# f1 = vals['f1']


# # In[365]:


# print(sum(f1)/len(f1))


# # In[366]:


# print(sum(vals['precision'])/len(vals['precision']))


# # In[367]:


# print(sum(vals['recall'])/len(vals['recall']))


# # In[368]:

# print('METEOR')
# print(meteor_metric.compute(predictions=input_list,references=output_list))


# import sacrebleu


# # In[348]:


# bleus1 = []
# for i in range(len(input_list)):
#     if input_list[i]!= '' and output_list[i] != '':
#         bleuA = sacrebleu.corpus_bleu([input_list[i]], [output_list[i]])
#         bleus1.append(bleuA.score)


# # In[ ]:


# get_stats = lambda a: (np.mean(a), np.std(a))        
 
# #print( bleu.score )
# print('========= BLEU ===========')
# print( "blues A ::", get_stats( bleus1) )  


# # In[379]:

from nltk.translate.bleu_score import corpus_bleu as sentence_bleu
arr1 = []
arr2 = []
arr3 = []
arr4 = []
for candidate,reference in zip(input_list,output_list):
#     print(reference.split(' ')reference.split(' '))
    score = sentence_bleu([[reference.split(' ')]], [candidate.split(' ')], weights=(1, 0, 0, 0))
    score2 = sentence_bleu([[reference.split(' ')]], [candidate.split(' ')], weights=(0, 1, 0, 0))
    score3 = sentence_bleu([[reference.split(' ')]], [candidate.split(' ')], weights=(0, 0, 1, 0))
    score4 = sentence_bleu([[reference.split(' ')]], [candidate.split(' ')], weights=(0, 0, 0, 1))
    arr1.append(score)
    arr2.append(score2)
    arr3.append(score3)
    arr4.append(score4)

print('BLEU')
print(np.mean(arr1))
print(np.std(arr1))
print(np.mean(arr2))
print(np.std(arr2))
print(np.mean(arr3))
print(np.std(arr3))
print(np.mean(arr4))
print(np.std(arr4))

import rouge

all_scores = {}
for aggregator in ['Best']:
    apply_avg = aggregator == 'Avg'
    apply_best = aggregator == 'Best'

    evaluator = rouge.Rouge(metrics=['rouge-n','rouge-l'],
                        max_n=4,
                        limit_length=True,
                        length_limit=100,
                        length_limit_type='words',
                        apply_avg=apply_avg,
                        apply_best=apply_best,
                        alpha=0.5, # Default F1_score
                        weight_factor=1.2,
                        stemming=False)

    scores = evaluator.get_scores(input_list,output_list)
    j = 0
    for k,v in scores.items():

        for k2,v2,in v.items():
            if f'{k}_{k2}' not in all_scores:
                all_scores[f'{k}_{k2}'] = v2
            else:
                all_scores[f'{k}_{k2}'] += (v2-all_scores[f'{k}_{k2}'])/(j+1)
        j += 1


# In[337]:

print('Rouge')
print(all_scores)



df = pd.read_csv('/media/nas_mount/avinash_ocr/arnav_medha/output_8bit_first750.csv')
# In[ ]:

print('BERT metric')
vals = bert_metric.compute(predictions=df['output_vicuna'],references=df['output'],lang='en')
f1 = vals['f1']


# In[ ]:


print(sum(f1)/len(f1))


# In[ ]:


print(sum(vals['precision'])/len(vals['precision']))


# In[ ]:


print(sum(vals['recall'])/len(vals['recall']))


# In[ ]:

print('Meteor')
print(meteor_metric.compute(predictions=df['output_vicuna'],references=df['output']))



