class libro():
    def __init__(self,titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn


    def __str__(self):
        print(f"{self.titulo} {self.autor}")

    def __eq__(self, libro2):
        if(libro1 == libro2):
            return self.libro1 == libro2
        





libro1 = libro("mundo", "bruno", 123)
libro2 = libro("mundo2", "reke",321)
libro1.__str__()
libro2.__str__()
libro1.__eq__()
