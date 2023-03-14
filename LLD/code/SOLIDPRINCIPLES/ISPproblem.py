from abc import ABCMeta, abstractmethod



class Data(metaclass=ABCMeta):

    @abstractmethod
    def extract_data_from_txt(txt_data: str):
        "Parse an event from XML"

    @abstractmethod
    def from_json(json_data: str):
        "Parse an event from JSON"
    @abstractmethod
    def from_csv(csv_data: str):
        ""
