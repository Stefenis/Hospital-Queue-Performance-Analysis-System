import csv, random, datetime

def rand_time(base, minutes_range=600):
    delta = datetime.timedelta(seconds=random.randint(0, minutes_range*60))
    return (base + delta).strftime("%Y-%m-%d %H:%M:%S")

base = datetime.datetime(2025,10,20,8,0,0)  # day 1 8:00
rows = []
doctors = ['D1','D2','D3','D4']
for i in range(1,1001):
    arrival = rand_time(base, minutes_range=12*60)  # arrivals during 12 hours
    reg = random.randint(60, 300)
    doc = random.choice(doctors)
    consult_start = rand_time(base, minutes_range=12*60)
    consult_dur = random.randint(300, 1800)  # 5 to 30 mins
    test_req = random.random() < 0.25
    test_dur = random.randint(300, 1800) if test_req else 0
    total_wait = reg + random.randint(60, 3600)
    schedule = "08:00-16:00"
    rows.append([f"P{i}", arrival, reg, doc, consult_start, consult_dur, int(test_req), test_dur, total_wait, schedule])

with open('hospital_queue_dataset.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['patient_id','arrival_time','registration_time_seconds','doctor_assigned','consultation_start','consultation_duration_seconds','test_required','test_duration_seconds','total_wait_seconds','doctor_schedule'])
    w.writerows(rows)

print("✅ Generated hospital_queue_dataset.csv successfully!")
