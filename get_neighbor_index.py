import networkx as nx
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--target_node", type=str, default="u0", help="target node index")
parser.add_argument("--hop", type=int, default="1", help="hop of nodes")
args = parser.parse_args()

g = nx.Graph()

# add user, item node
print("Adding user, item node...")
user_set = set()
item_set = set()

with open("./data/amazon-book/train.txt") as f:
	user_num = 0
	item_num = 0
	for l in f.readlines():
		if len(l) > 0:
			l = l.strip('\n').split(' ')
			items = [int(i) for i in l[1:]]
			uid = int(l[0])

			if uid not in user_set:
				user_num += 1
				user_set.add(uid)
				g.add_node('u' + str(uid), node_type='user')

			for iid in items:
				if iid not in item_set:
					item_num += 1
					item_set.add(iid)
					g.add_node('i' + str(iid), node_type='item')
				g.add_edge('u' + str(uid), 'i' + str(iid))

print('Number of nodes:', g.number_of_nodes())
print('Number of edges:', g.number_of_edges())

print('user_num:', user_num)
print('item_num:', item_num)

# Example
'''
#neigh_target_1hop = list(nx.ego_graph(g, args.target_node, 1)) # 1 hop nodes of u144
#neigh_target_2hop = list(nx.ego_graph(g, args.target_node, 2)) # range(1,2) hop

#print('neigh_'+ args.target_node +'_1hop:', neigh_target_1hop)
#print('neigh_'+ args.target_node +'_2hop:', neigh_target_2hop)

#print('len(neigh_'+ args.target_node +'_1hop):', len(neigh_target_1hop))
#print('len(neigh_'+ args.target_node +'_2hop):', len(neigh_target_2hop))
'''

neigh_target_hop = list(nx.ego_graph(g, args.target_node, args.hop))

print('neigh_'+str(args.target_node)+'_'+str(args.hop)+'hop:', neigh_target_hop)

print('len(neigh_'+str(args.target_node)+'_'+str(args.hop)+'hop):', len(neigh_target_hop))

# generate neighbor node index of target node
with open("./data/index_list.txt", "w") as file:
	result = ''
	for i, id in enumerate(neigh_target_hop):
		di = id[:1]
		if di == 'u':
			basic_id = 0
		elif di == 'i':
			basic_id = user_num
		
		result += str(basic_id + int(id[1:]))
		if i != len(neigh_target_hop) - 1:
			result += ','
		
	file.write(result)
