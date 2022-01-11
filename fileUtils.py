from notesList import NotesList


class FileUtils:

    @staticmethod
    def saveFile(path: str, notesList: NotesList):
        f = open(path, 'w')
        str = notesList.toString()
        f.write(str)
        f.close()