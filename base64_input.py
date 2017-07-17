#!/usr/bin/env python

import base64

if __name__ == "__main__":
	string_to_encode = "This is a test string"
	encoded_string = base64.b64encode(string_to_encode)
	print encoded_string