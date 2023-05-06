import itertools

import numpy as np
from itertools import permutations
from typing import *


class Semester:

	def __init__(self):
		self.semester_completed = []

	def append(self, prev_semester: Tuple[float, float]):
		"""

		:param prev_semester: Tuple of format (GPA, credits)
		:return:
		"""
		self.semester_completed.append(prev_semester)

	def get_semester(self):
		return self.semester_completed

	def get_gpa(self):
		gpa, credit = zip(*self.semester_completed)
		return round(np.average(gpa, weights=credit), 2)

	def optimize_gpa(self, current_semester: Dict[str, Tuple[float, float]]):
		"""

		:param current_semester: Dict of format {course_name: (GPA, credits)}
		:return:
		"""
		num_course = len(current_semester)
		pass_fail_list = [
			[0]*num_course for _ in range(num_course)
		]
		for idx, course_list in enumerate(pass_fail_list):
			pass_fail_list[idx][idx] = 1

		all_possibility = (list(itertools.product(*pass_fail_list)))
		# 0 -> pass, 1 -> keep

		numerator = 0
		denominator = 0

		for gpa_prev, credit_prev in self.semester_completed:
			numerator += gpa_prev * credit_prev
			denominator += credit_prev


		best_gpa = 0
		best_possibility = None
		for decision in all_possibility:
			current_semester_gpa, current_semester_credit = zip(*current_semester.values())

			current_semester_gpa = np.array(current_semester_gpa)
			current_semester_credit = np.array(current_semester_credit)
			decision = np.array(decision)

			current_semester_gpa = current_semester_gpa * decision
			current_semester_credit = current_semester_credit * decision

			current_numerator = numerator + np.sum(current_semester_gpa * current_semester_credit)
			current_denominator = denominator + np.sum(current_semester_credit)

			current_gpa = (current_numerator / current_denominator)

			if current_gpa > best_gpa:
				best_gpa = current_gpa
				best_possibility = decision

		best_gpa = round(best_gpa, 2)

		pass_class, keep_class = self.format_best_decision(best_possibility)

		difference_with_old_gpa = best_gpa - self.get_gpa()

		sign = "+" if difference_with_old_gpa > 0 else ""

		print(f"The best GPA that can be obtain is: {best_gpa} [{sign} {round(difference_with_old_gpa, 2)}]")
		print("This is the best decision to take:")
		print("---------------------------------")
		for pass_course in pass_class:
			print(f"Pass: {pass_course}")
		print("---------------------------------")
		for keep_course in keep_class:
			print(f"Keep: {keep_course}")
		print("---------------------------------")



	def format_best_decision(self, decision: Optional[np.ndarray]) -> Tuple[List, List]:
		"""
		:param decision: Tuple of format (GPA, credits)
		:return: str
		"""
		pass_class = []
		keep_class = []

		for idx, course in enumerate(decision):
			if course == 0:
				pass_class.append(list(current_semester.keys())[idx])
			else:
				keep_class.append(list(current_semester.keys())[idx])

		return pass_class, keep_class




if __name__ == '__main__':

	My_semester = Semester()
	My_semester.append((2.67, 15))
	My_semester.append((3.1, 15))
	My_semester.append((3.4, 15))


	current_semester = {
		"Design II" : (2.67, 4),
		"TPOP": (4, 3),
		"Quantique": (2.33, 3),
		"MecFlu": (4.33, 3),
		"SST" : (3.67, 1),
		"Optique": (3, 3),
	}
	My_semester.optimize_gpa(current_semester)
