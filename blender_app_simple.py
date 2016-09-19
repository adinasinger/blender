
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

def circuit_counter(count_num, category):
# get count and exercise_type filter
	pass

def workout_generator():
#generate random workout with 2 warm-up, 4 circuit, 2 cardio, 2 abs exercises
	workout = []
	count = 0
#get randomized exercise list
	random_list = randomize_workout(exercise_list)

#while count <=2, get name of exercise if type = warm-up (lowercase)
	
	for i in random_list:
		while count<=2:
			if i.workout_type.lower() == "warm-up":
				workout.append(i.name)
				print i.name
				count += 1
			break
	print workout
#while count <=4, get name of exercise if type = circuit (lowercase)
#while count <=2, get name of exercise if type = cardio (lowercase)
#while count <=2, get name of exercise if type = abs (lowercase)


def main():
	#load list of exercises
	import_exercise_list("Exercise_data.csv")
	workout_generator()

#print all exercise names in the class entry list
	# for exercise in exercise_list:
	# 	print exercise.name

	







#call menu function and branch for each menu selection
# menu: 0 - Main Menu, 1 - choose workout focus, 2 - choose exclusions, 3 - enter workout duration (minutes), 4 - enter new exercise
	#display menu
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
	# 		print "Enter name of exercise to delete"
	# 		#run del_exercise()
	# 	elif menu_input == 9:
	# 		print "See you next workout!"
	# 		menu_flag = False
	# 	elif menu_input != "":
	# 		print "Please select a valid menu option"
	# 	else:
	# 		break
	# return menu_input

	#generate random workout with 2 warm-up, 4 circuit, 2 cardio, 2 abs exercises




if __name__ == '__main__':
	main()