# 🧠 Cancer Detection App

This Streamlit-based web application detects **Brain Cancer** and **Skin Cancer** from uploaded medical images using YOLO object detection models.

## 📌 Features

- 🏥 **Brain Cancer Detection** using a trained YOLO model.
- 🩺 **Skin Cancer Detection** using a separate YOLO model.
- 📊 **Confidence Level Adjustment** for setting detection thresholds.
- 📂 **Dataset Links** for reference.
- 🖼 **User-Friendly UI** for easy image uploading and detection.

## 📦 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Jnan-py/cancer-detection-app.git
   cd cancer-detection-app
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Upload an image (either Brain MRI or Skin lesion).
3. Select the type of cancer detection: **Brain** or **Skin**.
4. Adjust the confidence threshold using the slider.
5. Click **"Detect Cancer"** to get the results.

## 📂 Project Structure

```
cancer-detection-app/
│── models/
│   ├── brain_detect.pt  # Brain cancer YOLO model
│   ├── skin_detect.pt   # Skin cancer YOLO model
│── notebooks/           # Contains model training notebooks
│── app.py               # Streamlit application
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

## 📝 Dataset Sources

- **Brain Cancer Dataset**: [Kaggle - Brain Tumor MRI](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)
- **Skin Cancer Dataset**: [Kaggle - Skin Cancer](https://www.kaggle.com/datasets/nodoubttome/skin-cancer9-classesisic)

## 🔧 Requirements

Ensure you have **Python 3.8+** installed.

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## 🛠 Technologies Used

- **Python**
- **Streamlit**
- **YOLOv8**
- **OpenCV**
- **PIL (Pillow)**
- **NumPy**
- **Pandas**

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

## 🏆 Acknowledgements

- **Ultralytics YOLO** for object detection models.
- **Kaggle** for datasets.
