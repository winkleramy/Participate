import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('zCode/FirewiseCommunityNames.txt',header=0)
namelen = [len(name) for name in df.Names]

plt.figure()
plt.hist(namelen)
plt.xlim([0,40])
plt.ylim([0,20])
plt.yticks(np.arange(0,21,2))
plt.title('Firewise Name Character Length')
plt.xlabel('number of characters in name')
plt.ylabel('number of communities')

print(np.average(namelen))
print(np.std(namelen))
print('done')