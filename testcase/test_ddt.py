# -- encoding: utf-8 --
# @time:    	2022/4/8 21:15
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
test_case = [{"id": 1, "name": "a", "age": 18},
             {"id": 2, "name": "b", "age": 19},
             {"id": 3, "name": "c", "age": 20}]
import ddt
import unittest


@ddt.ddt()
class TestDtt(unittest.TestCase):
    @ddt.data(*test_case)
    def test_001(self, case_data):
        print(case_data)
