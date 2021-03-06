
from class_Exercise import Exercise
from blender_menu import print_menu
from random import shuffle
import csv

exercise_list = []

def import_exercise_list(input_file):
#	exercise1 = Exercise("good mornings", "circuit", int("1"), "back", "standing")
# file i/o to import rest of exercises	
	with open(input_file, 'rU') as data_file:
    		reader = csv.reader(data_file)
    		for row in reader:
       		# print row
       			class_name = row[0]
       			class_type = row[1]
       			class_level = row[2]
       			exercise_list.append(Exercise(name = class_name, workout_type = class_type, diff_level = class_level))
      		return exercise_list


def randomize_workout(list1):
	shuffled_list = list1
	#shuffle returned list of exercises
	shuffle(shuffled_list)
	#return shuffled list
	return shuffled_list

def exercise_counter(count_num, category):
# get count and exercise_type filter, then return random exercised that meet criteria
	#get randomized exercise list
	workout = []
	count = 0
	random_list = randomize_workout(exercise_list)

	for i in random_list:
		while count<count_num:
			if i.workout_type.lower() == category:
				workout.append(i.name)
				print i.name
				count += 1
			break

def workout_generator():
#generate random workout with 3 warm-up, 6 circuit, 2 cardio, 2 abs exercises
	
#while count <3, get name of exercise if type = warm-up (lowercase)
	
	print '\033[1m'"\nWarm-up"'\033[0m'
	exercise_counter(3, "warm-up")
	print ""
#while count <6, get name of exercise if type = circuit (lowercase)
	print '\033[1m'"Circuit"'\033[0m'
	exercise_counter(6, "circuit")
	print ""
#while count <2, get name of exercise if type = cardio (lowercase)
	print '\033[1m'"Cardio"'\033[0m'
	exercise_counter(2, "cardio")
	print ""
	
#while count <2, get name of exercise if type = abs (lowercase)
	print '\033[1m'"Abs"'\033[0m'
	exercise_counter(2, "abs")
	print ""
	

def main():
	#load list of exercises
	import_exercise_list("Exercise_data.csv")
	
#call menu function and define branch for each menu selection
	
	#display menu
	# menu: 0 - Main Menu, 1 - Generate workout, 2 - Change workout difficulty, 3 - Select number of circuits, 4 - Enter new exercise, 5 - Exit

	# print_menu()

	# menu_flag = True

	# while (menu_flag):
	# 	menu_input = int(raw_input("\nEnter Selection: "))
	# 	if menu_input == 0:
	# 		print_menu()
	# 	elif menu_input == 1:
	# 		print "Choose workout focus (type) from options"
	# 		#run include_focus()
	# 		focus_input = raw_input("What kind of workout do you want to focus on? ")
	# 		include_exercise(focus_input)
	# 	elif menu_input == 2:
	# 		print "Choose body position from options"
	# 		#run exclude() OR just pick body position to filter list
	# 	elif menu_input == 3:
	# 		#define workout by duration and intensity; default workout length to 15 mins
	# 		print "Enter length of desired workout in minutes: "
	# 		print "Enter workout difficulty level: "
	# 	elif menu_input == 4:
	# 		#run add_exercise()
	# 		print "Add a new exercise (include name, difficulty level, type, muscle group worked, and body position) "
	# 	elif menu_input == 5:
	# 		print "See you next workout!"
	# 		menu_flag = False
	# 	elif menu_input != "":
	# 		print "Please select a valid menu option"
	# 	else:
	# 		break
	# return menu_input

	#generate random workout with 2 warm-up, 4 circuit, 2 cardio, 2 abs exercises
	workout_generator()



if __name__ == '__main__':
	main()