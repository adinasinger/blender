
from class_Exercise import Exercise
from blender_menu_v2 import print_menu
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


def set_difficulty():
	# get diff setting from user, return to variable to pass to generator
	diff_input = int(raw_input("What level of difficulty would you like today?\nEnter choice (1-4): "))
	return diff_input

def set_circuit_count():
# get number of circuits setting from user, return to variable to pass to generator
	circuit_input = int(raw_input("How many circuits would you like to do today?\nEnter choice (1-3): "))
	return circuit_input

def workout_generator(diff, num1):
#default generates random workout with 3 warm-up, 6 circuit, 2 cardio, 2 abs exercises at all diff levels
	
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
	
	print "Enter 0 for Main Menu or 5 to Exit"

def main():
	diff_choice = 4
	circuit_choice = 1
	#load list of exercises
	import_exercise_list("Exercise_data.csv")
	
#call menu function and define branch for each menu selection
	
	#display menu
	# menu: 0 - Main Menu, 1 - Generate workout, 2 - Change workout difficulty, 3 - Select number of circuits, 4 - Enter new exercise, 5 - Exit

	print_menu()

	menu_flag = True

	while (menu_flag):
		menu_input = int(raw_input("\nEnter menu selection: "))
		if menu_input == 0:
			print_menu()
		elif menu_input == 1:
			print "\nCurrent Settings - Difficulty: %i, # Circuits: %i" % (diff_choice, circuit_choice)
			workout_generator(diff=diff_choice,num1=circuit_choice)
		elif menu_input == 2:
			print "\nCurrent Difficulty Setting: %i \n" % (diff_choice)
			set_difficulty()
			diff_choice = diff_input
			print "\nNew Difficulty Setting: %i \n" % (diff_choice)
		elif menu_input == 3:
			print "\nCurrent Circuit Number Setting: %i \n" % (circuit_choice)
			set_circuit_count()
			circuit_choice = circuit_input
			print "\nNew Circuit Number Setting: %i \n" % (circuit_choice)
		elif menu_input == 4:
			print "Add a new exercise (include name, type, difficulty level, muscle group worked, and body position) "
			#run add_exercise()
		elif menu_input == 5:
			print "\nSee you next workout!\n"
			menu_flag = False
		elif menu_input != "":
			print "Please select a valid menu option"
		else:
			break
	return menu_input

	#generate random workout with 2 warm-up, 4 circuit, 2 cardio, 2 abs exercises
	#workout_generator(diff=diff_choice,num1=circuit_choice)
#


if __name__ == '__main__':
	main()