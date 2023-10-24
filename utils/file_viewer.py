import os
from pathlib import PurePath, Path


class FileViewer:
    def list_files_in_folder(self, folder: str) -> [str]:
        return [f for f in os.listdir(folder) if os.path.isfile(folder + '/' + f)]

    def get_file_contents(self, filenames: [str], path_to_files: str) -> dict:
        aggregated_content = dict()

        if not os.path.isdir(path_to_files):
            # log here
            raise NotADirectoryError

        for filename in filenames:
            book_fullpath = PurePath(path_to_files, filename)
            book_content = Path(book_fullpath).read_text()
            aggregated_content[filename] = book_content

        return aggregated_content
