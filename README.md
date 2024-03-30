# Satellite Image Dehazing using the AOD-Net Architecture

This project focuses on the removal of haze from satellite images, enhancing their quality and visibility using a deep learning approach. By leveraging convolutional layers, residual connections, and concatenation techniques, AOD-Net efficiently eliminates haze from input images, resulting in clearer and more detailed output.

<img width="468" alt="dehazing" src="https://github.com/SejalKankriya/satellite-image-dehazing/assets/43418191/7c22b655-9e8b-40d3-920b-00b70f4924b3">

## Folder Structure

* `readme.md`: Instructions for the project
* `requirement.txt`: All the installation libraries
* `dehazing-code.ipynb`: Complete code for the dehazing
* `dehazing.py`: Python code to run UI on windows os.
* `run_cvip_ui_picker.bat`: Bat file to run the dehazing UI on windows
* `run.py`: Python code to run UI on any OS.
* `test_dataset`: Hazy image test data
* `AOD_Net_reg.h5`: Hierarchical Data Format with saved model data.

## Getting Started
These instructions will guide you on how to set up your environment to run the project.

### Prerequisites
Ensure you have Python 3.6 or higher installed. The project dependencies can be installed via pip:

```bash
pip install -r requirements.txt
```

Alternatively, install the dependencies directly:
```bash
pip install opencv-python numpy tensorflow matplotlib scikit-image keras tkinter PIL
```

### Running the Dehazing App
To run the dehazing application on Windows:
  
  1. Double-click the run_cvip_ui_picker.bat file. Wait for the app to open.
  2. Choose and upload an image from the test_dataset directory.

To run the dehazing project on macOS or Linux:

  1. Open the terminal.
  2. Execute the command python run.py.
  3. To dehaze a different image, change the image path in the img variable inside run.py, for ex: img = cv2.imread('test_dataset/0810.jpg').

**Note**: Do not close the command prompt while the app is running.

## Project Insights
The project utilizes AOD-Net for dehazing, showing significant improvement in image clarity and quality of dehazed images compared to their hazy counterparts. The model's effectiveness is evidenced by qualitative results, validating the model's effectiveness against state-of-the-art techniques.

## License
This project is licensed under the MIT license.
