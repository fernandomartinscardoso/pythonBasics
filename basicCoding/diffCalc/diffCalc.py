x = []
xi = 0
xf = 2
n = 4000
inc = (xf-xi)/n
for i in range(n):
    x.append(xi)
    xi = xi + inc
y = []
for j in range(n):
    y.append(x[j]*2)

# Define a specific x value, x0, to calculate the corresponding y value
x0 = 1.2
# Calculate y0 using the equation y = 2x
y0 = x0*2
# Iterate through the x values to find the first x value greater than x0
for k in range(n):
    # Check if the current x value is greater than x0
    if x[k] > x0:
        # Calculate the difference in y and x values
        diffy = y[k]-y0
        diffx = x[k]-x0
        # Break out of the loop once the condition is met
        break

diffy_x0 = diffy/diffx

print(diffy_x0)
