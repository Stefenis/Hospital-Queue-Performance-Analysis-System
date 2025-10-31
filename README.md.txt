Hospital Queue Performance Analysis System

Project Overview

The Hospital Queue Performance Analysis System models and analyzes patient flow in a hospital’s Outpatient Department (OPD).
It uses synthetic data to simulate patient arrivals, registration, consultations, and testing times.
The goal is to identify bottlenecks, reduce waiting times, and improve doctor utilization.

Files in this Repository

File Name	Description
generate_hospital_data.py	Python script used to generate the synthetic hospital dataset.
hospital_queue_dataset.csv	The generated dataset with 1,000 patient records.
report.docx	Word document describing the system, problem, dataset, performance objectives, and outcomes.
README.md	Documentation for this repository (this file).

🧠 System Overview

The system focuses on understanding the performance of hospital queues.
It captures how long patients wait for registration, consultation, and tests.
This helps hospital administrators and system developers identify performance bottlenecks and optimize operations.

🎯 Performance Objectives

Minimize average waiting time – Keep average wait ≤ 20 minutes.

Maximize doctor utilization – Maintain ≥ 80% utilization rate.

Increase throughput – Serve ≥ 8 patients per hour.

Balance doctor workloads – Keep queue length variance ≤ 10%.

Identify bottlenecks – Find process steps causing delays (delay ratio ≤ 0.3).

🧰 Tools and Techniques Used

Tools:

	Python 3

	Pandas, NumPy (for data generation and analysis)

	Matplotlib / Seaborn (for graphs)

	Excel (for viewing and verifying data)

	GitHub (for version control)

Techniques:

	Synthetic data generation

	Queue modeling and performance measurement

	Descriptive statistical analysis

	Bottleneck identification and resource optimization


📊 Expected Outcomes

	Reduced patient waiting times.

	Improved doctor and staff efficiency.

	Clear identification of bottlenecks.

	Balanced workload distribution.

	Data and visual reports for better decision-making.

💻 How to Reproduce

Clone the Repository

git clone https://github.com/<your-username>/hospital-queue-performance.git
cd hospital-queue-performance


Run the Python Script

python generate_hospital_data.py


Output

A file named hospital_queue_dataset.csv will be created in the same folder.

You can open it using Excel or analyze it using Python notebooks.

👨‍💻 Author

Name: Stefenis Pietersz

