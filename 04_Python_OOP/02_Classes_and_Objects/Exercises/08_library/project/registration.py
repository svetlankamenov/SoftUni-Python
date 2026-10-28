from project.library import Library
from project.user import User


class Registration:
    def __init__(self):
        pass

    def add_user(self, user:User, library:Library):
        for added_user in library.user_records:
            if user.user_id == added_user.user_id:
                return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        for added_user in library.user_records:
            if user.user_id == added_user.user_id:
                library.user_records.remove(added_user)
                return

        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for added_user in library.user_records:
            if added_user.user_id == user_id:
                if added_user.username != new_username:
                    if added_user.username in library.rented_books:
                        library.rented_books[new_username] = library.rented_books.pop(added_user.username)
                    added_user.username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
                else:
                    return "Please check again the provided username - it should be different than the username used so far!"

        return f"There is no user with id = {user_id}!"