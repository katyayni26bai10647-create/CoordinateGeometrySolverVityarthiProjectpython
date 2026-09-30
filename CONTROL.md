# Execution Control Matrix (GeoKit CLI)

This document specifies the operational lifecycle, routing architecture, state constraints, and validation handling mechanics governing the **GeoKit CLI** runtime engine.

---

## 1. System Execution Lifecycle

---

## 2. Component Routing & Variable Registry

The execution engine processes data variables through isolated functional blocks based on user navigation.

### 🔹 Module 1: Distance Calculation
* **Target Trigger:** `choice == "1"`
* **Local Scope Variables:**
  * Inputs: `x1`, `y1`, `x2`, `y2` (Type: `float`)
  * Internal Aggregator: `a` (Stores the resolved hypotenuse distance)
* **Mathematical Implementation:** Uses the Euclidean metric equation:
  \[a = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\]

### 🔹 Module 2: Midpoint Bisection
* **Target Trigger:** `choice == "2"`
* **Local Scope Variables:**
  * Inputs: `x1`, `y1`, `x2`, `y2` (Type: `float`)
  * Intermediates: `b` (x-axis median balance), `c` (y-axis median balance)
* **Mathematical Implementation:** *Note: The baseline script currently processes a subtraction vector constraint (x₂ - x₁)/2. A patch is required to shift this to true midpoint averaging:*
  \[b = \frac{x_1 + x_2}{2}, \quad c = \frac{y_1 + y_2}{2}\]

### 🔹 Module 3: Slope Determination
* **Target Trigger:** `choice == "3"`
* **Local Scope Variables:**
  * Inputs: `d` (Coefficient of x), `e` (Coefficient of y)
  * Output: `f` (Line gradient)
* **Mathematical Implementation:** Derivation from standard form matrix linear layout dx + ey + g = 0:
  \[f = \frac{-d}{e}\]

---

## 3. Input Validation & Error Hardening Matrix

| Input Context | Variable Target | Data Type | Constraint Boundaries | Fallback Action / Exception Path |
| :--- | :--- | :--- | :--- | :--- |
| **Menu Route Selection** | `choice` | `str` | Must match exact characters `"1"`, `"2"`, `"3"`, `"4"` | Any unrecognized string bypasses calculations and defaults directly to system termination. |
| **Grid Metrics** | `x1`, `y1`, `x2`, `y2` | `float` | Continuous real numbers (-∞, ∞) | Non-numeric strings cause a fatal `ValueError` crash. *(Requires Try-Except patch to catch invalid input symbols)*. |
| **Linear Formula x-Weight** | `d` | `float` | Continuous real numbers (-∞, ∞) | Handled normally via core algebraic operations. |
| **Linear Formula y-Weight** | `e` | `float` | Critical Constraint: **Must not be equal to `0`** | If `e == 0`, a division by zero error occurs (`ZeroDivisionError`), causing an unhandled software crash. |

---

## 4. Architectural Vulnerabilities & Optimization Log

To upgrade this control file from a prototype map into a production-ready application specification, the following structural patches must be developed:

1. **State Persistence Loop:** Wrap the entry pipeline in a continuous conditional evaluation loop (`while True`). This keeps the menu open instead of dropping execution after resolving a single calculation.
2. **Exception Shields:** Implement explicit safety gates on Module 3 input metrics to block user entries where `e == 0`. It should route to a clear string notice (`"Slope is undefined / Vertical Line"`) rather than crashing the interface thread.
3. **Dependency Pruning:** The runtime configuration currently executes `import math` and `import cmath` hooks during boot-up. Because calculations are solved through lower-level native power calculations (`**0.5`), these imports are dead system memory links and should be removed.s

