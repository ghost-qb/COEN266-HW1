#Quan Bach
#COEN 266 Artificial Intelligence HW1 


possible_actions = ["Room is clean. beep beep", "Suck dust."]
possible_movement =["Move right.", "Move left."]

def roomba_around(_state,_action_sequence):
	finished_cleaning = False
	number_of_actions = 0
	while (~finished_cleaning):
		roomba_location = _state[2] #get the location of the robot at the current state 
		if _state[roomba_location] == 1:
			_action_sequence.append(possible_actions[_state[roomba_location]])
			number_of_actions += 1
			_action_sequence.append(possible_movement[roomba_location])
			number_of_actions += 1
            
			_state[roomba_location] = 0
			if roomba_location == 0:
				_state[2] = 1
			else: 
				_state[2] = 0
		else:
			_action_sequence.append(possible_movement[roomba_location])
			number_of_actions += 1
			if roomba_location == 0:
				_state[2] = 1
			else: 
				_state[2] = 0


		if (number_of_actions > 0 and _state[0] == 0 and _state[1] == 0):
			finished_cleaning = True
			return _state, _action_sequence, number_of_actions




test_case = [1,1,0]
print("Test case: ", test_case)
roomba_action = []
test = roomba_around(test_case,roomba_action)
print(test)


	
