# Split_Smiles
This simple Python Script can split large .smi (SMILES) fies in to user define small chunks.
open the script using a text editor
fiend the line "def split_smiles_file(input_file, output_prefix, chunk_size=20000000):" ----> Line No 3.
Put value to chunk_size=**20000000** as per your requirment.

fiend input_file = "DrugSpaceX-DL.smi"  # Path to your .smi file.
output_prefix = "DrugSpaceX-DL_chunk"  # Prefix for the output files ------> Line 40,41 at the ned of the script.
provide the input file name and output file name.
keep the input file and script in side the same folde.
open the terminal and run the script by executing following comand **python Split_SMI.py**.
