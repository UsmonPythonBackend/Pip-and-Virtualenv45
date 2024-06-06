def db():
     service = input("""
        1. Users
        >>>""")

     if service == '1':
         query = "SELECT * FROM "
         print(*Database.connect(query, "select"), sep="\n")

if __name__ == "__main__":
             db()