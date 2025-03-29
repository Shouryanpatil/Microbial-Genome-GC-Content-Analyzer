# Microbial Genome GC Content Analyzer

## Overview
This Python script analyzes GC content in microbial genomes. It processes FASTA files and provides various GC content analyses, including overall GC content, GC distribution across a sequence, and comparisons across multiple sequences.

## Features
- **Load multiple sequences** from separate FASTA files or a multi-sequence FASTA file.
- **Calculate GC content** for each sequence.
- **Analyze GC content distribution** across a sequence with a default window size of 1000.
- **Show GC content statistics** (mean, median, standard deviation).
- **Export results** to a CSV file.
- **Compare multiple sequences** using a bar chart.

## Installation
### Requirements
Ensure you have Python installed (Python 3.x recommended). Install dependencies using:
```sh
pip install biopython matplotlib
```

## Usage
### 1. Prepare Data
Place your FASTA files in the `data/` folder. You can:
- Use multiple FASTA files (e.g., `ecoli.fasta`, `salmonella.fasta`, `bacillus.fasta`).
- Use a single multi-sequence FASTA file containing multiple sequences.

### 2. Run the Script
Execute the script:
```sh
python gc_analyzer.py
```

### 3. Choose an Option
The script provides the following menu:
```
Microbial Genome GC Content Analyzer
1. Calculate GC content
2. Analyze GC distribution (default window: 1000)
3. Show GC statistics
4. Export results to CSV
5. Compare Sequences
6. Exit
```
#### Example Operations
- **Calculate GC content:** Displays the GC content for each loaded sequence.
- **Analyze GC distribution:** Plots the GC content variation over a sequence.
- **Show GC statistics:** Displays mean, median, and standard deviation of GC content.
- **Export results:** Saves GC content data to a CSV file.
- **Compare Sequences:** Generates a bar chart comparing GC content across sequences.

## Example Output
```
Loaded 3 sequences successfully.
Sequence ecoli NC_000913.3: GC Content = 50.79%
Sequence salmonella NZ_CP009273.1: GC Content = 52.15%
Sequence bacillus NC_000964.3: GC Content = 35.42%
```

## Contributing
Feel free to submit pull requests or report issues on [GitHub](https://github.com/yourusername/repository-name).

## License
This project is licensed under the MIT License.

