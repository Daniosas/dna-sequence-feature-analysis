import pandas as pd
import matplotlib.pyplot as plt

# Read DNA sequences from FASTA file
def read_fasta(filename):
    sequences = {}
    current_sequence = None

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                current_sequence = line[1:]
                sequences[current_sequence] = ""
            else:
                sequences[current_sequence] += line

    return sequences

filename = input("Enter the FASTA filename: ")

try:
    sequences = read_fasta(filename)

except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
    print("Please check the filename and try again.")
    exit()

# Function to calculate GC percentage
def gc_content(seq):
    """
    Calculate the GC content of a DNA sequence.
    Returns the percentage of G and C nucleotides.
    """
    g = seq.count("G")
    c = seq.count("C")
    return ((g + c) / len(seq)) * 100

# Function to count nucleotides
def nucleotide_count(seq):
    return {
        "A": seq.count("A"),
        "T": seq.count("T"),
        "G": seq.count("G"),
        "C": seq.count("C")
    }

# Build dataset
data = []

for name, seq in sequences.items():
    data.append({
        "Sequence": name,
        "Length": len(seq),
        "GC_Content": gc_content(seq),
        **nucleotide_count(seq)
    })

df = pd.DataFrame(data)

df.to_csv("dna_sequence_analysis.csv", index=False)

print(df)

print("\n===== SUMMARY REPORT =====")

print(f"Number of sequences analysed: {len(df)}")

print(f"Average GC content: {df['GC_Content'].mean():.2f}%")

longest = df.loc[df["Length"].idxmax()]
print(f"Longest sequence: {longest['Sequence']} ({longest['Length']} bp)")

shortest = df.loc[df["Length"].idxmin()]
print(f"Shortest sequence: {shortest['Sequence']} ({shortest['Length']} bp)")

highest_gc = df.loc[df["GC_Content"].idxmax()]
print(f"Highest GC content: {highest_gc['Sequence']} ({highest_gc['GC_Content']:.2f}%)")

lowest_gc = df.loc[df["GC_Content"].idxmin()]
print(f"Lowest GC content: {lowest_gc['Sequence']} ({lowest_gc['GC_Content']:.2f}%)")

print("\nAnalysis complete!")
print("Results saved to dna_sequence_analysis.csv")

# Visualization
plt.figure()
plt.bar(df["Sequence"], df["GC_Content"])
plt.title("GC Content of DNA Sequences")
plt.xlabel("Sequence")
plt.ylabel("GC Content (%)")
plt.savefig("gc_content_visualization.png", dpi=300, bbox_inches="tight")
plt.show()