from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import matplotlib.pyplot as plt
import os

data_folder = "data/"

def load_sequences():
    sequences = {}
    file_map = {}
    for file_name in os.listdir(data_folder):
        if file_name.endswith(".fasta"):
            file_path = os.path.join(data_folder, file_name)
            for record in SeqIO.parse(file_path, "fasta"):
                sequences[record.id] = (file_name, record.seq)
                file_map[record.id] = file_name
    print(f"Loaded {len(sequences)} sequences successfully")
    return sequences, file_map

def calculate_gc(sequences):
    results = {seq_id: gc_fraction(seq[1]) * 100 for seq_id, seq in sequences.items()}
    for seq_id, gc in results.items():
        print(f"{sequences[seq_id][0]} {seq_id}: GC Content = {gc:.2f}%")
    return results

def analyze_gc_distribution(sequences, sequence_id, window_size=1000):
    if sequence_id not in sequences:
        print(f"Sequence {sequence_id} not found")
        return
    sequence = sequences[sequence_id][1]
    gc_windows = [gc_fraction(sequence[i:i + window_size]) * 100 for i in range(0, len(sequence) - window_size + 1, window_size)]
    positions = list(range(0, len(sequence) - window_size + 1, window_size))
    plt.figure(figsize=(10, 6))
    plt.plot(positions, gc_windows, color='blue')
    plt.title(f"GC Content Distribution - {sequences[sequence_id][0]} {sequence_id}")
    plt.xlabel("Position in Sequence")
    plt.ylabel("GC Content (%)")
    plt.grid(True)
    plt.show()

def show_gc_statistics(sequences, sequence_id, window_size=1000):
    if sequence_id not in sequences:
        print(f"Sequence {sequence_id} not found")
        return
    sequence = sequences[sequence_id][1]
    gc_windows = [gc_fraction(sequence[i:i + window_size]) * 100 for i in range(0, len(sequence) - window_size + 1, window_size)]
    if gc_windows:
        mean_gc = sum(gc_windows) / len(gc_windows)
        median_gc = sorted(gc_windows)[len(gc_windows) // 2]
        std_gc = (sum((x - mean_gc) ** 2 for x in gc_windows) / len(gc_windows)) ** 0.5
        print(f"GC Statistics for {sequences[sequence_id][0]} {sequence_id}:")
        print(f"Mean GC: {mean_gc:.2f}%")
        print(f"Median GC: {median_gc:.2f}%")
        print(f"Standard Deviation: {std_gc:.2f}%")

def export_results(sequences, filename="gc_results.csv"):
    results = calculate_gc(sequences)
    with open(filename, 'w') as f:
        f.write("File Name,Sequence ID,GC Content (%)\n")
        for seq_id, gc in results.items():
            f.write(f"{sequences[seq_id][0]},{seq_id},{gc:.2f}\n")
    print(f"Results saved to {filename}")

def compare_sequences(sequences):
    results = calculate_gc(sequences)
    plt.figure(figsize=(10, 6))
    plt.bar(results.keys(), results.values(), color='green')
    plt.xticks(rotation=45)
    plt.ylabel("GC Content (%)")
    plt.title("GC Content Across Sequences")
    plt.tight_layout()
    plt.show()

def main():
    sequences, file_map = load_sequences()
    while True:
        print("\nMicrobial Genome GC Content Analyzer")
        print("1. Calculate GC content")
        print("2. Analyze GC distribution (default window: 1000)")
        print("3. Show GC statistics")
        print("4. Export results to CSV")
        print("5. Compare Sequences")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            calculate_gc(sequences)
        elif choice == "2":
            seq_id = input("Enter sequence ID: ")
            analyze_gc_distribution(sequences, seq_id)
        elif choice == "3":
            seq_id = input("Enter sequence ID: ")
            show_gc_statistics(sequences, seq_id)
        elif choice == "4":
            filename = input("Enter output filename (default: gc_results.csv): ") or "gc_results.csv"
            export_results(sequences, filename)
        elif choice == "5":
            compare_sequences(sequences)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
