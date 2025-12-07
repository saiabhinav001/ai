# Install the library if it's not already installed
# !pip install hmmlearn --quiet

import numpy as np
import matplotlib.pyplot as plt
from hmmlearn import hmm

# Define model
model = hmm.CategoricalHMM(n_components=2)
model.startprob_ = [0.6, 0.4]
model.transmat_ = [[0.7, 0.3], [0.3, 0.7]]
model.emissionprob_ = [[0.9, 0.1], [0.2, 0.8]]

# Observations: 0=Dry, 1=Wet
obs = np.array([0, 1, 0, 1, 0, 0]).reshape(-1, 1)

# Decode hidden states
logp, states = model.decode(obs, algorithm="viterbi")
print("Log probability:", logp)
print("Hidden states:", states)

# Plot
plt.plot(states, '-o', label="Hidden State")
plt.xticks(range(len(obs)))
plt.xlabel("Time Step")
plt.ylabel("State (0=Sunny, 1=Rainy)")
plt.title("Most Likely Hidden States")
plt.legend()
plt.grid(True)
plt.show()