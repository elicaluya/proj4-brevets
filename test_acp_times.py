from acp_times import *


def test_open_1():
	assert open_time(60,200,arrow.get('2016-10-24 01:30', 'YYYY-MM-DD HH:mm')) == '2016-10-24 03:15'

def test_open_2():
	assert open_time(120,200,arrow.get('2016-10-24 01:30', 'YYYY-MM-DD HH:mm')) == '2016-10-24 05:01'

def test_open_3():
	assert open_time(175,200,arrow.get('2016-10-24 01:30', 'YYYY-MM-DD HH:mm')) == '2016-10-24 06:38'

def test_open_4():
	assert open_time(200,200,arrow.get('2016-10-24 01:30', 'YYYY-MM-DD HH:mm')) == '2016-10-24 07:22'
	

def test_close_1():
	assert close_time(60,200,arrow.get('2016-10-24 01:30', 'YYYY-MM-DD HH:mm')) == '2016-10-24 05:30'

def test_close_2():
	assert close_time(120,200,arrow.get('2016-10-24 01:30', 'YYYY-MM-DD HH:mm')) == '2016-10-24 09:30'

def test_close_3():
	assert close_time(175,200,arrow.get('2016-10-24 01:30', 'YYYY-MM-DD HH:mm')) == '2016-10-24 13:09'

def test_close_4():
	assert close_time(200,200,arrow.get('2016-10-24 01:30', 'YYYY-MM-DD HH:mm')) == '2016-10-24 14:50'