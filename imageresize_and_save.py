import os
import cv2
import sys
import argparse
from loguru import logger


class Imagesavingresizer():

    def __init__(self, _input_path, _output_path, _size_ratio):
        self.input_path = _input_path
        self.output_path = _output_path
        self.new_size_ratio = _size_ratio

        file_names = os.listdir(self.input_path)
        self.file_extensions_for_resize = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')
        self.file_paths = [os.path.join(self.input_path, x) for x in file_names
                           if x.lower().endswith(self.file_extensions_for_resize)]

    def open_resize_add_save(self):
        files_num = len(self.file_paths)

        for f_num, f_path in enumerate(self.file_paths):

            f_name = f_path.split(os.sep)[-1]

            try:
                img = cv2.imread(f_path)
                img = cv2.resize(img, (0, 0), fx=self.new_size_ratio, fy=self.new_size_ratio)
                cv2.imwrite(os.path.join(self.output_path, f_name), img)
                logger.info(f'{f_num}/{files_num} Done')
            except:
                e = sys.exc_info()[0]
                logger.info(f'An error occurred: {e}')
                logger.info(f'Error with file path: {f_path}')

        logger.info('Resize done.')
        logger.info(f'Resized files saved to: {self.output_path}')

    def check_old_and_new_num_of_files(self):
        old_files_names_len = len(os.listdir(self.input_path))
        new_file_names_len = len(os.listdir(self.output_path))

        if old_files_names_len == new_file_names_len:
            logger.info(f'All files where resized - total num {new_file_names_len}')
        else:
            logger.info(
                f'Old files num: {old_files_names_len}, New files num: {new_file_names_len} -'
                f' NOT all files where resized. That could be because of errors or images extensions.')
            logger.info(f'File extensions included: {self.file_extensions_for_resize}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir_path', required=True, type=str, help="input directory with images")
    parser.add_argument('-o', '--output_dir_path', required=True, type=str, help="output directory for resized")
    parser.add_argument('-s', '--sizeratio', type=float, default=0.25,
                        help="0.25 to get images 4 times smaller. choose from 0 to 1 float")

    args = parser.parse_args()

    isr = Imagesavingresizer(args.input_dir_path, args.output_dir_path, args.sizeratio)

    isr.open_resize_add_save()
    isr.check_old_and_new_num_of_files()
