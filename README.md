# DNA Sequence Feature Analysis

**A self-directed computational biology project using Python**

**Project date:** 9 July 2026

## Overview

This project explores the application of Python programming to basic DNA sequence analysis. Developed as a practical exercise following introductory Python training, the project applies programming concepts and data analysis techniques to extract, organise, compare and visualise features of DNA sequences.

The tool reads DNA sequences from a FASTA file and calculates sequence length, nucleotide composition and GC content. It also generates a structured results table, produces a summary report and visualises GC content across the analysed sequences.

## Project Objectives

- Apply Python programming skills to a biological data analysis task.
- Extract basic sequence features from DNA sequences in FASTA format.
- Calculate and compare GC content across multiple DNA sequences.
- Organise extracted biological data into a structured tabular format.
- Generate a visual representation of GC content distribution.

## Features

The analysis script performs the following operations:

1. **FASTA file parsing:** Reads multiple DNA sequences and their identifiers from a FASTA file.
2. **Sequence length calculation:** Determines the length of each DNA sequence in base pairs.
3. **GC content calculation:** Computes the percentage of guanine (G) and cytosine (C) nucleotides in each sequence.
4. **Nucleotide composition:** Counts the occurrences of adenine (A), thymine (T), guanine (G) and cytosine (C).
5. **Tabular data organisation:** Uses pandas to structure the extracted features into a DataFrame.
6. **Summary statistics:** Reports the total number of sequences, average GC content, longest and shortest sequences, and sequences with the highest and lowest GC content.
7. **Data visualisation:** Uses matplotlib to generate a bar chart comparing the GC content of the analysed sequences.

## Technologies and Libraries

- Python
- pandas
- matplotlib
- FASTA sequence format

## Project Structure

```text
dna-sequence-feature-analysis/
│
├── main.py
├── requirements.txt
├── sample_sequences.fasta
├── dna_sequence_analysis_results.csv
├── gc_content_visualization.png
└── README.md
```

## Installation and Usage

### 1. Clone or download the repository

Download the repository to your computer and open the project directory.

### 2. Install the dependencies

Run the following command:

```bash
pip install -r requirements.txt
```

### 3. Run the analysis

Execute the main Python script:

```bash
python main.py
```

When prompted, enter the name of the FASTA file:

```text
sample_sequences.fasta
```

The script will process the sequences, display the analysis results and summary report, and generate a GC content visualisation.

## Output

The project produces:

- **dna_sequence_analysis.csv:** A tabular file containing sequence identifiers, sequence lengths, GC content percentages and individual nucleotide counts.
- **gc_content_visualization.png:** A bar chart comparing the GC content of the analysed DNA sequences.

## Learning Outcomes

This project provided practical experience in applying Python to biological sequence data, including file handling, basic sequence feature extraction, data manipulation with pandas and scientific visualisation with matplotlib.

It represents an introductory step in developing computational biology and bioinformatics skills through independent, hands-on learning.

## Project Status

Completed: July 2026.
