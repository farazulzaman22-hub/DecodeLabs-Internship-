import cv2
import pytesseract

# Tesseract OCR Path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load Image
image = cv2.imread("Images/test.png")

# Check if image exists
if image is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully.")

    # Convert to Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Otsu Thresholding
    _, thresh = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Extract Text using OCR
    text = pytesseract.image_to_string(
        thresh,
        config='--psm 6'
    )

    # Display Extracted Text
    print("\n========== EXTRACTED TEXT ==========\n")
    print(text)

    # Save Text to File
    with open("extracted_text.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("\nText saved successfully in 'extracted_text.txt'")

    # Optional: Show Processed Image
    cv2.imshow("Original Image", image)
    cv2.imshow("Threshold Image", thresh)

    cv2.waitKey(0)
    cv2.destroyAllWindows()