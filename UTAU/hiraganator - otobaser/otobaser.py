import utils

def process_file(file_name):
    with open(file_name, 'r', encoding="utf8") as file:
        lines = file.readlines()

    result = []

    for line in lines:
        line = line.strip()
        if line:
            aliases = line.split('_')
            original_text = '_'.join(aliases)

            if all(alias in ['a', 'e', 'i', 'o', 'u', 'an', 'en', 'in', 'on', 'un', 'eh', 'oh', 'br', 'n'] for alias in aliases):
                for i, alias in enumerate(aliases):
                    if i == 0:
                        result.append(f'{original_text}.wav=- {alias},0,0,0,0,0')
                    else:
                        result.append(f'{original_text}.wav={aliases[i-1]} {alias},0,0,0,0,0')
            else:
                for alias in aliases:
                    result.append(f'{original_text}.wav={alias},0,0,0,0,0')

    return result

def write_output(file_name, output):
    with open(file_name, 'w', encoding="utf8") as file:
        for line in output:
            file.write(line + '\n')

# Read and process the file
file_name = 'reclist.txt'
output = process_file(file_name)

# Write the output to a new file
output_file_name = 'oto.ini'
write_output(output_file_name, output)
