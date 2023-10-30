import unittest


class TestFileViewerMethods(unittest.TestCase):
    def test_get_file_contents_when_path_doesnt_exist(self):
        # do what's needed to raise the exception
        self.assertTrue(True)

    def test_get_file_contents_with_multiple_files(self):
        self.assertTrue(True)

    ##
    # Bonus (start)
    ##
    # def test_list_files_in_folder_empty(self):
    #     self.assertTrue(False)

    # def test_list_files_in_folder_with_one_file(self):
    #     self.assertTrue(False)

    # def test_list_files_in_folder_with_multiple_files(self):
    #     self.assertTrue(False)

    # def test_list_files_in_folder_with_multiple_files_and_folders(self):
    #     self.assertTrue(False)

    ##
    # Bonus (end)
    ##


if __name__ == '__main__':
    unittest.main()