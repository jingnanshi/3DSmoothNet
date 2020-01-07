import os
import subprocess
from pathlib import Path

if __name__ == "__main__":
    cnn_exe = "main_cnn.py"
    input_folder = "../data/evaluate/sdv/3DMatch_dataset/"
    output_folder = "../data/evaluate/output_data/3DMatch_dataset/"

    # load scenes
    all_scenes = [name for name in os.listdir(input_folder)
            if os.path.isdir(os.path.join(input_folder, name))]

    for scene in all_scenes:
        print("Starting inference for %s." % scene)

        # path for inference output (descriptors) for each scene
        descriptor_output_path = os.path.abspath(os.path.join(output_folder, scene))+"/"
        Path(descriptor_output_path).mkdir(parents=True, exist_ok=True)

        sdv_input_path = os.path.abspath(os.path.join(input_folder, scene))+"/" 
        
        cmd_args = "python " + cnn_exe + " --run_mode=test " + "--evaluate_input_folder=" + sdv_input_path +  " --evaluate_output_folder=" + descriptor_output_path

        subprocess.call(cmd_args, shell=True, cwd=os.path.abspath("../"))

