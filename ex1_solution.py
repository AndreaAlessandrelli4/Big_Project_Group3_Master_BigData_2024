# Given the input file ‘lego_sets.jsonl’ in JSONL format, extract all records that match these conditions:
# - Lego sets included in date [2000, 2010]
# - Number of pieces in the set >= 70
# Write the output to another JSONL file.


# Import JSON module
import json

def filter_records_json(input_file, output_file, start_year, end_year, min_pieces):

    # Open input file and output file
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:

       # Iterate over JSON records...
        for line in infile:

            # Load a JSON record
            record = json.loads(line)

            # Verify correct JSON data format.
            try:
                year = int(record["year"]) # Convert year to integer
                pieces = int(record["pieces"])
            except ValueError:
                continue # Skip records with invalid year or number of pieces

            # Check if the record meets the defined filter.
            if start_year <= year <= end_year and pieces > min_pieces:

                # If yes, write teh record on output file.
                json.dump(record, outfile)
                outfile.write('\n') # Write each record in JSONL format


if __name__ == "__main__":
    # Example usage
    filter_records_json('../lego_sets.jsonl', 'filtered_output.jsonl', 2000, 2010, 70)
