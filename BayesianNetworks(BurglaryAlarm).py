# Install the library if it's not already installed
# !pip install pgmpy --quiet

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Burglary', 'Alarm'), ('Earthquake', 'Alarm'),
    ('Alarm', 'JohnCall'), ('Alarm', 'MaryCall')
])

model.add_cpds(
    TabularCPD('Burglary', 2, [[0.99], [0.01]]),
    TabularCPD('Earthquake', 2, [[0.98], [0.02]]),
    TabularCPD('Alarm', 2, [[0.999, 0.71, 0.06, 0.05], [0.001, 0.29, 0.94, 0.95]],
               ['Burglary', 'Earthquake'], [2, 2]),
    TabularCPD('JohnCall', 2, [[0.95, 0.10], [0.05, 0.90]], ['Alarm'], [2]),
    TabularCPD('MaryCall', 2, [[0.99, 0.30], [0.01, 0.70]], ['Alarm'], [2])
)

inference = VariableElimination(model)
print(inference.query(['Alarm'], evidence={'Burglary': 1, 'Earthquake': 0}))