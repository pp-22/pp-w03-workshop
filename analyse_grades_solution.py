import numpy as np
import matplotlib.pyplot as plt

# Read the data into a NumPy array
grades = np.loadtxt('grades.txt', delimiter=',')

# Make 4 histograms to display the grades for each assignment
# Note: this is not the only way to create subplots
fig, ax = plt.subplots(1, 4)

# Use a loop to draw all 4 histograms
for i in range(4):
    # By grade:
    ax[i].hist(grades[:, i], bins=range(0, 101))

    # By band:
    #  ax[i].hist(grades[:, i], bins=range(0, 101, 10))
plt.show()

# Report some statistics in a file
n = grades.shape[0]

with open('stats.txt', 'w') as report:

    report.write('Statistics by assignment\n')

    # Reports per assignment
    for i in range(4):
        report.write(f'Assignment {i+1}:\n')
        report.write(f'- Average grade: {np.mean(grades[:, i]):.1f}\n')
        report.write(f'- Median grade: {np.median(grades[:, i]):.1f}\n')

        # How many students got an A?
        got_A = np.count_nonzero(grades[:, i] >= 70)
        report.write(f'- {got_A} students got an A ({100*got_A/n:.1f}% of students).\n\n')

    # How many students got an A on all assignments?
    # One way to do this with a loop and conditional statement:
    got_A_all = 0
    for s in range(n):
        # Add 1 student to the total if they got As everywhere
        #  if grades[s, 0] >= 70 and grades[s, 1] >= 70 and grades[s, 2] >= 70 and grades[s, 3] >= 70:
            #  got_A_all += 1

        # Another way to do the same thing, casting a bool to an int:
        got_A_all += int(np.all(grades[s, :] >= 70))

    # Yet another way, which doesn't require a loop, type-casting an array of bools to 0s and 1s
    # got_A_all = np.sum(np.all(grades >= 70, axis=1))

    report.write(f'\n{got_A_all} students got an A for all 4 assignments ({100*got_A_all/n:.1f}% of students).\n')
