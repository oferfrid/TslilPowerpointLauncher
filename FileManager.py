import glob, os


def get_files_path(path, extantions=('stl','zip')):
    files_path = []
    for ext in extantions:
        files_path+= [file for file in glob.glob(os.path.join(path,'*.{}'.format(ext)))]
    return files_path

def get_sorted_files(files_path):
    file_names = [os.path.basename(fp) for fp in files_path]
    sorted_file_names,  sorted_files_path = list(zip(*[(n,p) for n,p in sorted(zip(file_names,files_path))]))
    return sorted_file_names, sorted_files_path

def main():
    fp = get_files_path(r'C:\Users\oferfrid\Downloads\ppt')
    sorted_file_names, sorted_files_path = get_sorted_files(fp)




if __name__ == '__main__':
    main()