## This script processes the Allen Brain Institute lfp .nwb file to .csv

from pynwb import NWBHDF5IO
import pandas as pd

# load the NWB file
nwb_file_path = '/Users/hannahghaffari/Documents/Mehta_lab/ecephys_cache_dir/session_746083955/probe_760647911_lfp.nwb'
io = NWBHDF5IO(nwb_file_path, 'r')
nwbfile = io.read()

# list all acquisition keys
acquisition_keys = list(nwbfile.acquisition.keys())   
print("Available acquisition keys:", acquisition_keys)

# access LFP data
lfp = nwbfile.acquisition['probe_760647911_lfp_data']
lfp_data = lfp.data[:]
timestamps = lfp.timestamps[:]

print("Timestamps shape:", timestamps.shape)
print("LFP data shape:", lfp_data.shape)

electrode_table = lfp.electrodes
channel_ids = electrode_table.table['id'][electrode_table.data[:]]
print("Channel IDs:", electrode_table.table['id'][electrode_table.data[:]])
col_names = [f"Ch{i+1}_{channel_id}" for i, channel_id in enumerate(channel_ids)]

# create df with each channel data in separate column
df = pd.DataFrame(lfp_data, columns=col_names)
df['Timestamp'] = timestamps
df = df[['Timestamp'] + [col for col in df.columns if col != 'Timestamp']]

output_csv_path = '/Users/hannahghaffari/Documents/Mehta_lab/ecephys_cache_dir/session_746083955/probe_760647911_lfp_data.csv'
df.to_csv(output_csv_path, index=False)

io.close()

print('done')
