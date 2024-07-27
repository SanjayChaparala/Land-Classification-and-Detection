# Land Classification and Detection

This project involves developing a Computer Vision framework to classify and detect various land types from satellite imagery, aimed at determining the total land cover available for urban planning. The framework leverages advanced algorithms and image processing techniques to provide accurate and actionable insights for urban planners.

## Features

- Land Classification Framework: Utilizes YOLOv5, OpenCV, and TensorFlow to classify and detect different land types from satellite imagery.
- Algorithm Development: Employs Python, scikit-learn, and Keras to engineer and fine-tune advanced algorithms for precise land classification.
- Data Processing: Preprocesses and analyzes large datasets of satellite images using Pandas and NumPy to enhance model accuracy.
- Model Integration: Integrates Computer Vision models into practical urban planning applications using Docker for seamless deployment.
- Google Colab Utilization: Leverages Google Colab for running experiments and training models, benefiting from powerful computational resources.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/Land-Classification-and-Detection.git
    ```

2. Navigate to the project directory:
    ```sh
    cd Land-Classification-and-Detection
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Training the Model:**
    - Open `yolov5.ipynb` in Google Colab or Jupyter Notebook.
    - Run the cells to train the YOLOv5 model on your dataset.

2. **Testing the Model:**
    - Open `vision.ipynb` in Google Colab or Jupyter Notebook.
    - Run the cells to test the trained model on a set of satellite images.

3. **Classifying a Single Image:**
    - Use the `data.py` script to classify and detect land types in a single clear satellite image:
    ```sh
    python data.py --input data/hd_satellite_image.jpg --output results/land_classification.jpg
    ```

## Project Structure

- `data/`: Directory for storing satellite images and datasets.
- `yolov5.ipynb`: Jupyter Notebook for training the YOLOv5 model.
- `vision.ipynb`: Jupyter Notebook for testing the trained model.
- `data.py`: Script for testing a single clear satellite image.
- `requirements.txt`: List of dependencies required for the project.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements or new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

