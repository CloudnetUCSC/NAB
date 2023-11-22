import json
import os
from os.path import dirname
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

results_dir = f"{dirname(__file__)}/../results"
plot_out_dir = f"{dirname(__file__)}/plotOut"
dataset_metadata_json_file = f"{dirname(__file__)}/../labels/vmFailure_metadata.json"
plot_metadata = json.load(open(dataset_metadata_json_file))

model_name = "numenta"
input_csv_file_name = "2023-11-08_unlabelled.csv"


model_out_path = f"{results_dir}/{model_name}/vmFailureData"
model_out_file = f"{model_out_path}/{model_name}_{input_csv_file_name}"

plot_title = f"{model_name} - {input_csv_file_name.split('.')[0]}"
plot_save_file = f"{plot_out_dir}/{plot_title}"


model_out_df = pd.read_csv(model_out_file, header=0, parse_dates=True)

plt.plot(model_out_df.index, model_out_df["anomaly_score"], label="Anomaly score")
plt.plot(model_out_df.index, model_out_df["label"], color=(0.8, 0.8, 0.0, 0.7), label="Pre-failure and Failure Label")

failure_point = plot_metadata[input_csv_file_name]["failure_point"]
if failure_point:
    plt.axvline(x=failure_point, color=(0.8, 0.0, 0.0, 0.7), label="Actual failure point")

training_region = plot_metadata[input_csv_file_name]["training_region"]
plt.plot([training_region[0], training_region[1], training_region[1]+1], [1, 1, 0], color=(0.0, 0.0, 0.0, 0.7), label="Training region")
plt.fill_between([training_region[0], training_region[1], training_region[1]+1], [1, 1, 0], color=(0.0, 0.0, 0.0, 0.3))

plt.title(plot_title)
plt.legend()
plt.savefig(plot_save_file + ".png", dpi=300)
plt.show()


# model_out_ts_df = pd.read_csv(model_out_file, header=0, index_col="timestamp", parse_dates=True)
# model_out_ts_df["timestamp"] = model_out_ts_df.index
# plt.plot(model_out_ts_df.index, model_out_ts_df["anomaly_score"], label="Anomaly score")
# plt.plot(model_out_ts_df.index, model_out_ts_df["label"], color=(0.8, 0.8, 0.0, 0.7), label="Pre-failure and Failure Label")

# failure_point_timestamp = model_out_ts_df["timestamp"].iloc[failure_point]
# plt.axvline(x=failure_point_timestamp, color=(0.8, 0.0, 0.0, 0.7), label="Actual failure point")

# training_region = plot_metadata[input_csv_file_name]["training_region"]
# training_region_ts = [
#     model_out_ts_df["timestamp"].iloc[training_region[0]],
#     model_out_ts_df["timestamp"].iloc[training_region[1]],
#     model_out_ts_df["timestamp"].iloc[training_region[1]+1],
# ]
# plt.plot(training_region_ts, [1, 1, 0], color=(0.0, 0.0, 0.0, 0.7), label="Training region")
# plt.fill_between(training_region_ts, [1, 1, 0], color=(0.0, 0.0, 0.0, 0.3))

# plt.plot([datetime.strptime("2023-09-19 09:51:00", "%Y-%m-%d %H:%M:%S") , datetime.strptime("2023-09-19 09:52:00", "%Y-%m-%d %H:%M:%S")], [0, 1], color=(0.8, 0.0, 0.0, 0.7), label="Actual failure point")
# plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator(minticks=25))
# plt.xticks(rotation=90, fontsize='xx-small')

# plt.title(plot_title + " timestamp")
# plt.legend()
# plt.savefig(plot_save_file + "_timestamp.png", dpi=300)
# plt.show()
