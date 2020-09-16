import os,sys,inspect
import importlib.util
import json

def main():
    # Load scripts module
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(scripts_dir)
    sys.path.insert(0, parent_dir)

    # One argument is required
    if len(sys.argv) >= 2:
        if sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print("""
            Usage: specify the path of the fixture python file.
            If no path is specified all python files that are inside
            a 'fixtures' folder will be executed
            """)
            return
        run(os.path.abspath(sys.argv[1]))
    else:
        root_dir = os.path.dirname(parent_dir)
        for dirpath, dirs, files in os.walk(parent_dir):
            for file in files:
                is_fixture = os.path.basename(dirpath) == 'fixtures'
                if file.endswith('.py') and is_fixture:
                    run(f'{dirpath}/{file}')


def run(path):
    # Load fixture module
    spec = importlib.util.spec_from_file_location("module.name", path)
    m_fixture = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m_fixture)

    # Output generated fixture to a json file
    fixtures = m_fixture.create()
    filename = os.path.basename(path).split('.')[0]
    json_path = f'{os.path.dirname(path)}/{filename}.json'

    f = open(json_path, 'w+')
    f.write(json.dumps(fixtures, indent=2))
    f.close()


if __name__ == '__main__':
    main()