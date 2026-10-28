from project.album import Album
from project.song import Song

class Band:
    def __init__(self, name:str):
        self.name = name
        self.albums = []

    def add_album(self, album:Album):
        for added_album in self.albums:
            if album.name == added_album.name:
                return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for added_album in self.albums:
            if album_name == added_album.name:
                if added_album.published:
                    return "Album has been published. It cannot be removed."
                else:
                    self.albums.remove(added_album)
                    return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        info = f"Band {self.name}\n"
        for added_album in self.albums:
            info += f"{added_album.details()}\n"

        info = info.rstrip()
        return info