import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

X, y = [], []
for bp_id in [f"{i:03}" for i in range(1, 100+1)]:
    for n in range(12):
        name = f"#BP{bp_id}_{n}"
        img = Image.open(f"cells/{name}.jpg")
        X.append(np.asarray(img).flatten())
        y.append(name)

        # plt.imshow(X[-1].reshape(98, 98), interpolation="nearest")
        # plt.show()

np.array(X).dump(open('array_X_cells.npy', 'wb'))
np.array(y).dump(open('array_y_names.npy', 'wb'))
import pandas as pd
pd.DataFrame(X).to_excel("test_X.xlsx")
