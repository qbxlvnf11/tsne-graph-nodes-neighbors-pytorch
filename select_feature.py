import numpy as np
import torch
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--feature", type=str, default="features.pt", help="torch feature file name")
parser.add_argument("--label", type=str, default="labels.npy", help="numpy label file name")
parser.add_argument("--index_text", type=int, default=1, help="True: load select index text file, False: get select index range")
parser.add_argument("--index_text_name", type=str, default="index_list.txt", help="text select index file name")
parser.add_argument("--index_range", type=str, default="0,100", help="select index range")
args = parser.parse_args()

data_path = './data/'

X = torch.load(data_path + args.feature)
if len(X.size()) == 3:
	X = X[:,X.size()[1]-1,:]
print('feature size:', X.size())
X = X.tolist()

Y = np.load(data_path + args.label)
print('label size:', Y.shape)
Y = Y.tolist()

if args.index_text:
	try:
		file = open(data_path + args.index_text_name, mode = 'r', encoding = 'utf-8')
		index_list = list(map(int, file.readline().split(',')))
	finally:
		file.close()
else:
	index_list = []
	index_range = args.index_range.split(',')
	for i in range(int(index_range[0]), int(index_range[1])):
		index_list.append(i)
print('index_list:', index_list)

features = []
labels = []

for index in index_list:
	features.append(X[index])
	labels.append(Y[index])

features = torch.Tensor(features)
labels = np.array(labels)

#print('features:', features)
print('features size:', features.size())
#print('labels:', labels)
print('labels size:', labels.shape)

torch.save(features, data_path + 'select_' + args.feature) 
np.save(data_path + 'select_' + args.label, labels)
print('complete save')