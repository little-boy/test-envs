import json
import os
from pathlib import Path

from utils.file_viewer import FileViewer

result_file = './tmp/book_synthesis.txt'
path_to_books = './data/books'

file_viewer = FileViewer()

# get list of books
books = file_viewer.list_files_in_folder(path_to_books)

# reset file content
os.truncate(result_file, 0)

# get book contents
books_synthesis = file_viewer.get_file_contents(books, path_to_books)

# write file as json
serialized_book_synthesis = json.dumps(books_synthesis, sort_keys=True, indent=4)
Path(result_file).write_text(serialized_book_synthesis)
