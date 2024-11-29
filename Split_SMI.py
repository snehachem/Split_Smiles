# Split a .smi file into smaller files containing 200,000 SMILES strings each

def split_smiles_file(input_file, output_prefix, chunk_size=20000000):
    """
    Splits a .smi file into smaller files.
    
    Parameters:
    - input_file: str, path to the input .smi file
    - output_prefix: str, prefix for the output files
    - chunk_size: int, number of lines per chunk file (default is 200,000)
    """
    try:
        with open(input_file, 'r') as infile:
            file_count = 0
            line_count = 0
            output_file = None
            
            for line in infile:
                # Open a new file for each chunk
                if line_count % chunk_size == 0:
                    if output_file:
                        output_file.close()
                    output_file = open(f"{output_prefix}_{file_count}.smi", 'w')
                    file_count += 1
                
                # Write the line to the current chunk
                output_file.write(line)
                line_count += 1
            
            # Close the last output file
            if output_file:
                output_file.close()
                
        print(f"File split successfully into {file_count} chunks.")
    
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_file = "DrugSpaceX-DL.smi"  # Path to your .smi file
output_prefix = "DrugSpaceX-DL_chunk"  # Prefix for the output files
split_smiles_file(input_file, output_prefix)
