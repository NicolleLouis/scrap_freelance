class StringFormatterService:
    @staticmethod
    def format_field(raw_field):
        field_renaming = {
            "pneu": "pneus",
            "tige": "tige_de_selle"
        }

        field = raw_field.lower()
        field = field.strip()
        field = field.replace(" ", "_")
        field = field.replace("-", "_")
        field = field.replace("/", "_")
        field = field.replace("é", "e")
        field = field.replace("è", "e")
        field = field.replace("î", "i")

        if field in field_renaming:
            field = field_renaming[field]

        return field

    @staticmethod
    def format_price(raw_price):
        price = raw_price.replace("€", "")
        price = ''.join(price.split())
        if price.isnumeric():
            return int(price)
        else:
            return None
