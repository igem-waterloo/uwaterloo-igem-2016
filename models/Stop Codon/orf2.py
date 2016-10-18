def get_orf(seq):
    start = 'atg'
    ends = ['tag', 'tga', 'taa']
    last_idx = len(seq) - 3
    orfs = []
    idx = 0
    start_idx = 0
    stop_idx = 0
    while idx < last_idx:
        if seq[idx : idx + 3] == start:
            idx += 3
            start_idx = idx
            while idx < last_idx and seq[idx : idx + 3] not in ends:
                idx += 3
            stop_idx = idx
            orfs.append(seq[start_idx : stop_idx])
        else:
            idx += 1
    return orfs

