import os
import struct
import json
from B3DParser import B3DTree

class B3DToJsonConverter:
    def __init__(self, parser):
        self.parser = parser

    def convert(self, filepath):
        data = self.parser.parse(filepath)
        return data

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print('Usage: b3d_to_json.py [input.b3d] [output.json]')
        sys.exit(0)

    filepath = sys.argv[1]
    output_file = sys.argv[2]
    
    parser = B3DTree()
    converter = B3DToJsonConverter(parser)
    result = converter.convert(filepath)

    
    with open(output_file, "w") as json_file:
        json.dump(result, json_file, indent=1)

    print(f"Conversion successful. Output saved to {output_file}")
