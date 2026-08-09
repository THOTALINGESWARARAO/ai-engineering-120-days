import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
scores = [35, 42, 50, 61, 70]
attendance = [60, 65, 68, 72, 75]

plt.scatter(hours, scores)
plt.title("Hours vs Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()

plt.scatter(hours, scores, s=100)
plt.show()

plt.scatter(hours, scores, alpha=0.5)
plt.show()

plt.scatter(hours, scores, marker="^")
plt.show()

group = [0, 0, 0, 1, 1]

plt.scatter(hours, scores, c=group)
plt.show()

fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(hours, scores)
ax.set_title("Hours vs Score")
ax.set_xlabel("Hours Studied")
ax.set_ylabel("Exam Score")
ax.grid(True)

plt.show()

fig, axes = plt.subplots(1, 2)

axes[0].scatter(hours, scores)
axes[0].set_title("Hours vs Score")

axes[1].hist(scores)
axes[1].set_title("Score Distribution")

plt.show()

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].scatter(hours, scores)
axes[0, 0].set_title("Hours vs Score")
axes[0, 0].set_xlabel("Hours Studied")
axes[0, 0].set_ylabel("Exam Score")
axes[0, 0].grid(True)

axes[0, 1].scatter(attendance, scores)
axes[0, 1].set_title("Attendance vs Score")
axes[0, 1].set_xlabel("Attendance")
axes[0, 1].set_ylabel("Exam Score")
axes[0, 1].grid(True)

axes[1, 0].hist(scores, bins=5)
axes[1, 0].set_title("Score Distribution")
axes[1, 0].set_xlabel("Score")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].grid(True)

axes[1, 1].hist(attendance, bins=5)
axes[1, 1].set_title("Attendance Distribution")
axes[1, 1].set_xlabel("Attendance")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].grid(True)

plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(hours, scores, label="Students")
ax.legend()

plt.show()

fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(hours, scores)
ax.set_title("Hours vs Score")
ax.set_xlabel("Hours Studied")
ax.set_ylabel("Exam Score")
ax.grid(True)

plt.tight_layout()

plt.savefig("day16_scatter.png",dpi=300,bbox_inches="tight")

plt.show()

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].scatter(hours,scores,s=80,alpha=0.7)
axes[0, 0].set_title("Hours Studied vs Exam Score")
axes[0, 0].set_xlabel("Hours Studied")
axes[0, 0].set_ylabel("Exam Score")
axes[0, 0].grid(True)

axes[0, 1].scatter(attendance,scores,s=80,alpha=0.7)
axes[0, 1].set_title("Attendance vs Exam Score")
axes[0, 1].set_xlabel("Attendance")
axes[0, 1].set_ylabel("Exam Score")
axes[0, 1].grid(True)

axes[1, 0].hist(scores, bins=5)
axes[1, 0].set_title("Score Distribution")
axes[1, 0].set_xlabel("Score")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].grid(True)

axes[1, 1].hist(attendance, bins=5)
axes[1, 1].set_title("Attendance Distribution")
axes[1, 1].set_xlabel("Attendance")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].grid(True)

plt.tight_layout()

plt.savefig("Student Performance EDA dashboard.png",dpi=300,bbox_inches="tight")

plt.show()