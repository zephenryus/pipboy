import os

from kivy.lang import Builder


def load_kv(screen_instance):
    # Get the module path and replace dots with OS-specific path separators
    module_path = screen_instance.__module__.replace('.', os.sep)
    # Split the module path to a list to manipulate the path
    module_path_list = module_path.split(os.sep)
    # Replace the 'screens' directory with 'kv'
    module_path_list[module_path_list.index('screens')] = 'kv'
    # Construct the KV file name
    module_path_list[-1] = os.path.splitext(os.path.basename(module_path))[0] + '.kv'
    # Join the path components to get the absolute path to the KV file
    kv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', *module_path_list))
    print(f"Loading KV file from: {kv_path}")
    with open(kv_path, 'r') as f:
        print(f"KV file content:\n{f.read()}")
    Builder.unload_file(kv_path)
    Builder.load_file(kv_path)
    print("KV file loaded")
