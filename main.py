import os
import shutil


def rename_and_move_videos(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith((".mp4", ".avi", ".mkv")):
                if root != folder and root != os.path.join(folder, file):
                    if "sample" in file.lower():
                        os.remove(os.path.join(root, file))
                        print(f"Removed file: {file}")
                    elif "copy" in file.lower():
                        os.remove(os.path.join(root, file))
                        print(f"Removed file: {file}")
                    else:
                        parent_dir = os.path.basename(root)
                        new_name = parent_dir + os.path.splitext(file)[1]
                        new_path = os.path.join(folder, new_name)
                        old_path = os.path.join(root, file)
                        shutil.move(old_path, new_path)
                        shutil.rmtree(root)
                        print(f"Moved and renamed file: {file} to {new_name}")
            else:
                try:
                    os.remove(os.path.join(root, file))
                    print(f"Removed non-video file: {file}")
                except FileNotFoundError:
                    print(f"Tried to remove but File not found: {file}")


folder = input("Enter the folder to scan: ")
rename_and_move_videos(folder)
