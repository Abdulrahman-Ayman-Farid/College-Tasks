import cv2
import matplotlib.pyplot as plt
import numpy as np

rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)

bitwise_and = cv2.bitwise_and(rectangle, circle)
bitwise_or = cv2.bitwise_or(rectangle, circle)
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
bitwise_not_circ = cv2.bitwise_not(circle)

plt.figure(figsize=(15, 10))
plt.suptitle("Bitwise (Logical) Operations", fontsize=16)

plt.subplot(2, 3, 1)
plt.imshow(rectangle, cmap='gray')
plt.title("Rectangle")
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(circle, cmap='gray')
plt.title("Circle")
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(bitwise_and, cmap='gray')
plt.title("AND")
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(bitwise_or, cmap='gray')
plt.title("OR")
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(bitwise_xor, cmap='gray')
plt.title("XOR")
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(bitwise_not_circ, cmap='gray')
plt.title("NOT (Circle)")
plt.axis('off')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
print("Displaying bitwise operations plot.")
plt.show()
print("Plot window closed.")