def convert_to_dict(module):
    ar_dict = {}
    ar_dict["name"] = ""
    ar_dict["executable"] = ""
    ar_dict["module"] = ""

    if module == "AugBase":
        ar_dict["name"] = "AugBase"
        ar_dict["executable"] = "ArBaseExcecutable"
        ar_dict["service"] = "augmented_base"
    elif module == "AugVideo":
        ar_dict["name"] = "AugVideo"
        ar_dict["executable"] = "ArVideoExcecutable"
        ar_dict["service"] = "augmented_video"
    else:
        print("Can't convert {} to dict, module name not renamed".format(module))
        ar_dict["name"] = module
        ar_dict["executable"] = module
        ar_dict["service"] = module

    return ar_dict


mylist = ["foo", "AugBase", "bar", "AugVideo"]

for i in mylist:
    print(convert_to_dict(i))