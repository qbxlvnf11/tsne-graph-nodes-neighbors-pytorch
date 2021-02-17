

Description
=============

#### - t-SNE for graph nodes neighbors
  - t-SNE learns a two-dimensional embedding vector that preserves a certain neighboring structure of data represented as a high-dimensional vector, and expresses high-dimensional data as a two-dimensional map.
  - We add two py files (get_neighbor_index.py, select_feature.py) to get neighbors index list of target node and select embedding vector appropriated for index list.
  - Plot the x-axis and y-axis of t-SNE classified labels
  - Examples
 
<img src=https://user-images.githubusercontent.com/52263269/108198495-04b90c00-715f-11eb-9495-c38ad4cd531b.png width=350><img src=https://user-images.githubusercontent.com/52263269/108201966-cffb8380-7163-11eb-900f-5d04d7421212.png width=350>

Contents
=============

#### - get_neighbor_index.py
  - Save neighbors index list txt of target node using NetworkX
#### - select_feature.py
  - Select embedding vector apropriated to index list
  - index_text mode: read index list txt, index_range mode: set range of index list
#### - tsne_torch.py
  - Read feature vectors & labels and learning t-SNE
  - Plot axies of t-SNE
  - Using CUDA tensor

##### Order of execution: get_neighbor_index.py -> select_feature.py -> tsne_torch.py

Datasets
=============

#### - Amazon-Book Dataset

https://jmcauley.ucsd.edu/data/amazon/

References
=============

#### - NetworkX Library

https://networkx.github.io/documentation/stable/index.html

#### - t-SNE Pytorch

https://github.com/mxl1990/tsne-pytorch

Author
=============

#### - LinkedIn: https://www.linkedin.com/in/taeyong-kong-016bb2154

#### - Blog URL: https://blog.naver.com/qbxlvnf11

#### - Email: qbxlvnf11@google.com, qbxlvnf11@naver.com
