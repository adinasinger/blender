# this class records the filterable info for each exercise

class Exercise(object):
	def __init__(self, name, workout_type, diff_level, muscle_group="", body_position=""):
		self.name = name
		self.workout_type = workout_type
		self.diff_level = diff_level
		self.muscle_group = muscle_group
		self.body_position = body_position



