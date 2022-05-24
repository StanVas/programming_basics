time_period = int(input())
treated_patients = 0
untreated_patients = 0
doctors = 7
for patient in range(1, time_period + 1):
    patients = int(input())
    if patient % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if doctors >= patients:
        treated_patients += patients
    elif doctors < patients:
        untreated_patients += patients - doctors
        treated_patients += doctors
print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
