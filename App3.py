import tkinter as tk
from tkinter import messagebox
import pandas as pd
import pickle
import random

# Load the trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Classification function
def classify_mass_index(percentage):
    if percentage < 18:
        return "You are fit. Keep it up! You look like a martial artist.", "You're doing great! Here are some exercises to maintain your fitness: Jumping Jacks, Push-ups, Squats, Lunges, and Planks."
    elif 18 <= percentage < 25:
        return "You are normal. Maintain your current lifestyle.", "You're in good shape! Here are some exercises to stay active: Walking, Cycling, Swimming, Yoga, and Dancing."
    elif 25 <= percentage < 30:
        return "You are overweight. Consider incorporating more exercise into your routine.", "It's time to get moving! Here are some exercises to help you shed those extra pounds: Running, Cycling, Jump Rope, High-Intensity Interval Training (HIIT), and Strength Training."
    else:
        return "You are obese. It's important to focus on a healthy diet and regular exercise.", "Let's work on getting healthier! Here are some exercises to kickstart your fitness journey: Cardio Workouts, Weight Training, Circuit Training, Pilates, and Kickboxing."

# Prediction function
def predict_mass_index():
    try:
        # Collect input data
        age = float(entry_age.get())
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        # Validate age
        if age > 100:
            messagebox.showwarning("Age Limit Exceeded", "Please enter an age less than or equal to 100.")
            return

        # Calculate BMI
        bmi = weight / (height / 100) ** 2

        # Create DataFrame
        input_df = pd.DataFrame([[age, bmi]], columns=['Age', 'BMI'])

        # Make prediction
        prediction = model.predict(input_df)[0]

        # Classify prediction and get exercise suggestions
        classification, exercises = classify_mass_index(prediction)

        # Display result and exercises
        messagebox.showinfo("Prediction Result", f"Predicted Body Mass Index: {prediction:.2f}%\n{classification}\n\n{exercises}")

    except ValueError as ve:
        messagebox.showerror("Input Error", f"Please enter valid numeric values: {ve}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the Tkinter GUI
root = tk.Tk()
root.title("Body Mass Index")

# Add colorful background
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()
background_img = tk.PhotoImage(file=r"C:\Users\Asus\OneDrive\Desktop\Body Mass Index Prediction\peach-peachandgoma.gif")
canvas.create_image(0, 0, anchor=tk.NW, image=background_img)

# Create and place the input fields and labels
fields = ['Age', 'Weight (kg)', 'Height (cm)']
entries = {}

for field in fields:
    frame = tk.Frame(root, bg='lightblue')
    label = tk.Label(frame, text=field, font=('Helvetica', 12, 'bold'), bg='lightblue')
    entry = tk.Entry(frame, font=('Helvetica', 12))
    frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    label.pack(side=tk.LEFT)
    entry.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    entries[field] = entry

# Assign entries to specific variables
entry_age = entries['Age']
entry_weight = entries['Weight (kg)']
entry_height = entries['Height (cm)']

# Create and place the Predict button
predict_button = tk.Button(root, text="Predict", command=predict_mass_index, font=('Helvetica', 12, 'bold'), bg='green', fg='white')
predict_button.pack(side=tk.BOTTOM, padx=5, pady=10)

# Run the GUI loop
root.mainloop()
