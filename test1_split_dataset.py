import random, shutil, os


def list_split(input_list, split_rate):
	list_dict = {}

	num_list = len(input_list)

	train_picknumber = int(num_list*split_rate['train'])
	train_list = random.sample(input_list, train_picknumber)

	for sample in train_list:
		if sample in input_list:
			input_list.remove(sample)
	valid_picknumber = int(num_list*split_rate['valid'])
	valid_list = random.sample(input_list, valid_picknumber)

	for sample in valid_list:
		if sample in input_list:
			input_list.remove(sample)
	test_list = input_list

	list_dict['train_list'] = train_list
	list_dict['valid_list'] = valid_list
	list_dict['test_list'] = test_list
 
	return list_dict


def dataset_split(input_path, wanted_words, split_rate):
	current_path = os.getcwd()
	target_base_path = current_path + '/splitted_data'
	if os.path.exists(target_base_path):
		shutil.rmtree(target_base_path)

	for word in wanted_words:
		source_path = input_path + '/' + word
		if os.path.isdir(source_path):
			file_path = os.listdir(source_path)
			a = len(file_path)
			list_dict = list_split(file_path, split_rate)

			print('word:' + word + '\t' + 
				'total:' + str(a) + '\t'
				'train:' + str(len(list_dict['train_list'])) + ' ' + '\t'
				'valid:' + str(len(list_dict['valid_list'])) + ' ' + '\t' 
				'test:' + str(len(list_dict['test_list'])))

			target_train_path = target_base_path + '/train/' + word
			target_valid_path = target_base_path + '/valid/' + word
			target_test_path = target_base_path + '/test/' + word

			os.makedirs(target_train_path)
			os.makedirs(target_valid_path)
			os.makedirs(target_test_path)

			for sample in list_dict['train_list']:
				audio_path = source_path + '/' + sample
				shutil.copy(audio_path, target_train_path)
			for sample in list_dict['valid_list']:
				audio_path = source_path + '/' + sample
				shutil.copy(audio_path, target_valid_path)
			for sample in list_dict['test_list']:
				audio_path = source_path + '/' + sample
				shutil.copy(audio_path, target_test_path)


	return 0


input_path = '/home/liurun/lr/kws/mytc_resnet/speech_commands_dataset/dataset'
wanted_words = ['house', 'right', 'bird']
split_rate = {
	'train': 0.8,
	'test': 0.1,
	'valid': 0.1,
}

file_path = dataset_split(input_path, wanted_words, split_rate)


