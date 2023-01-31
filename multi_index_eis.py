import numpy as np
import pandas as pd

WANTED_COLUMNS=(0, 3, 4, 5)
# possible columms - ['freq / Hz', 'neg. Phase / °', 'Idc / uA', 'Z / Ohm', "Z' / Ohm", "Z'' / Ohm", 'Cs / F']
# (0, 3, 4, 5) -> ['freq / Hz', 'Z / Ohm', "Z' / Ohm", "Z'' / Ohm"]

csv_filename='pa14_eis_-400mV_e5.csv'

names_list=np.genfromtxt(csv_filename, dtype=str, delimiter=',')[0]
unique_names=np.unique(names_list)[1:]
#['pa14_eis_edc_-0-4-00' 'pa14_eis_edc_-0-4-01' 'pa14_eis_edc_-0-4-02' ... 'pa14_eis_edc_-0-4-29' 'pa14_eis_edc_-0-4-30']

eis_df=pd.read_csv(csv_filename, header=[0,1])

inner_column_names=list(eis_df.loc[:, unique_names[0]].columns)
wanted_columns=[column_name for column_index, column_name in enumerate(inner_column_names) if column_index in (0, 3, 4, 5)]
# ['freq / Hz', 'Z / Ohm', "Z' / Ohm", "Z'' / Ohm"]

for experiment_name in unique_names:
    experiment_df=eis_df.loc[:, experiment_name]
    reduced_experiment_df=experiment_df[wanted_columns]
    print(experiment_name)
    print(reduced_experiment_df)
    # from here the access is normal :)
