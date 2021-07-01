import pandas as pd
from chefboost import Chefboost as cb

# ----------------------------------------------

parallelism_cases = [True]
# parallelism_cases = [False]
# parallelism_cases = [False, True]

if __name__ == '__main__':

    for enableParallelism in parallelism_cases:
        print("-------------------------")

        print("Validation set case")

        df = pd.read_csv("dataset/wine.csv")
        validation_df = pd.read_csv("dataset/wine.csv")
        config = {'algorithm': 'C4.5', 'enableParallelism': enableParallelism}
        model = cb.fit(df, config, validation_df=validation_df)

    print("-------------------------")
    print("unit tests completed successfully...")
