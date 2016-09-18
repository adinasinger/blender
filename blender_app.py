# menu: 0 - Main Menu, 1 - choose workout focus, 2 - choose exclusions, 3 - enter workout duration (minutes), 4 - enter new exercise

from class_Exercise import Exercise
from blender_menu import print_menu
from random import *

exercise_list=[]

def import_exercise_list():
	Exercise("good mornings", int("1"), "upper body", "back", "standing")
#file i/o to import rest of exercises?

def randomize_workout(list1):
	random_list = list1.shuffle()#shuffle returned list of exercises
	#return shuffled list
	return random_list

def include_exercise(focus):
	focus_list=[]

	#show list of filter criteria (sep function? in main?) - upper body, lower body, abs, all
	#prompt user to enter a workout focus from list (in main)
	for exercise in exercise_list:
		if exercise.exercise_type.lower() == focus:
			focus_list.append(exercise)
	#return randomized list of exercises matching filter
	print focus_list

def exclude_exercise(exclusion):
	#show list of filter criteria (sep function?)
	#prompt user to enter exclusion from list
	#return randomized list of exercises matching filter
	pass

def workout_duration(minutes):
	#default workout to 15 minutes (any additional structure to circuits?)
	#prompt user for desired workout duration (in minutes)
	#look up duration for entry in randomized exercise list - OR can assume 30 sec duration ok for each set, and add or repeat exercises until duration met
	#use loop/conditional to add durations until greater or equal to arguement (move to next if over, until have checked all in list)
	#return list of exercises 
	pass

def workout_intensity(int):
	#default workout to intensity 1 (any additional structure to circuits?)
	#prompt user for desired workout intensity (1-4)
	#look up difficulty level for entry in randomized exercise list - if not enough for set, ok to use lower intensities but NOT higher
	#return list of exercises 
	pass

def add_excercise():
	#prompt user for name of new exerise
	#check for upper/lowercase
	#if exercise name exists, warn user and return to prompt
	#if exercise name doesn't exist, promt for details and then add to dictionary/database
	#prompt for related data (see above) 
	pass

def del_excercise():
	#prompt user for name of exerise to delete
	#check for upper/lowercase
	#if exercise name does NOT exist, warn user and return to prompt
	#if exercise name exists, promt to be sure if they want to delete
	#if user sure they want to delete, then delete exercise from class list
	pass


def main():
	import_exercise_list()
	print_menu()

	menu_flag = True

	while (menu_flag):
		menu_input = int(raw_input("\nEnter Selection: "))
		if menu_input == 0:
			print_menu()
		elif menu_input == 1:
			print "Choose workout focus (type) from options"
			#run include_focus()
			focus_input = raw_input("What kind of workout do you want to focus on? ")
			include_exercise(focus_input)
		elif menu_input == 2:
			print "Choose body position from options"
			#run exclude() OR just pick body position to filter list
		elif menu_input == 3:
			#define workout by duration and intensity; default workout length to 15 mins
			print "Enter length of desired workout in minutes: "
			print "Enter workout difficulty level: "
		elif menu_input == 4:
			#run add_exercise()
			print "Add a new exercise (include name, difficulty level, type, muscle group worked, and body position) "
		elif menu_input == 5:
			print "Enter name of exercise to delete"
			#run del_exercise()
		elif menu_input == 9:
			print "See you next workout!"
			menu_flag = False
		elif menu_input != "":
			print "Please select a valid menu option"
		else:
			break
	return menu_input



if __name__ == '__main__':
	main()