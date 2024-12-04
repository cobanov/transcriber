import lancedb


class LanceDBManager:
    def __init__(self, db_path="lancedb"):
        self.db = lancedb.connect(db_path)

    def create_or_load_table(self, table_name):
        if table_name not in self.db.table_names():
            return self.db.create_table(table_name)
        return self.db.open_table(table_name)

    def insert_data(self, table_name, data):
        table = self.create_or_load_table(table_name)
        table.add(data)

    def search(self, table_name, embedding, top_k=5):
        table = self.db.open_table(table_name)
        results = table.search(embedding).limit(top_k).to_pandas()
        return results
