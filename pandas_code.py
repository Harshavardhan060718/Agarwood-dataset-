import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = {
	"Tree": ["Agar Wood","Agar Wood","Agar Wood","Agar Wood","Agar Wood"],
	"Species":["malaccensis","crassna","sinensis","khasiana","filaria"],
	"Soil type":["Loamy, clay loam, acidic (pH 5.5-6.5)","Deep sandy clay, feralit, pH 4–6","Fertile sandy loam, well-drained, pH 5–7","high organic soils","Moist tropical lowlands, loamy/slightly acidic"],
	"Max-Height (M)":[25,27,15,13,11],
	"Max-Diameter (CM)":[60,70,30,35,40],
	"Total Wood Weight (Estimate) (KG)":[2000,1500,1000,1200,950],
	"Agarwood Yield (Min/Avg per Tree) (KG)":[5,4,3,2,2],
	"Market Price min (per kg)":[80000,150000,100000,80000,50000]
}
df= pd.DataFrame(data)
print(df)
df.to_csv("agarwood_dataset.csv",index= False)
print("Dataset Created Successfully!")


yeild_array= np.array(df["Market Price min (per kg)"])
print(np.mean(yeild_array))

plt.figure(figsize=(8,5))
sns.violinplot(x="Agarwood Yield (Min/Avg per Tree) (KG)",y="Market Price min (per kg)",data=df)
plt.title("Yeild vs. MArket price")
plt.xlabel("Yeild(KG)")
plt.ylabel("Market Price (KG)")
plt.grid(True)
plt.show()






































