import os
import shutil


def rename_and_move_videos(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith((".mp4", ".avi", ".mkv")):
                parent_dir = os.path.basename(root)
                new_name = parent_dir + os.path.splitext(file)[1]
                new_path = os.path.join(folder, new_name)
                old_path = os.path.join(root, file)
                shutil.move(old_path, new_path)
                shutil.rmtree(root)
                print(f"Moved and renamed file: {file} to {new_name}")


folder = input("Enter the folder to scan: ")
rename_and_move_videos(folder)
