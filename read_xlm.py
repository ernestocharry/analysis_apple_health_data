import pandas as pd
from datetime import datetime

df = pd.read_xml('export.xml')

df.drop(df.index[:2], inplace=True)  # Drop data from date exported, date birth 
df.reset_index(inplace=True, drop=True)

df = df[['value', 'HKCharacteristicTypeIdentifierDateOfBirth',
         'HKCharacteristicTypeIdentifierBiologicalSex',
         'HKCharacteristicTypeIdentifierBloodType',
         'HKCharacteristicTypeIdentifierFitzpatrickSkinType',
         'HKCharacteristicTypeIdentifierCardioFitnessMedicationsUse', 
         'type','sourceName', 'unit', 'creationDate', 'startDate','endDate', 
         'MetadataEntry', 'device', 'workoutActivityType', 'duration',
         'durationUnit', 'WorkoutEvent', 'WorkoutStatistics', 'WorkoutRoute',
         'dateComponents', 'activeEnergyBurned', 'activeEnergyBurnedGoal',
         'activeEnergyBurnedUnit', 'appleMoveTime', 'appleMoveTimeGoal',
         'appleExerciseTime', 'appleExerciseTimeGoal', 'appleStandHours',
         'appleStandHoursGoal', 'HeartRateVariabilityMetadataList']]

df = df[['value', 'type','sourceName', 'unit', 'creationDate', 'startDate',
         'endDate']]

df = df.where(df['creationDate'] >= "2022-01-01").dropna()

df.to_csv('export_from_python_'+datetime.today().strftime('%Y%m%d')+'.csv')
df.to_csv('C:/Users/felix/Documents/control_charry/export_from_python.csv')