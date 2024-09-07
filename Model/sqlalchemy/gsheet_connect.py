from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials # Note: the Python Quickstart code imports from oauth2.credentials. DON'T DO THAT. 
import pandas as pd
import os  
from googleapiclient.errors import HttpError
import google.auth

name_json = "login-304908-7a0b64a45114.json"
path_json = os.path.join('Model','sqlalchemy',name_json)


CELL_RANGE_SCOPES = ['Inventory!A2:O','Inbound!A2:O','Outbound!A:O','Adjusment!A:O']

class ActivateSheet():

    def __init__(self) -> None:
        data_range = ['Inventory!A2:O','Inbound!A2:O','Outbound!A2:O','Adjusment!A2:O']

        self.CELL_RANGE_SCOPES=data_range
        pass

        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        self.credentials = Credentials.from_service_account_file(path_json, scopes=SCOPES) # Note: the Python Quickstart code uses the `from_authorized_user_file` function. DON'T DO THAT.

        service = build('sheets', 'v4', credentials=self.credentials)

        # The ID of the spreadsheet to retrieve data from.
        # Open your spreadsheet in the browser and copy the part from the URL
        # E.g. https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit
        # self.SPREADSHEET_ID = '1Cp1YbL7Hg96P6ZKTxk9mx1yOLe4YHFV4vx4AgyijXf4' 

        # The A1 notation of the values to retrieve.
        # See details under #Cell here: https://developers.google.com/sheets/api/guides/concepts
        self.CELL_RANGE = self.CELL_RANGE_SCOPES[0] 
        self.CELL_RANGE2= self.CELL_RANGE_SCOPES[1]
        self.CELL_RANGE3= self.CELL_RANGE_SCOPES[2]
        self.CELL_RANGE4= self.CELL_RANGE_SCOPES[3]

        # Call the Sheets API
        self.sheet = service.spreadsheets()

    def get_inventory(self):
        result = self.sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                    range=self.CELL_RANGE).execute()
        self.values = result.get('values', [])
        if len(self.values)==0:
            self.values=[["","","","","","","","",""] ]
        for values in self.values:
            if len(values) <= 6:
                values.append('0')
            values[8] = values[8].replace(".","")
            values[8] =values[8].replace(",00","")
            values[8] =values[8].replace("(","-")
            values[8] =values[8].replace(")","")
            if values[8]=="":
                values[8]=str('0')
            values[8] = values[8].replace(',','.')
            values[8] =float(values[8])
            # import pdb 
            # pdb.set_trace()

        # Do something with the returned values
        pd.set_option('display.max_rows', None)
        # pd.set_option('display.max_columns', None)

        data_pandas = pd.DataFrame(self.values)
        self.get_total = round(sum(data_pandas[8]),2)

        # print(data_pandas)

        # print(values2)
        # print(values3)
        # print(values4)
        return self.values , self.get_total

    def get_inbound(self):
        result = self.sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                    range=self.CELL_RANGE2).execute()

        self.values2 = result.get('values', [])
        if len(self.values2)==0:
            self.values2=[["","","","","","","","","","","","","","","",""] ]

        for values in self.values2:
            # while len(values) != 10:
            #     values.append('0')
            values[9] = values[9].replace(".","")
            values[9] =values[9].replace(",00","")
            if values[9]=="":
                values[9]=str('0')
            values[9] =values[9].replace(",",".")
            # print(values[9])
            values[9] =float(values[9])
            # import pdb 
            # pdb.set_trace()
        # Do something with the returned values
        pd.set_option('display.max_rows', None)
        # pd.set_option('display.max_columns', None)

        data_pandas = pd.DataFrame(self.values2)
        # print(data_pandas)
        self.get_total = sum(data_pandas[9])
        # print(self.get_total)

        # print(values2)
        # print(values3)
        # print(values4)
        return self.values2,self.get_total

    def get_outbound(self):
        result = self.sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                    range=self.CELL_RANGE3).execute()

        self.values3 = result.get('values', [])
        if len(self.values3)==0:
            self.values3=[["","","","","","","","","","",""] ]

        for values in self.values3:
      


            values[10] = values[10].replace(".","")
            values[10] = values[10].replace(",00","")
            if values[10]=="":
                values[10]=str('0')

            values[10] = values[10].replace(",",".")
            values[10] = float(values[10])
        # Do something with the returned values
        pd.set_option('display.max_rows', None)
        # pd.set_option('display.max_columns', None)

        data_pandas = pd.DataFrame(self.values3)

        # print(data_pandas)
        self.get_total = sum(data_pandas[10])
        return self.values3,self.get_total

    def get_adjustment(self):
        result = self.sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                    range=self.CELL_RANGE4).execute()
        self.values4 = result.get('values', [])

        if len(self.values4)==0:
            self.values4=[["","","","","","","","","",""] ]
        for values in self.values4:
            while len(values) <= 9:
                values.append('0')

            values[9] = values[9].replace(".","")
            values[9] =values[9].replace(",00","")
            if values[9]=="":
                values[9]=str('0')
            values[9] =values[9].replace(",",".")
            values[9] =float(values[9])

        # Do something with the returned values
        pd.set_option('display.max_rows', None)
        # pd.set_option('display.max_columns', None)

        data_pandas = pd.DataFrame(self.values4)
        self.get_total = sum(data_pandas[9])
        # print(data_pandas)

        return self.values4,self.get_total

    # Sample response -
    # [['A1', 'B1'],
    # ['A2', 'B2'],
    # ['A3', 'B3'],
    # ['A4', 'B4']]

    # def write_value(self,spreadsheet_id=None, range_name=None, value_input_option=None, _values=None):
    def write_value(self,data):
    
        """
        Creates the batch_update the user has access to.
        Load pre-authorized user credentials from the environment.
        TODO(developer) - See https://developers.google.com/identity
        for guides on implementing OAuth2 for the application.
        """
        value_input_option = "USER_ENTERED"
        self.values_tuple = data 
        self.values = [] 
        for dataa in self.values_tuple:
            self.databaru = list(dataa)
            del self.databaru[15]
            self.values.append(self.databaru)
        # import pdb 
        # pdb.set_trace()
        self.range_name = self.CELL_RANGE
        # self.SPREADSHEET_ID = spreadsheet_id
        # spreadsheet_id=self.SPREADSHEET_ID
        # creds, _ = google.auth.default()
        # self.values=self.values
        # import pdb 
        # pdb.set_trace()
        # pylint: disable=maybe-no-member
        try:
            service = build("sheets", "v4", credentials= self.credentials)
            # self.values = [
            #     [
            #         # Cell values ...
            #     ],
            #     # Additional rows ...
            # ]
            body = {"values": self.values}
            result = (
                service.spreadsheets()
                .values()
                .update(
                    spreadsheetId=self.SPREADSHEET_ID,
                    range=self.range_name,
                    valueInputOption=value_input_option,
                    body=body,
                )
                .execute()
            )
            print(f"{result.get('updatedCells')} cells updated.")
            return result
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

    def delete_value(self,data):
        
        """
        Creates the batch_update the user has access to.
        Load pre-authorized user credentials from the environment.
        TODO(developer) - See https://developers.google.com/identity
        for guides on implementing OAuth2 for the application.
        """
        value_input_option = "USER_ENTERED"
        self.new_data = []

        for add in range(len(data)) :
            self.new_data.append(['','','','','','','','','','','','','','','',''])

        
        self.values_tuple = self.new_data 
        
        self.values = [] 

        for dataa in self.values_tuple:
            self.databaru = list(dataa)
            del self.databaru[15]
            self.values.append(self.databaru)
        # import pdb 
        # pdb.set_trace()
        self.range_name = self.CELL_RANGE
        # self.SPREADSHEET_ID = spreadsheet_id
        # spreadsheet_id=self.SPREADSHEET_ID
        # creds, _ = google.auth.default()
        # self.values=self.values
        # import pdb 
        # pdb.set_trace()
        # pylint: disable=maybe-no-member
        try:
            service = build("sheets", "v4", credentials= self.credentials)
            # self.values = [
            #     [
            #         # Cell values ...
            #     ],
            #     # Additional rows ...
            # ]
            body = {"values": self.values}
            result = (
                service.spreadsheets()
                .values()
                .update(
                    spreadsheetId=self.SPREADSHEET_ID,
                    range=self.range_name,
                    valueInputOption=value_input_option,
                    body=body,
                )
                .execute()
            )
            print(f"{result.get('updatedCells')} cells updated.")
            return result
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

# Tes = ActivateSheet(CELL_RANGE_SCOPES)
# Tes.get_adjustment()
# Tes.get_outbound()