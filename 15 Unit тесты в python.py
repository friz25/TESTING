from work15 import *
data = {'Смартфон': 251, 'Компьютер': 340, 'Планшет': 36, 'ТВ': 10}
# data = {'Смартфон': -251, 'Компьютер': '340', 'Планшет': 36, 'ТВ': 10}


import unittest

class Test_work(unittest.TestCase):

	def setUp(self):#предтестовая подготовка кода
		pass
	def tearDown(self):#сделать чтото после тестир-ия
		pass
	#проверяет поступил ли в функцию tuple (кортеж)
	def test_test_arr(self):
		self.assertEqual(type(test_arr(data)), tuple)
	#проверяет поступил ли в функцию list (список)
	def test_percent1(self):
		self.assertEqual(type(percent([13,256,2])), list)
	#проверяет полученный % <= 100
	def test_percent2(self):
		for i in percent([13,256,56]):
			with self.subTest(i=i):
				self.assertGreaterEqual(100, i)

if __name__ == '__main__':
	unittest.main()
#чтобы запустить (более подробный) юниттест из CMD:
#python -m unittest -v test_work15