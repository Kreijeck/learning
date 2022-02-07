import re
import pandas as pd
import time

from sqlalchemy import true

class FStringParser:
    def __init__(self, string_template: str, tag_chars=("%<", ">%")) -> None:
        self.string_template = string_template
        self.tag_chars = tag_chars
        self.keys = self.__get_keys()
        self.regex = self.__parse_to_regexstring()

    def __get_keys(self) -> list:
        keys = []
        tag_start = self.tag_chars[0]
        tag_stop = self.tag_chars[1]
        idx_start = self.string_template.find(tag_start)
        while idx_start != -1:
            idx_stop = self.string_template.find(tag_stop, idx_start)
            # find string between start/stop seperator
            key = self.string_template[idx_start + len(tag_start): idx_stop]
            keys.append(key)
            idx_start = self.string_template.find(tag_start, idx_stop)

        return keys

    def __parse_to_regexstring(self):
        regex_signs = ["[", "]"]
        regex_string = self.string_template
        # Replace Parameter als wild cards : (.+)
        for key in self.keys:
            key_pattern = f"{self.tag_chars[0]}{key}{self.tag_chars[1]}"
            regex_string = regex_string.replace(key_pattern, "(.+)")

        # Replace specific regex signs with an escape sign 
        for sign in regex_signs:
            regex_string = regex_string.replace(sign, f"\\{sign}")
        return regex_string
    
    def get_value_dict(self, output):
        value_dict = {}
        matches = re.finditer(self.regex, output)
        for match in matches:
            for no, group in enumerate(match.groups()):
                value_dict[self.keys[no]] = group

        return value_dict

    def get_value_dict_of_df(self, df: pd.Series) -> list:
        
        datamodel = df.str.extract(self.regex).set_axis(self.keys, axis=1)
        # for output in df:
        #     value_dict = self.get_value_dict(output)
        #     # value_dict = {}
        #     # matches = re.finditer(self.regex, output)
        #     # for match in matches:
        #     #     for no, group in enumerate(match.groups()):
        #     #         value_dict[self.keys[no]] = group

        #     l.append(value_dict)
        return datamodel





if __name__ == '__main__':
    # test_string = "[pose/datapackages] ArCore::AccelerometerDataPackage: {accelerationXAxis 0.105, accelerationYAxis -0.507, accelerationZAxis 9.801, temperature 54, timestamp 1046370}"
    template_string = "[pose/datapackages] ArCore::AccelerometerDataPackage: {accelerationXAxis %<accelX>%, accelerationYAxis %<accelY>%, accelerationZAxis %<accelZ>%, temperature %<temp>%, timestamp %<timestamp>%}"
    st = FStringParser(template_string)
    # mydict = st.get_value_dict(test_string)
    # print(mydict)

    start = time.time()
    df = pd.read_csv("regex/testdata.csv")
    df = pd.read_csv(r"D:\Projects\dlt_v2_protics\test_files\test.csv")
    print(df)
    # val_dict = st.get_value_dict_of_df(df["Payload"])
    # df_pose = pd.DataFrame(val_dict).dropna().reset_index(drop=True)
    df_pose = st.get_value_dict_of_df(df["Payload"]).dropna().reset_index(drop=True)
    stop = time.time()
    print(df_pose)
    print(f"Needed Time: {round(stop-start, 2)}s")