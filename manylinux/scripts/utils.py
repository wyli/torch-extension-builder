import subprocess

def get_ptcu_code():
    from torch import __version__
    torch_version = "".join(__version__.split(".")[:2])
    cuda_version = __version__.split("+cu")[-1]
    return "pt" + torch_version + "cu" + cuda_version

def unpack_wheel(wheel_path, directory=None):
    if directory == None:
        subprocess.check_output(["python", "-m", "wheel", "unpack", wheel_path])
    else:
        subprocess.check_output(["python", "-m", "wheel", "unpack", wheel_path, "-d", directory])

def pack_wheel(input_directory, output_directory):
    subprocess.check_output(["python", "-m", "wheel", "pack", input_directory, "-d", output_directory])

def replace_dependancy(library, original_dep, new_dep):
    print(f"patchelf --replace-needed {original_dep} {new_dep} {library}")
    subprocess.check_output(["patchelf", "--replace-needed", original_dep, new_dep, library])

def write_rpath(library, rpath):
    print(f"patchelf --set-rpath {rpath} {library}")
    subprocess.check_output(["patchelf", "--set-rpath", rpath, library])
