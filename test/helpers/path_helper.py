import os

def data_directory():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', "data"))

def monkey_example_directory():
    return data_directory() + "/MonkeyExample"

def xcode_example_project():
    return data_directory() + "/iOSProject/Example.xcodeproj"

def spaced_example_directory():
    return data_directory() + "/Spaces"
