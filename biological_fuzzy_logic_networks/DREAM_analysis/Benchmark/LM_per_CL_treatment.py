from sklearn.linear_model import LinearRegression

# from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

markers_to_predict = [
    "p53",
    "cleavedCas",
    "p38",
    "RB",
    "MAPKAPK2",
    "CREB",
    "p90RSK",
    "H3",
    "MKK36",
]


# Subnetwork inputs
cont_features = [
    "AKT_S473",
    "SMAD23",
    "GSK3B",
    "AKT_T308",
    "SRC",
    "MKK4",
    "AMPK",
    "ERK12",
]

cell_line = "MCF10A"  # train cell lines
treatment = "EGF"

# cl_data = pd.read_csv(
#     f"/dccstor/ipc1/CAR/DREAM/DREAMdata/Time_aligned_per_cell_line/CL_incl_test/{cell_line}.csv"
# )
# cl_data = cl_data[cl_data["time"] == 9]
# cl_data = cl_data[cl_data["treatment"] == treatment]


# train, test = train_test_split(cl_data)

# train.to_csv(
#     f"/dccstor/ipc1/CAR/DREAM/Model/Baseline/LM_OneCellLineOneTreatment/LM_OneCellLine_{cell_line}_{treatment}_train.csv"
# )

# test.to_csv(
#     f"/dccstor/ipc1/CAR/DREAM/Model/Baseline/LM_OneCellLineOneTreatment/LM_OneCellLine_{cell_line}_{treatment}_test.csv"
# )

# Train and valid data are scaled between 0 and 1
train = pd.read_csv(
    f"/dccstor/ipc1/CAR/DREAM/Model/Mini_subnetwork/{cell_line}/train_data.csv",
    index_col=0,
)
test = pd.read_csv(
    f"/dccstor/ipc1/CAR/DREAM/Model/Mini_subnetwork/{cell_line}/valid_data.csv",
    index_col=0,
)

lm = LinearRegression()
lm.fit(train[cont_features], train[markers_to_predict])
pred = pd.DataFrame(lm.predict(test[cont_features]), columns=markers_to_predict)

pred.to_csv(
    f"/dccstor/ipc1/CAR/DREAM/Model/Mini_subnetwork/{cell_line}/LM_{cell_line}_{treatment}_predictions.csv"
)
with open(
    f"/dccstor/ipc1/CAR/DREAM/Model/Mini_subnetwork/{cell_line}/LM_{cell_line}_{treatment}.pkl",
    "wb",
) as f:
    pickle.dump(lm, f)
print(lm.score(test[cont_features], test[markers_to_predict]))
