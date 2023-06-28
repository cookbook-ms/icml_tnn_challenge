Submission contains three new files: 

1. scnn_layer.py 
   - where to store 
   - contain one class: SCNNLayer
2. scnn_train.ipynb
   - preprocessing: 
     - load a dataset: shrec16 -- requring features on faces, complex-level classification; karate club -- node-level classification 
     - lift the data from the graph domain to the topological domain 
   - create the neural network 
     - define a class: SCNN that inherits from nn.module and layer, along with linear layers
   - train the neural network on a classification task 
     - define a simple training loop for node/edge/complex classification 
3. test_scnn_layer.py 
   - where to store 
   - contain one class: TestSCNNLayer, which contains unit tests for all of the functions 