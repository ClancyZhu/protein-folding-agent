def process_sequence(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    sequence = "".join([l.strip() for l in lines if not l.startswith(">")])

    print(f"[DataAgent] Sequence length: {len(sequence)}")

    return sequence
