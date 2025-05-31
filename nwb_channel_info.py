## Get channel, electrode ID, and location info from the probe .nwb file

from pynwb import NWBHDF5IO

with NWBHDF5IO('/Users/hannahghaffari/Documents/Mehta_lab/ecephys_cache_dir/session_746083955/probe_760647913_lfp.nwb', 'r') as io:
	nwbfile = io.read()

	electrodes = nwbfile.electrodes
	
	count = 0
	for i in range(len(electrodes)):
		count += 1
		electrode_id = electrodes.id[i]
		location = electrodes['location'][i] if 'location' in electrodes else 'N/A'
        	
		print(f"Channel: {count}")
		print(f"Electrode ID: {electrode_id}")
		print(f"Location: {location}")
		print("---")
