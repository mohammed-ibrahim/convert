import json
import expr_evaluator
import os
import sys

def convert():

    if len(sys.argv) != 4:
        log.error('Usage: $ python <python_src_file> <input_fmt> <output_fmt> <value_to_convert>')
        return None

    rules_file_name = 'rules.json'
    current_file_directory = os.path.dirname(os.path.realpath(__file__)) 
    rules_file_path = os.path.join(current_file_directory, rules_file_name)
    contents = None

    try:
        with open(rules_file_path, 'r') as file_stream:
            contents = json.load(file_stream)
    except Exception as e:
        print 'Failed to load the rules file' + str(rules_file_path)
        return None

    from_route = sys.argv[1]
    to_route = sys.argv[2]
    value = sys.argv[3]

    if from_route not in contents['inputs']:
        print 'Unknows unit type: ' + str(from_route)
        return

    if to_route not in contents['inputs']:
        print 'Unknows unit type: ' + str(to_route)
        return

    if not str(value).replace('.', '').isdigit():
        print 'value_to_convert should be an integer'
        return

    f_alias = contents['inputs'][from_route]['alias']
    t_alias = contents['inputs'][to_route]['alias']

    print expr_evaluator.evaluate(contents['routes'], f_alias + '_' + t_alias, float(value))
    return None

convert()
