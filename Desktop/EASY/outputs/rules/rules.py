def findDecision(obj): #obj[0]: fixed acidity, obj[1]: volatile acidity, obj[2]: citric acid, obj[3]: residual sugar, obj[4]: chlorides, obj[5]: free sulfur dioxide, obj[6]: total sulfur dioxide, obj[7]: density, obj[8]: pH, obj[9]: sulphates, obj[10]: alcohol
	# {"feature": "alcohol", "instances": 1599, "metric_value": 0.9965, "depth": 1}
	if obj[10]<=11.488317414799278:
		# {"feature": "free sulfur dioxide", "instances": 1319, "metric_value": 0.9943, "depth": 2}
		if obj[5]>1.0:
			# {"feature": "chlorides", "instances": 1316, "metric_value": 0.994, "depth": 3}
			if obj[4]>0.038:
				# {"feature": "total sulfur dioxide", "instances": 1314, "metric_value": 0.9938, "depth": 4}
				if obj[6]<=112.9533211878411:
					# {"feature": "volatile acidity", "instances": 1239, "metric_value": 0.9985, "depth": 5}
					if obj[1]<=1.0736549872636059:
						# {"feature": "density", "instances": 1231, "metric_value": 0.9989, "depth": 6}
						if obj[7]>0.99236:
							# {"feature": "fixed acidity", "instances": 1230, "metric_value": 0.9988, "depth": 7}
							if obj[0]>5.0:
								# {"feature": "citric acid", "instances": 1229, "metric_value": 0.9989, "depth": 8}
								if obj[2]<=0.8363361475575392:
									# {"feature": "pH", "instances": 1228, "metric_value": 0.9989, "depth": 9}
									if obj[8]>2.86:
										# {"feature": "sulphates", "instances": 1227, "metric_value": 0.9988, "depth": 10}
										if obj[9]>0.33:
											# {"feature": "residual sugar", "instances": 1226, "metric_value": 0.9989, "depth": 11}
											if obj[3]>1.2:
												return 'bad'
											elif obj[3]<=1.2:
												return 'bad'
											else: return 'bad'
										elif obj[9]<=0.33:
											return 'bad'
										else: return 'bad'
									elif obj[8]<=2.86:
										return 'good'
									else: return 'good'
								elif obj[2]>0.8363361475575392:
									return 'bad'
								else: return 'bad'
							elif obj[0]<=5.0:
								return 'bad'
							else: return 'bad'
						elif obj[7]<=0.99236:
							return 'good'
						else: return 'good'
					elif obj[1]>1.0736549872636059:
						return 'bad'
					else: return 'bad'
				elif obj[6]>112.9533211878411:
					# {"feature": "residual sugar", "instances": 75, "metric_value": 0.3534, "depth": 5}
					if obj[3]<=9.516083208746958:
						# {"feature": "pH", "instances": 74, "metric_value": 0.3034, "depth": 6}
						if obj[8]>2.93:
							# {"feature": "density", "instances": 71, "metric_value": 0.1851, "depth": 7}
							if obj[7]>0.9948023556288615:
								# {"feature": "volatile acidity", "instances": 69, "metric_value": 0.1093, "depth": 8}
								if obj[1]<=0.5941304347826087:
									# {"feature": "citric acid", "instances": 36, "metric_value": 0.1831, "depth": 9}
									if obj[2]>0.28:
										return 'bad'
									elif obj[2]<=0.28:
										# {"feature": "sulphates", "instances": 10, "metric_value": 0.469, "depth": 10}
										if obj[9]>0.54:
											return 'bad'
										elif obj[9]<=0.54:
											# {"feature": "fixed acidity", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[0]<=7.9:
												return 'bad'
											elif obj[0]>7.9:
												return 'good'
											else: return 'good'
										else: return 'bad'
									else: return 'bad'
								elif obj[1]>0.5941304347826087:
									return 'bad'
								else: return 'bad'
							elif obj[7]<=0.9948023556288615:
								# {"feature": "fixed acidity", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]>5.9:
									return 'good'
								elif obj[0]<=5.9:
									return 'bad'
								else: return 'bad'
							else: return 'good'
						elif obj[8]<=2.93:
							# {"feature": "citric acid", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=0.28:
								return 'good'
							elif obj[2]>0.28:
								return 'bad'
							else: return 'bad'
						else: return 'good'
					elif obj[3]>9.516083208746958:
						return 'good'
					else: return 'good'
				else: return 'bad'
			elif obj[4]<=0.038:
				return 'good'
			else: return 'good'
		elif obj[5]<=1.0:
			return 'good'
		else: return 'good'
	elif obj[10]>11.488317414799278:
		# {"feature": "fixed acidity", "instances": 280, "metric_value": 0.4459, "depth": 2}
		if obj[0]>4.6:
			# {"feature": "sulphates", "instances": 279, "metric_value": 0.4352, "depth": 3}
			if obj[9]>0.37:
				# {"feature": "residual sugar", "instances": 278, "metric_value": 0.4241, "depth": 4}
				if obj[3]<=7.004917399898503:
					# {"feature": "volatile acidity", "instances": 272, "metric_value": 0.3923, "depth": 5}
					if obj[1]<=0.9722506001702707:
						# {"feature": "citric acid", "instances": 270, "metric_value": 0.3809, "depth": 6}
						if obj[2]<=0.738103389514061:
							# {"feature": "pH", "instances": 268, "metric_value": 0.3693, "depth": 7}
							if obj[8]<=3.356082089552239:
								# {"feature": "free sulfur dioxide", "instances": 151, "metric_value": 0.1407, "depth": 8}
								if obj[5]>3.0:
									# {"feature": "chlorides", "instances": 140, "metric_value": 0.108, "depth": 9}
									if obj[4]<=0.0796642857142857:
										return 'good'
									elif obj[4]>0.0796642857142857:
										# {"feature": "total sulfur dioxide", "instances": 51, "metric_value": 0.2387, "depth": 10}
										if obj[6]<=27.627450980392158:
											# {"feature": "density", "instances": 34, "metric_value": 0.3228, "depth": 11}
											if obj[7]>0.9969517647058824:
												return 'good'
											elif obj[7]<=0.9969517647058824:
												return 'good'
											else: return 'good'
										elif obj[6]>27.627450980392158:
											return 'good'
										else: return 'good'
									else: return 'good'
								elif obj[5]<=3.0:
									# {"feature": "chlorides", "instances": 11, "metric_value": 0.4395, "depth": 9}
									if obj[4]>0.05:
										return 'good'
									elif obj[4]<=0.05:
										# {"feature": "total sulfur dioxide", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6]<=8.0:
											return 'good'
										elif obj[6]>8.0:
											return 'bad'
										else: return 'bad'
									else: return 'bad'
								else: return 'good'
							elif obj[8]>3.356082089552239:
								# {"feature": "density", "instances": 117, "metric_value": 0.5757, "depth": 8}
								if obj[7]>0.9923736264315303:
									# {"feature": "chlorides", "instances": 102, "metric_value": 0.6268, "depth": 9}
									if obj[4]>0.047091033775712665:
										# {"feature": "total sulfur dioxide", "instances": 91, "metric_value": 0.6709, "depth": 10}
										if obj[6]<=82.09841860630175:
											# {"feature": "free sulfur dioxide", "instances": 87, "metric_value": 0.6365, "depth": 11}
											if obj[5]<=15.574712643678161:
												return 'good'
											elif obj[5]>15.574712643678161:
												return 'good'
											else: return 'good'
										elif obj[6]>82.09841860630175:
											# {"feature": "free sulfur dioxide", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[5]<=17.0:
												return 'bad'
											elif obj[5]>17.0:
												return 'good'
											else: return 'good'
										else: return 'bad'
									elif obj[4]<=0.047091033775712665:
										return 'good'
									else: return 'good'
								elif obj[7]<=0.9923736264315303:
									return 'good'
								else: return 'good'
							else: return 'good'
						elif obj[2]>0.738103389514061:
							# {"feature": "chlorides", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0.066:
								return 'good'
							elif obj[4]>0.066:
								return 'bad'
							else: return 'bad'
						else: return 'bad'
					elif obj[1]>0.9722506001702707:
						# {"feature": "citric acid", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]>0.24:
							return 'good'
						elif obj[2]<=0.24:
							return 'bad'
						else: return 'bad'
					else: return 'bad'
				elif obj[3]>7.004917399898503:
					# {"feature": "chlorides", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[4]>0.051:
						return 'bad'
					elif obj[4]<=0.051:
						return 'good'
					else: return 'good'
				else: return 'bad'
			elif obj[9]<=0.37:
				return 'bad'
			else: return 'bad'
		elif obj[0]<=4.6:
			return 'bad'
		else: return 'bad'
	else: return 'good'
