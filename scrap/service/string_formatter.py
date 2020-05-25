class StringFormatterService:
    @staticmethod
    def format_field(raw_field):
        field = raw_field.lower()
        field = field.replace(" ", "_")
        field = field.replace("-", "_")
        field = field.replace("/", "_")
        field = field.replace("é", "e")
        field = field.replace("è", "e")
        field = field.replace("î", "i")
        return field

    @staticmethod
    def format_price(raw_price):
        price = raw_price.replace("€", "")
        price = ''.join(price.split())
        if price.isnumeric():
            return int(price)
        else:
            return None
