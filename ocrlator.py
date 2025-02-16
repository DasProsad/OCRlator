#!/usr/bin/env python3

import os
import sys
import re
import easyocr

print(f"easyocr ver: {easyocr.__version__}")

def processImage(image_path) -> tuple:
	reader = easyocr.Reader(['en'])
	results = reader.readtext(image_path)
	extracted_text = " ".join([res[1].strip() for res in results])  # Strip spaces around detected text
	print(extracted_text)
	valid_expression = " ".join(re.findall(r'\d+|\+', extracted_text))

	try:
		total_cost = eval(valid_expression)
	except Exception:
		total_cost = None

	with open("ocr_output.txt", "w") as f:
		f.write(valid_expression)

	return valid_expression, total_cost

if __name__ == "__main__":
	my_name = os.path.basename(__file__)

	if len(sys.argv) != 2:
		print(f"Usage: {my_name} <image_path>")
		sys.exit(24)
	else:
		image_path = sys.argv[1]
		text, total = processImage(image_path)
		print("Extracted Expression:", text)
		print("Total Cost:", total)
