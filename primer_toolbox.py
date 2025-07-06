## primer_tools.py

# Core bioinformatics functions for primer design

def gc_content(seq):
    """Calculate GC content (%) of a DNA sequence."""
    seq = seq.upper()
    gc_count = seq.count('G') + seq.count('C')
    try:
        return round((gc_count / len(seq)) * 100, 2)
    except ZeroDivisionError:
        return 0.0


def melting_temp(seq):
    """
    Calculate melting temperature (Tm) using Wallace rule:
    Tm = 2°C * (A + T) + 4°C * (G + C)
    """
    seq = seq.upper()
    a_count = seq.count('A')
    t_count = seq.count('T')
    g_count = seq.count('G')
    c_count = seq.count('C')
    return 2 * (a_count + t_count) + 4 * (g_count + c_count)


def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    rev_comp = ''.join(complement.get(base, base) for base in reversed(seq.upper()))
    return rev_comp


def design_primers(seq, primer_length):
    """
    Design forward and reverse primers of given length from a DNA sequence.
    Returns (forward_primer, reverse_primer).
    """
    seq = seq.upper()
    if len(seq) < primer_length:
        raise ValueError("Sequence length is shorter than primer length.")
    forward = seq[:primer_length]
    reverse = reverse_complement(seq[-primer_length:])
    return forward, reverse
