import sys
from collections import defaultdict
from pathlib import Path
import shutil

class FilesSortAndCopy:
    DEFAULT_DEST = "dist"
    def __init__(self, src=None, dest=None) -> None:
        self.src = src
        self.dest = dest
        if self.src:
            self.__call__()

    @property
    def src(self):
        return self.__src

    @property
    def dest(self):
        return self.__dest

    @src.setter
    def src(self, new_value):
        self.__src = self._src_validate(new_value)

    @dest.setter
    def dest(self, new_value):
        self.__dest = self._dest_validate(new_value)

    def _src_validate(self, new_value):
        if new_value is None:
            return None
        src = Path(new_value)
        if not src.is_dir():
            raise Exception(f"Source directory {src} is not valid")
        return src

    def _dest_validate(self, new_value):
        if new_value is None:
            return None
        dst = Path(new_value)
        if dst.exists():
            if not dst.is_dir():
                raise Exception(f"Destination directory {dst} cannot be used")
            if any(dst.iterdir()):
                raise Exception(f"Destination directory {dst} is not empty")
        return dst

    def __call__(self, src=None, dest=None):
        src_ = self._src_validate(src) if src else self.__src
        if not src_:
            raise Exception(f"Please set source directory")
        if dest:
            dest_ = self._dest_validate(dest)
        else:
            dest_ = self.__dest or self._dest_validate(src_.resolve().parent / FilesSortAndCopy.DEFAULT_DEST)

        print(f"Source directory: {src_}")
        print(f"Destination directory: {dest_}")

        d = defaultdict(list)
        self._scan_src(d, src_)
        self._make_dest_and_copy(d, dest_)

    def _scan_src(self, d, src: Path):
        for item in src.iterdir():
            if item.is_file():
                fname = item.name
                if fname.startswith("."):
                    fname = fname[1:]
                ending = "no_ending" if not "." in fname else fname.split(".")[-1]
                d[ending].append(item.resolve())
            elif item.is_dir():
                self._scan_src(d, item)

    def _make_dest_and_copy(self, d, dest: Path):
        if not dest.exists():
            dest.mkdir()
        for k in d:
            dest_tmp = dest / k
            dest_tmp.mkdir()
            for f in d[k]:
                try:
                    shutil.copy(f, dest_tmp)
                except Exception as err:
                    print(err)


def print_help():
    print("""[INFO]  Usage: python task1.py <source_dir> [<destination_dir>]
                    <source_dir>      - copy from, mandatory
                    <destination_dir> - copy and sort to, optional, default is '<source_dir>/../dest'\n""")

def main():
    argn = len(sys.argv)
    if argn < 2:
        raise Exception("Please add a source directory")

    src = sys.argv[1]

    if argn >= 3:
        dest = sys.argv[2]
    else:
        dest = FilesSortAndCopy.DEFAULT_DEST

    # Sort and copy in constructor
    FilesSortAndCopy(src, dest)

    # Create an object, set src and dist (optional) and do sort_and_copy
    files_sort_and_copy = FilesSortAndCopy()
    files_sort_and_copy.src = src
    files_sort_and_copy.dest = dest+"_set"
    files_sort_and_copy()

    # Can be called many times for different src or/and dest
    files_sort_and_copy(dest=dest+"_call_1")
    files_sort_and_copy(dest=dest+"_call_2")

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print_help()
        print(f"[ERROR] {err}\n")
        exit(1)
