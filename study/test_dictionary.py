# 변수 선언

example_dictionary = {
	"키A": "값A",
	"키B": "값B",
	"키C": "값C"
}

# items() 함수
print("items(): ", example_dictionary.items())

# for 반복문과 items() 함수 조합
for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))