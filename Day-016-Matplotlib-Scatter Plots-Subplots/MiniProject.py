import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
scores = [35, 40, 48, 52, 58, 65, 70, 75, 82, 90]
attendance = [60, 65, 68, 72, 75, 80, 82, 88, 92, 95]

fig, axes = plt.subplots(2,2,figsize=(12, 8))

axes[0, 0].scatter(hours,scores,s=100,alpha=0.7)
axes[0, 0].set_title("Hours Studied vs Exam Score")
axes[0, 0].set_xlabel("Hours Studied")
axes[0, 0].set_ylabel("Exam Score")
axes[0, 0].grid(True)

axes[0, 1].scatter(attendance,scores,s=80,alpha=0.7)
axes[0, 1].set_title("Attendance vs Exam Score")
axes[0, 1].set_xlabel("Attendance")
axes[0, 1].set_ylabel("Exam Score")
axes[0, 1].grid(True)

axes[1, 0].hist(scores,bins=5)
axes[1, 0].set_title("Score Distribution")
axes[1, 0].set_xlabel("Score")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].grid(True)

axes[1, 1].hist(attendance,bins=5)
axes[1, 1].set_title("Attendance Distribution")
axes[1, 1].set_xlabel("Attendance")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].grid(True)

plt.tight_layout()
plt.savefig("Student Performance EDA dashboard.png",dpi=300,bbox_inches="tight")
plt.savefig("Student Performance EDA dashboard.svg",dpi=300,bbox_inches="tight")
plt.show()