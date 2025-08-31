# Key notes from unit

# 1. Optimisation

### What it is:

- it means finding the best values for our parameters like weights in a neural network
- - Best typical means make the error as small as possible
- - Optimisation is the process of finding that "the best point"

### Derivatives and critical points

Think of a curve (like a hill)

- The slope tells you if you're going up hill or down hill
- When the slope = 0, you're at the "flat spot" which could be the top of the hill (maximum), the bottom of a valley (minimum), or a saddle (flat but not min or max)

This "slope" is what a derivative measures

- For one variable (x), the derivative is just the slope at that point
- For multiple variables (x,y,...), we use partial derivatives: slope in the x-direction, slope in the y-direct etc.
- Collecting partial derivatives give a gradient vector = direction of steepest uphill

### First Derivative Test

How do you find where the "flat spots" are?

- Take the first derivative
- set it equal to zero
- solve for the x( or x,y,...)
- These are your critical points.

#### Examples:

👉 Conceptual Example: If f(x) = x², derivative is f′(x) = 2x. Setting 2x = 0 → x = 0 is a critical point.

👉 Example 1: A valley (minimum)

Let’s take
f(x) = (x – 3)²

Derivative: f′(x) = 2(x – 3)

Set = 0 → 2(x – 3) = 0 → x = 3

So the critical point is at x = 3.

If you look at the graph: it’s a parabola shaped like a bowl, lowest point at (3,0).
👉 Critical point = minimum.

👉 Example 2: A hill (maximum)

Take
f(x) = –x²

Derivative: f′(x) = –2x

Set = 0 → –2x = 0 → x = 0

Critical point at x = 0.

Graph is an upside-down bowl (like a hilltop).
👉 Critical point = maximum.

👉 Example 3: A flat crossing (not max or min)

Take
f(x) = x³

Derivative: f′(x) = 3x²

Set = 0 → 3x² = 0 → x = 0

Critical point at x = 0.

Graph goes down → flattens at (0,0) → then goes up again. It’s not a min or max, it’s just a saddle/flat inflection point.
👉 Shows that “derivative = 0” doesn’t always mean min or max.

👉Example 4: Multiple critical points

Take
f(x) = x³ – 3x

Derivative: f′(x) = 3x² – 3

Set = 0 → 3x² – 3 = 0 → x² = 1 → x = ±1

Two critical points: x = –1 and x = 1.

Graph looks like a snake:

At x = –1 → it’s a local maximum.

At x = 1 → it’s a local minimum.

👉 Same function can have multiple mins and maxes.

👉 Example 5: Flat everywhere (special case)

Take
f(x) = 5 (a flat horizontal line)

Derivative: f′(x) = 0 (for all x).

Every point is technically a “critical point” (slope is 0 everywhere).

But since the graph is totally flat, there are no maxima or minima — it’s just constant.
👉 Shows that critical points don’t always matter in optimisation.

🔑 Pattern you should notice:

Step 1: derivative tells you slope.

Step 2: set slope = 0 → gives “flat spots”.

Step 3: these flat spots could be min, max, or neither. You only know after testing curvature (second derivative).
