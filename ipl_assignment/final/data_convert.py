import yaml
import time
#1 (1).yaml
start_time = time.time()
file_number = 1
main_data = []
while(file_number < 637):
	file_name = "1 ("+str(file_number)+").yaml"
	#print(file_name)
	document = open(file_name).read()
	file_number = file_number + 1
	l = yaml.load(document)
	i = 0
	j = 0
	team1=l['innings'][0]['1st innings']['team']
	innings1_balls = []
	while(i<len(l['innings'][0]['1st innings']['deliveries'])):
		innings1_balls.append(list(l['innings'][0]['1st innings']['deliveries'][i].keys()))
		i = i+1
	innings1_balls_1 = []
	for i in range(len(innings1_balls)):
		innings1_balls_1.append(innings1_balls[i][0])
	i=0

	while(i<len(l['innings'][0]['1st innings']['deliveries'])):
		temp_list =[]
		temp_list.append("1st innings")
		temp_list.append(innings1_balls_1[i])
		temp_list.append(l['innings'][0]['1st innings']['deliveries'][i][innings1_balls_1[i]]['batsman'])
		temp_list.append(l['innings'][0]['1st innings']['deliveries'][i][innings1_balls_1[i]]['bowler'])
		temp_list.append(l['innings'][0]['1st innings']['deliveries'][i][innings1_balls_1[i]]['non_striker'])
		temp_list.append(l['innings'][0]['1st innings']['deliveries'][i][innings1_balls_1[i]]['runs']['batsman'])
		temp_list.append(l['innings'][0]['1st innings']['deliveries'][i][innings1_balls_1[i]]['runs']['extras'])
		if('wicket' in l['innings'][0]['1st innings']['deliveries'][i][innings1_balls_1[i]].keys()):
			temp_list.append(l['innings'][0]['1st innings']['deliveries'][i][innings1_balls_1[i]]['wicket']['player_out'])
		else:
			temp_list.append("no wicket")
		i = i+1
		main_data.append(temp_list)
	if(len(l['innings'])>=2):
		team2=l['innings'][1]['2nd innings']['team']
		innings2_balls = []
		i = 0
		#print(l['innings'][1]['2nd innings']['deliveries'][0].keys())
		while(i<len(l['innings'][1]['2nd innings']['deliveries'])):
			innings2_balls.append(list(l['innings'][1]['2nd innings']['deliveries'][i].keys()))
			i = i+1
		#print(innings2_balls)
		innings2_balls_1 = []
		for i in range(len(innings2_balls)):
			innings2_balls_1.append(innings2_balls[i][0])
		i = 0
		while(i<len(innings2_balls_1)):
			temp_list =[]
			temp_list.append("2nd innings")
			temp_list.append(innings2_balls_1[i])
			temp_list.append(l['innings'][1]['2nd innings']['deliveries'][i][innings2_balls_1[i]]['batsman'])
			temp_list.append(l['innings'][1]['2nd innings']['deliveries'][i][innings2_balls_1[i]]['bowler'])
			temp_list.append(l['innings'][1]['2nd innings']['deliveries'][i][innings2_balls_1[i]]['non_striker'])
			temp_list.append(l['innings'][1]['2nd innings']['deliveries'][i][innings2_balls_1[i]]['runs']['batsman'])
			temp_list.append(l['innings'][1]['2nd innings']['deliveries'][i][innings2_balls_1[i]]['runs']['extras'])
			if('wicket' in l['innings'][1]['2nd innings']['deliveries'][i][innings2_balls_1[i]].keys()):
				temp_list.append(l['innings'][1]['2nd innings']['deliveries'][i][innings2_balls_1[i]]['wicket']['player_out'])
			else:
				temp_list.append("no wicket")
			i = i+1
			main_data.append(temp_list)
		super_over = []
		if(len(l['innings'])>2):
			key_name1 = team2+" "+"Super Over"
			innings3_balls = []
			i = 0
			#print(l['innings'][1]['2nd innings']['deliveries'][0].keys())
			while(i<len(l['innings'][2][key_name1]['deliveries'])):
				innings3_balls.append(list(l['innings'][2][key_name1]['deliveries'][i].keys()))
				i = i+1
			#print(innings2_balls)
			innings3_balls_1 = []
			for i in range(len(innings3_balls)):
				innings3_balls_1.append(innings3_balls[i][0])
			i = 0
			while(i<len(innings3_balls_1)):
				temp_list =[]
				temp_list.append(key_name1)
				temp_list.append(innings3_balls_1[i])
				temp_list.append(l['innings'][2][key_name1]['deliveries'][i][innings3_balls_1[i]]['batsman'])
				temp_list.append(l['innings'][2][key_name1]['deliveries'][i][innings3_balls_1[i]]['bowler'])
				temp_list.append(l['innings'][2][key_name1]['deliveries'][i][innings3_balls_1[i]]['non_striker'])
				temp_list.append(l['innings'][2][key_name1]['deliveries'][i][innings3_balls_1[i]]['runs']['batsman'])
				temp_list.append(l['innings'][2][key_name1]['deliveries'][i][innings3_balls_1[i]]['runs']['extras'])
				if('wicket' in l['innings'][2][key_name1]['deliveries'][i][innings3_balls_1[i]].keys()):
					temp_list.append(l['innings'][2][key_name1]['deliveries'][i][innings3_balls_1[i]]['wicket']['player_out'])
				else:
					temp_list.append("no wicket")
				i = i+1
				main_data.append(temp_list)
			key_name2 = team1+" "+"Super Over"
			innings3_balls = []
			i = 0
			#print(l['innings'][1]['2nd innings']['deliveries'][0].keys())
			while(i<len(l['innings'][3][key_name2]['deliveries'])):
				innings3_balls.append(list(l['innings'][3][key_name2]['deliveries'][i].keys()))
				i = i+1

			innings3_balls_1 = []
			for i in range(len(innings3_balls)):
				innings3_balls_1.append(innings3_balls[i][0])
			i = 0
			while(i<len(innings3_balls_1)):
				temp_list1 =[]
				temp_list1.append(key_name2)
				temp_list1.append(innings3_balls_1[i])
				temp_list1.append(l['innings'][3][key_name2]['deliveries'][i][innings3_balls_1[i]]['batsman'])
				temp_list1.append(l['innings'][3][key_name2]['deliveries'][i][innings3_balls_1[i]]['bowler'])
				temp_list1.append(l['innings'][3][key_name2]['deliveries'][i][innings3_balls_1[i]]['non_striker'])
				temp_list1.append(l['innings'][3][key_name2]['deliveries'][i][innings3_balls_1[i]]['runs']['batsman'])
				temp_list1.append(l['innings'][3][key_name2]['deliveries'][i][innings3_balls_1[i]]['runs']['extras'])
				if('wicket' in l['innings'][3][key_name2]['deliveries'][i][innings3_balls_1[i]].keys()):
					temp_list1.append(l['innings'][3][key_name2]['deliveries'][i][innings3_balls_1[i]]['wicket']['player_out'])
				else:
					temp_list1.append("no wicket")
				i = i+1
				main_data.append(temp_list1)
		#print("length",len(main_data))
for i in main_data:
	string = ""
	for j in i:
		string = string + str(j) +","
	print(string)
end_time = time.time()
print("Time taken=",end_time-start_time)
