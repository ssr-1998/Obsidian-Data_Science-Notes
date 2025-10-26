
# Index
1. [[#Important Pointers]]

Refer [[Understanding LSTM Networks (Colah's Blog).pdf]]

### Important Pointers:

- An LSTM cell does indeed have gating mechanism. It includes three gates: the **forget gate**, **update gate**, and the **output gate**.

- An LSTM is similar to an RNN layer except that the RNN cells are replaced with LSTM cells.

- An LSTM does have an explicit cell state.

- An RNN does allow for an easier flow of gradients called as the **constant error carousel**.

- The LSTM cell is able to solve the problem of vanishing gradients because the Gradient is propagated from the cell state `ct` to the previous cell state `ct−1` without any weights involved directly between `ct` and `ct−1` which ensures that at least some gradient is always propagated **backwards in time**.
