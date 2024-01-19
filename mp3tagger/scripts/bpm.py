# Get the filter string for bpm attributes
def get_bpm_filter(bpm_list):
    # Get the low and high bpms
    bpmLow = bpm_list[0]
    bpmHi = bpm_list[1]

    # Include a secondary bpm range, either double or halved
    if bpmLow > 80:
        bpmLow2 = int(bpmLow / 2)
        bpmHi2 = int(bpmHi / 2)
    else:
        bpmLow2 = int(bpmLow * 2)
        bpmHi2 = int(bpmHi * 2)

    filter = f"((NOT BPM LESS {bpmLow} AND NOT BPM GREATER {bpmHi}) OR (NOT BPM LESS {bpmLow2} AND NOT BPM GREATER {bpmHi2})) AND "

    return filter
