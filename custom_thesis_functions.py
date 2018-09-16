path_import_data = r"C:\Users\janni\OneDrive\TU Berlin\4 - Abschlussarbeiten\01 - Bachelorarbeit\model\data\\"
path_pickle_data = r"C:\Users\janni\OneDrive\TU Berlin\4 - Abschlussarbeiten\01 - Bachelorarbeit\model\validation\\"

def create_date_format(period):
    """Put first and last timestamp of given period in brackets"""
    return "({0}) ({1})".format(period[0].strftime("%Y-%m-%d %H-%M"), period[-1].strftime("%Y-%m-%d %H-%M"))