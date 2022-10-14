import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

# Generate lots of fake grades for 4 assignments in a class of 300.
# For half the class (150): create a skewed distribution
#   using the product of normally distributed samples.
# For the other half: add normally distributed grades
#   over quite a wide range.

grades = []
means = [[70, 80], [76, 84], [62, 76], [54, 69]]

# Loop over assignments
for j in range(4):
    b = []

    # Tinker with numbers until you get something looking nice
    for i in range(150):
        a = 15. + rng.standard_normal(100)
        b.append(np.product(a))

    # Flip distribution to be centred around the chosen mean,
    # with the tail on the left
    b = np.array(b) / np.min(b) # scale values to be positive
    b = means[j][1] - np.array(b, dtype=int)

    # Add some normally distributed grades to that to pad out the empty bits
    c = rng.normal(means[j][0], 20, 150)
    c = list(np.array(c, dtype=int))

    b = list(b)
    for i in c:
        b.append(i)

    # Bring down the generated grades greater than 100
    for i in range(len(b)):
        if b[i] > 100:
            b[i] = 100 - int(rng.normal(5, 2))
    
    # Plot the histogram to check the distribution -- run again if I don't like it!
    plt.hist(b, bins=range(0, 101))
    grades.append(b)

plt.show()

# Take the absolute values, just in case we have a few negative grades by now
grades = np.abs(np.array(grades, dtype=int))

# Shuffle the grades to mix the order between the 2 distributions
rng.shuffle(grades, axis=1)

# Write the data in the file
with open('grades_new.txt', 'w') as myfile:
    for i in range(300):
        line = f'{grades[0][i]},{grades[1][i]},{grades[2][i]},{grades[3][i]}\n'
        myfile.write(line)
