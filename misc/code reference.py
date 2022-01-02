# code to create subplot

import seaborn as sns
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (18, 20))
for index in range(len(cat_features)):
    plt.subplot(8, 5, index + 1)
    sns.countplot(data = train.dropna(), x = train.loc[:, cat_features[index]])
    plt.xticks(rotation = 90)
    plt.tight_layout()
    
    
    
# code to create heatmap

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))
sns.heatmap(train_data.corr(), center = 0)
plt.title("Correlations Between Columns")
plt.show()


