def gc_content(seq):
    """Calculate GC content (%) of a DNA sequence."""
    gc_count = seq.count('G') + seq.count('C')
    return round((gc_count / len(seq)) * 100, 2)

def melting_temp(seq):
    """Calculate melting temperature (Tm) using a simple formula:
    Tm = 2°C * (A+T) + 4°C * (G+C)
    (basic Wallace rule, good for primers < 20bp)
    """
    a_count = seq.count('A')
    t_count = seq.count('T')
    g_count = seq.count('G')
    c_count = seq.count('C')
    return 2 * (a_count + t_count) + 4 * (g_count + c_count)

def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    rev_comp = ''.join(complement.get(base, base) for base in reversed(seq))
    return rev_comp

def design_primers(dna_seq, primer_length):
    """Design forward and reverse primers of given length from dna_seq."""
    forward_primer = dna_seq[:primer_length]
    reverse_primer = reverse_complement(dna_seq[-primer_length:])
    return forward_primer, reverse_primer

def main():
    dna_seq = input("Enter DNA sequence (A, T, G, C only): ").upper()
    primer_length = int(input("Enter primer length (e.g., 18): "))

    # Get primers
    fwd, rev = design_primers(dna_seq, primer_length)

    # Calculate stats
    fwd_gc = gc_content(fwd)
    rev_gc = gc_content(rev)
    fwd_tm = melting_temp(fwd)
    rev_tm = melting_temp(rev)

    # Print results
    print("\nForward primer: ", fwd)
    print(f"GC content: {fwd_gc}%, Tm: {fwd_tm}°C")
    print("\nReverse primer: ", rev)
    print(f"GC content: {rev_gc}%, Tm: {rev_tm}°C")

if __name__ == "__main__":
    main()
