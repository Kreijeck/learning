import re


class String_Template:
    def __init__(self, string_template: str, tag_chars=("%<", ">%")) -> None:
        self.string_template = string_template
        self.tag_chars = tag_chars
        self.keys = self.__parse_keys()

    def __parse_keys(self) -> list:
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

    def get_key_value(self, teststring: str):
        d = {}
        s = re.
        # for key in self.keys:
        #     d[key] = 



if __name__ == '__main__':
    test_string = "Name: Thomas, Age: 40, country: DE"
    st = String_Template("Name: %<name>%, Age: %<age>%, country: %<country>%")
    print(st.__parse_keys())


# def create_fstring():
#     name = "Kreijeck"
#     age = "35"
#     country = "Germany"

#     print("The following data is received: Name: {name}, age={age}, country={country}")

# def get_values(f_string, log_string) -> dict:
#     # pseudocode
#     d = f_string.extract_parametes(log_string)
#     return d

# create_fstring()

# d = {
#     'name': "Kreijeck",
#     'age': 35,
#     'country': 'Germany',
#     }