import os

from trashcli.put import format_original_location
from .files import make_parent_for, make_file, make_unreadable_file


class FakeTrashDir:
    def __init__(self, path):
        self.info_path = os.path.join(path, 'info')
        self.files_path = os.path.join(path, 'files')

    def add_unreadable_trashinfo(self, basename):
        path = self.a_trashinfo(basename)
        make_unreadable_file(path)

    def add_trashed_file(self, basename, path, content):
        trashinfo_path = self.a_trashinfo(basename)
        file_path = self.file_path(basename)
        make_file(trashinfo_path, a_trashinfo(path))
        make_file(file_path, content)

    def a_trashinfo(self, basename):
        return '%s/%s.trashinfo' % (self.info_path, basename)

    def file_path(self, basename):
        return '%s/%s'  % (self.files_path, basename)

    def add_trashinfo(self, contents, base_name = "basename"):
        path = '%(info_dir)s/%(name)s.trashinfo' % {'info_dir': self.info_path,
                                                    'name': base_name}
        make_parent_for(path)
        make_file(path, contents)

    def add_trashinfo2(self, path, formatted_deletion_date):
        self.add_trashinfo(a_trashinfo(path, formatted_deletion_date),
                           os.path.basename(path))


def a_trashinfo(path,
                formatted_deletion_date='2000-01-01T00:00:01'):
    return ("[Trash Info]\n" +
            "Path=%s\n" % format_original_location(path) +
            "DeletionDate=%s\n" % formatted_deletion_date)


def a_trashinfo_without_date():
    return ("[Trash Info]\n"
            "Path=/path\n")

def a_trashinfo_with_invalid_date():
    return ("[Trash Info]\n"
            "Path=/path\n"
            "DeletionDate=Wrong Date")

def a_trashinfo_without_path():
    return ("[Trash Info]\n"
            "DeletionDate='2000-01-01T00:00:00'\n")

def a_trashinfo_with_date(date):
    return ("[Trash Info]\n"
            "DeletionDate=%s\n" % date)

def a_trashinfo_with_path(path):
    return ("[Trash Info]\n"
            "Path=%s\n" % path)
