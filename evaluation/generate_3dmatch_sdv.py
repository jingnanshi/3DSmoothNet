import os
import subprocess
from pathlib import Path

if __name__ == "__main__":
    # path to the dataset
    data_path = "../data/evaluate/input_data/3DMatch_dataset/"
    keypoints_dir = "01_Keypoints"

    # path to sdv parametrization executable
    sdv_exe = "../3DSmoothNet"
    sdv_path = "../data/evaluate/sdv/3DMatch_dataset/"


    # get all scenes
    all_scenes = [name for name in os.listdir(data_path)
            if os.path.isdir(os.path.join(data_path, name))]

    # for all the ply files in each scene
    # run input parametrization
    for scene in all_scenes:
        print("Starting input parametrization for %s." % scene)
        # path of sdv parametrization output
        sdv_output_path = os.path.abspath(os.path.join(sdv_path, scene))
        Path(sdv_output_path).mkdir(parents=True, exist_ok=True)

        scene_path = os.path.join(data_path, scene)

        point_cloud_files = [pname 
                for pname in os.listdir(scene_path) if pname.endswith(".ply")]

        for pc_file in point_cloud_files:
            pc_name = pc_file.split(".")[0]
            ky_name = pc_name + "Keypoints.txt"

            pc_path = os.path.abspath(os.path.join(scene_path, pc_file))
            ky_path = os.path.abspath(os.path.join(scene_path, keypoints_dir, ky_name))

            cmd_args = sdv_exe +  " -f " + pc_path + " -k " + ky_path +  " -o " + sdv_output_path
            subprocess.call(cmd_args, shell=True)

        print("Scene %s parametrization complete." % scene)

    print("All parametrization complete.")

