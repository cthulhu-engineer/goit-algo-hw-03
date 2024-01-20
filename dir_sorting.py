import os
import shutil
import sys


def copy_and_sort_files(src_dir, dest_dir, ext_folder_map=None):
    if ext_folder_map is None:
        ext_folder_map = {}

    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)

        try:
            if os.path.isdir(item_path):
                copy_and_sort_files(item_path, dest_dir, ext_folder_map)
            else:
                file_ext = os.path.splitext(item)[-1].lower()
                dest_folder = ext_folder_map.get(file_ext, os.path.join(dest_dir, file_ext[1:]))

                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)

                shutil.copy(item_path, os.path.join(dest_folder, item))
        except PermissionError:
            print(f"Permission denied: {item_path}")
        except FileNotFoundError:
            print(f"File not found: {item_path}")
        except Exception as error:
            print(f"Error copying {item_path}: {error}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [destination_directory]")
        sys.exit(1)

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        copy_and_sort_files(src_dir, dest_dir)
    except Exception as error:
        print(f"Error processing directories: {error}")


if __name__ == "__main__":
    main()
