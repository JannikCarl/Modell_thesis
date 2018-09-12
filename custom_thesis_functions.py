path_import_data = r"C:\Users\janni\OneDrive\TU Berlin\4 - Abschlussarbeiten\01 - Bachelorarbeit\modell\data\\"
path_pickle_data = r"C:\Users\janni\OneDrive\TU Berlin\4 - Abschlussarbeiten\01 - Bachelorarbeit\validierung\\"

def create_date_format(period):
    return "({0}) ({1})".format(period[0].strftime("%Y-%m-%d %H-%M"), period[-1].strftime("%Y-%m-%d %H-%M"))