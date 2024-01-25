import pathlib
from   typing   import List, Optional
import yaml

def encoding_from_character_yaml(path_otoini:pathlib.Path) -> str:
    # Get the encoding of the oto.ini from OpenUtau character.yaml if exist
    # Character.yaml might appear at any parent folder of the oto.ini
    # If not found, use cp932
    path_character_yaml: Optional[pathlib.Path] = None
    for parent in pathlib.Path(path_otoini).absolute().parents:
        if(parent / 'character.yaml').is_file() and (parent / 'character.txt').is_file():
            path_character_yaml = parent / 'character.yaml'
            break
    oto_encoding = 'cp932'
    if path_character_yaml is not None:
        print(f"character.yaml found: {path_character_yaml}")
        with open(path_character_yaml, 'r', encoding='utf-8') as f:
            character_yaml = yaml.safe_load(f)
            if('text_file_encoding' in character_yaml):
                oto_encoding = character_yaml['text_file_encoding']
                print(f"oto.ini encoding: {oto_encoding}")
            else:
                print(f"text_file_encoding not found in character.yaml, using cp932")
    else:
        print(f"character.yaml not found, using cp932")
    return oto_encoding