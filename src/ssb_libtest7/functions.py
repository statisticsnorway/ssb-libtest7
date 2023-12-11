"""A collection of useful functions.

The template and this example uses Google style docstrings as described at:
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

"""

from dapla import FileClient

fs = FileClient.get_gcs_file_system()


def move_gcs_folder(from_folder: str, to_folder: str):
    """Move all files inn a given gcs "folder" """
    for from_path in fs.ls(from_folder):
        to_path = f"{to_folder}/{from_path.split('/')[-1]}"
        fs.cp(from_path, to_path)
