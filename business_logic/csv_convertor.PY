import csv
import pandas as pd
from fastapi import HTTPException
import json


class CsvConvertor:

    def __init__(self, csv_file_path):
        self.column_names = []
        self.csv_file_path = csv_file_path
        self.json_array = self.csv_to_json(self.csv_file_path)

    def csv_to_json(self, csvFilePath):
        """
        read csv file and convert it to json using
        class csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
        Create an object that operates like a regular reader but maps the information in each row to a dict whose keys are given by the optional fieldnames parameter.

        :param csvFilePath:
        :return:
        """
        json_array = []
        # read csv file
        with open(csvFilePath, encoding='utf-8') as csvf:
            # load csv file data using csv library's dictionary reader
            csv_reader = csv.DictReader(csvf)
            first_row = True
            for row in csv_reader:
                if first_row:
                    self.column_names = list(row.keys())
                    first_row = False
                # add this python dict to json array
                json_array.append(row)
        # convert each csv row into python dict
        return json_array



    async def append_row_to_csv(self, dict: dict):
        if not await self.are_list_equal(self.column_names, list(dict.keys())):
            return HTTPException(status_code=404, detail=f"Sorry, dict{dict.keys()} is not equal to {self.column_names}")

        with open(self.csv_file_path, 'a', newline='') as f_object:
            # Pass the file object and a list
            # of column names to DictWriter()
            # You will get a object of DictWriter

            dict_writer_object = csv.DictWriter(f_object, fieldnames=self.column_names)

            # Pass the dictionary as an argument to the Writerow()
            dict_writer_object.writerow(dict)

            # Close the file object
            f_object.close()

    async def are_list_equal(self, list1, list2):
        _list1 = list1.copy()
        _list2 = list2.copy()
        _list1.sort()
        _list2.sort()
        if list1 == list2:
            return True
        return False

    async def update_csv_file(self, row, column, new_data):
        df = pd.read_csv(self.csv_file_path)
        # updating the column value/data
        df.loc[row - 1, column] = new_data
        # writing into the file
        df.to_csv(self.csv_file_path, index=False)

    async def update_list(self, filter, new_data):
        row = None
        for item in self.json_array:
            for filter_key, filter_val in filter.items():
                if item[filter_key] == str(filter_val):
                    row = item["row"]
                    for key, val in new_data.items():
                        if key != "row":
                            await self.update_csv_file(int(row), key, val)

        return {"message": f"update rwo {row}"}

    async def append_list(self, item):
        row = len(self.json_array) + 1
        item.row = row
        _item_dict = dict(item)
        self.json_array.append(_item_dict)
        await self.append_row_to_csv(_item_dict)
        return {"message": f"new item was added to file {self.csv_file_path} in row {row}"}


