import string


def clean_up(src_path, dest_path):
    with open(src_path) as source_file:
        with open(dest_path, "w") as dest_file:
            for line in source_file:
                table = string.maketrans(line, line)
                new_line = line.translate(table, string.punctuation)
                dest_file.write(new_line)
            source_file.close()
            dest_file.close()


if __name__ == '__main__':
    # Example used to  clean up the example file
    clean_up('/home/gianluca/Desktop/news', '/home/gianluca/Desktop/write_file')