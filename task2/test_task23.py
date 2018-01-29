import io
import os

def countchar(text_file):
	file = io.open(text_file, encoding = 'utf-8')
	file_text = file.readline()
	return (len(file_text) - 1)

def test_task23():
	assert countchar('input.txt') == 6
