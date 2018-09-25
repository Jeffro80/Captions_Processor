# Captions Processor
# Jeff Mitchell
# Version 2.0125 September 2018
# Removes timestamps from captions files

# To Do:

# - Add menu options
# - Automatically create save file name from load file name

import custtools.admintools as ad
import custtools.filetools as ft


def combine_captions(processed_captions):
    """Combines a list of captions into one string.

    Args:
        processed_captions (list): The processed captions.

    Returns:
        caption (str): All captions as one string.
    """
    caption = ''
    for item in processed_captions:
        caption = '{} {}'.format(caption, item)
    # print(caption)
    # Remove initial space
    caption = caption[1:]
    return caption


def main():
    main_message()
    repeat = True
    while repeat:
        print('\nPlease select the file to be processed\n')
        file_name = ft.get_load_file_name_picker()
        # print('File name: {}'.format(file_name))
        source_captions = ft.load_sbv(file_name)
        # ad.debug_list(captions)
        # Remove timestamps
        processed_captions = process_captions(source_captions)
        captions = []
        captions.append(processed_captions)
        save_name = input('Please enter the name of file to save captions to '
                          '--> ') + '.txt'
        ft.save_list_to_text(captions, save_name)
        if not ad.check_repeat():
            repeat = False


def main_message():
    """Print the welcome message."""
    print('\n\n*************==========================*****************')
    print('\nCaptions Processor version 2.01')
    print('Created by Jeff Mitchell, 2018')


def process_captions(captions):
    """Removes timestamps from captions.

    Removes lines starting with a '0' and returns a list with just the lines
    containing text.

    Args:
        captions (list): List of captions from source data.

    Returns:
        processed_captions (list): Captions with timestamps removed.
    """
    processed_captions = []
    excluded = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','[']
    for line in captions:
        # print(line)
        if len(line) < 1:
            continue
        elif line[0] in excluded:
            continue
        else:
            processed_captions.append(line)
    long_caption = combine_captions(processed_captions)
    return long_caption


if __name__ == '__main__':
    main()
