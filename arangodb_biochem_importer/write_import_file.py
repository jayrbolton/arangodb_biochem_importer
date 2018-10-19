import os
import json


def write_import_file(row_gen, output_dir):
    """
    Write out an importable file of JSON import data
    Args:
      generator - yields csv rows to import
      output_path - csv file path to write to
      headers - list of header names
    Returns a dictionary of counts for how many rows generated for each collection
        (keys are collection names, values are counts)
    """
    for (col_name, data) in row_gen:
        json_data = json.dumps(data)
        file_path = os.path.join(output_dir, col_name + '.json')
        with open(file_path, 'a') as fd:
            fd.write(json_data + '\n')
