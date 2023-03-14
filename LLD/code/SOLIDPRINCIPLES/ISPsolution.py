

from abc import ABCMeta,abstractmethod


class CSVconverter(metaclass=ABCMeta):
    @abstractmethod
    def from_csv(csv_data: str):
        ...

class JSON_CONVERTER(metaclass=ABCMeta):
    @abstractmethod
    def from_json(json_data: str):
        ...
class TXT_CONVERTER(metaclass=ABCMeta):
    @abstractmethod
    def extract_data_from_txt(txt_data: str):
        ...



class txtClient(TXT_CONVERTER):
    ...

class jsonClient(JSON_CONVERTER):
    ...

