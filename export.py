import csv

def save_primers_to_csv(filename, forward_primer, reverse_primer, fwd_gc, rev_gc, fwd_tm, rev_tm):
    """Save primer information to a CSV file."""

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Primer', 'Sequence', 'GC Content (%)', 'Melting Temp (°C)'])
        writer.writerow(['Forward', forward_primer, fwd_gc, fwd_tm])
        writer.writerow(['Reverse', reverse_primer, rev_gc, rev_tm])

    print(f"Results saved to {filename}")

