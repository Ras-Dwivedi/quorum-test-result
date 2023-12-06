# quorum-test-result
This repo contains the result of the quorum test conducted across multiple deployments.
Following deployments were used
1. 8 GB single vm
2. 32 GB sigle vm
3. 4 node each having 8 GB ram

# Result
QBFT was found to be fastest

# Files
1. 8 GB/  32GB/ Multinode folders contains the result of those deployments
2. In each deployments 4 methods were used.
  a. Sequentials: all transactions were given one by one
  b. Threaded 1: all transactions were given simultaneously having as many threads as the transcations
  c. Threaded 2: A maximum of 100 threads were given and all transactions were divided in those threads
  d. Threaded3 : A maximum of 25 transcations per thread were given

3. figure folder contains the images of the results
4. extractor.py is used to extract the mean and standard deviation of the result.
5. pytest.py is used to run multiple experiment through python script.
6. redolist.py is used to identify the bad experiments so that they can be done again.
7. ibft_comp.py file is used to plot the final graphs after the results are available.

