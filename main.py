from primer_designer import gc_content, melting_temp, reverse_complement, design_primers
from export import save_primers_to_csv

def main():
    dna_seq = input("Enter DNA sequence (A, T, G, C only): ").upper()
    primer_length = int(input("Enter primer length (e.g., 18): "))

    # Design primers
    fwd, rev = design_primers(dna_seq, primer_length)

    # Calculate GC content and melting temp
    fwd_gc = gc_content(fwd)
    rev_gc = gc_content(rev)
    fwd_tm = melting_temp(fwd)
    rev_tm = melting_temp(rev)

    # Print results
    print("\nForward primer: ", fwd)
    print(f"GC content: {fwd_gc}%, Tm: {fwd_tm}°C")
    print("\nReverse primer: ", rev)
    print(f"GC content: {rev_gc}%, Tm: {rev_tm}°C")

    # Save results to CSV
    save_primers_to_csv('primer_results.csv', fwd, rev, fwd_gc, rev_gc, fwd_tm, rev_tm)

if __name__ == "__main__":
    main()

