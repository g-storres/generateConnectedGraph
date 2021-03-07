# generateConnectedGraph
Simple procedure to generate the Laplacian matrix of a connected graph along with some helpful ordering/sum procedures.

Variance/edge density depends on numpy's implementation of the choice function, which I believe follows a normal distribution.

The procedure works by first generating a connected spanning tree and then adding edges until there are m edges.
