



class Pagination():
    @staticmethod
    def page_pagination(query_set: list, page_size: int, page: int):
        return query_set[page_size * (page -1):page_size * page]