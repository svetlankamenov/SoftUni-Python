class PhotoAlbum:
    def __init__(self, pages:int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = photos_count // 4
        if photos_count % 4 != 0:
            pages += 1

        return cls(pages)

    def add_photo(self, label:str):
        for i, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {i+1} slot {len(page)}"

        return "No more free slots"

    def display(self):
        output = "-----------\n"
        for page in self.photos:
            output += " ".join(["[]" for _ in range(len(page))]) + "\n"
            output += "-----------\n"

        return output