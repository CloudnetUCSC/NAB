import os
from os.path import dirname
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

results_dir = f"{dirname(__file__)}/../results"
input_csv_file_name = "19-09-2023_cron_removed_prefailure"

model_name = "numenta"
model_out_path = f"{results_dir}/{model_name}/vmFailureData"
model_out_file = f"{model_out_path}/{model_name}_{input_csv_file_name}.csv"

plot_title = f"{model_name} - {input_csv_file_name} - timestamp"
plot_save_file = f"{dirname(__file__)}/{plot_title}.png"

model_out_df = pd.read_csv(model_out_file, header=0, index_col="timestamp", parse_dates=True)
print(model_out_df)

plt.plot(model_out_df.index, model_out_df["anomaly_score"], label="Anomaly score")
plt.plot(model_out_df.index, model_out_df["label"], color=(0.8, 0.8, 0.0, 0.7), label="Pre-failure and Failure Label")

plt.plot([datetime.strptime("2023-09-19 09:51:00", "%Y-%m-%d %H:%M:%S") , datetime.strptime("2023-09-19 09:52:00", "%Y-%m-%d %H:%M:%S")], [0, 1], color=(0.8, 0.0, 0.0, 0.7), label="Actual failure point")
# plt.xaxis.set_major_locator(mdates.MinuteLocator(byminute=range(0, 60, 5)))
# plt.xticks(rotation=70)
# plt.locator_params(tight=True)
plt.title(plot_title)
plt.legend()
plt.savefig(plot_save_file, dpi=300)

plt.show()
