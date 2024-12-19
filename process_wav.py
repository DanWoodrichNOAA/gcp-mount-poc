import os
import hashlib
import csv

def calculate_md5(file_path):
    """Calculate MD5 hash of a file's contents."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def process_directory():
    """Process all .wav files in the /input directory and write MD5 hashes to /output/results.csv."""
    input_dir = "/input"
    output_csv = "/output/results.csv"


    if os.path.isdir(input_dir):
        print("input dir exists")

    if os.path.isdir(os.path.dirname(output_csv)):
        print("output dir exists")

    print([f for f in os.listdir(input_dir)])
    wav_files = [f for f in os.listdir(input_dir) if f.endswith(".aif")]

    print(f"wav files found:{wav_files}")

    with open(output_csv, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Filename", "MD5 Hash"])
        for wav_file in wav_files:
            file_path = os.path.join(input_dir, wav_file)
            md5_hash = calculate_md5(file_path)
            writer.writerow([wav_file, md5_hash])

if __name__ == "__main__":
    print('starting script')

    process_directory() 