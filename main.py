from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
from tensorflow.keras.preprocessing import image

# Load the saved model
model = load_model("cat_vs_dog_model.h5")

# Create the GUI window
root = tk.Tk()
root.title("Cat vs Dog Predictor")

# Center the window and make it bigger
window_width = 500
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Function to handle file selection
def select_file():
    file_path = filedialog.askopenfilename(parent=root, title="Select file", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
    if file_path:
        predict_class(file_path)

# Function to make a prediction and show the result
def predict_class(file_path):
    try:
        # Load the image and resize it to the required input size of the model
        img = Image.open(file_path)
        img = img.resize((100, 100))

        # Convert the image to a numpy array
        img_array = image.img_to_array(img)

        # Reshape the array to match the expected input shape of the model
        img_array = np.expand_dims(img_array, axis=0)

        # Normalize the image data
        img_array = img_array / 255.0

        # Make a prediction using the trained model
        prediction = model.predict(img_array)

        # Show the predicted class (0 for cat, 1 for dog)
        if prediction[0][0] > prediction[0][1]:
            predicted_class = "Cat"
        else:
            predicted_class = "Dog"

        # Update the image and prediction label
        img_tk = ImageTk.PhotoImage(img)
        image_label.configure(image=img_tk)
        image_label.image = img_tk
        prediction_label.configure(text=f"{file_path}\n\n{predicted_class}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the file selection button
select_button = tk.Button(root, text="Select File", command=select_file)
select_button.pack(pady=10)

# Create the image label
image_label = tk.Label(root)
image_label.pack()

# Create the prediction label
prediction_label = tk.Label(root, font=("Helvetica", 16))
prediction_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
