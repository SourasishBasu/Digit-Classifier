# Digit-Classifier
Interactive ML webapp using Gradio and Tensorflow to identify handwritten digits using a model trained on the MNIST dataset.

## Prerequisites:

- Python 3.9 & up

- Open Command prompt and type:

  ```bash
  pip install gradio --user

  pip install tensorflow --user
  ```

### To run in terminal:
- Open Powershell in the local repository folder
- Type:

  ```bash
   python main.py
  ```
  
- The web interface will be available at the url generated: http://localhost:8080

## Using Google Colab
- The program is also available in Google Colab which can be accessed [here](https://colab.research.google.com/github/SourasishBasu/Digit-Classifier/blob/main/Digit_Classifier.ipynb).

- Copy the notebook to your Google Drive and follow the instructions to run the code.

## Usage

- Draw different digits using mouse cursor onto the sketch area and click submit.

- A list of guesses along with how confident the trained model is for other guesses will be provided with varying percentages.

- Click clear to refresh the sketch area and start drawing again.

## App Images

<p align="center"> 
  <img src="https://github.com/SourasishBasu/Digit-Classifier/blob/36be02c13b92a8b7a1fbc8e0484a951710101c50/assets/webUI.png" />
   <br><b>Interface</b>
</p>

<br></br>

<p align="center"> 
  <img src="https://github.com/SourasishBasu/Digit-Classifier/blob/36be02c13b92a8b7a1fbc8e0484a951710101c50/assets/guess.png" />
</p>

<br></br>
