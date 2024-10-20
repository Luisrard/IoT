#21310369

import os
import pandas as pd
#For windows: pip install pyreadline3
import readline
import glob
import os
import shutil

HEADER_FIELD_FOR_FILE_NAME = 'empresa'

def complete_path(text, state):
    return (glob.glob(os.path.expanduser(text) + '*') + [None])[state]

def input_with_autocomplete(prompt_text):
    readline.set_completer(complete_path)
    readline.parse_and_bind('tab: complete')
    return input(prompt_text)

def read_csv_file(filepath: str):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")
    
    if not filepath.lower().endswith('.csv'):
        raise ValueError(f"The file {filepath} is not a CSV file.")
    
    return pd.read_csv(filepath)

def read_letter_template(filepath: str):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")
    
    with open(filepath, 'r') as file:
        return file.read()

def fomat_letter(template: str, row: pd.Series):
    row_dict = {}
    header_file_name = ''
    for header, value in row.items():
        header_str = str(header).strip()
        value_str = str(value).strip()
        
        row_dict[header_str] = value_str

        if header == HEADER_FIELD_FOR_FILE_NAME:
            header_file_name = value_str
    return header_file_name, template.format(**row_dict)

def generate_letters(csv_filepath: str, letter_filepath: str, output_folder: str):
    csv_data = read_csv_file(csv_filepath)
    letter_template = read_letter_template(letter_filepath)
    
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder) 

    os.makedirs(output_folder)    
    
    for index, row in csv_data.iterrows():
        header_file_name, personalized_letter = fomat_letter(letter_template, row)
        output_filepath = os.path.join(output_folder, f'{index}_{header_file_name}.txt')
        with open(output_filepath, 'w') as output_file:
            output_file.write(personalized_letter)

def main():
    csv_filepath = input_with_autocomplete("Enter the path to the CSV file: ")
    letter_filepath = 'letter.txt'
    output_folder = 'out'
    
    try:
        generate_letters(csv_filepath, letter_filepath, output_folder)
        print("Letters generated successfully.")
    except (FileNotFoundError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()
