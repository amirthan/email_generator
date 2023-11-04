# Email Generator Application

## Project Description

This project provides an interactive web application for generating emails based on user-defined parameters. Utilizing the power of Streamlit alongside a open source llms, users can easily craft emails with varying styles, tones, subject matter, and more. This user-friendly application offers a simple interface for customizing the content of the email to fit various contexts and recipient preferences.

## Setup Instructions

1. **Clone the Repository**:
   - Clone this repository to your local machine by running the following command:
     ```bash
     git clone https://github.com/amirthan/email_generator.git
     ```

2. **Install Dependencies**:
   - Navigate to the project directory:
     ```bash
     cd your-repository
     ```
   - Install the necessary dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```

3. **Download the Model**:
   - Download the Hugging Face model `lama-2-7b-chat.Q5_K_M.gguf` from the provided link (you might need to provide the link).
   - Create a folder named `models` in the root directory of the project.
   - Place the downloaded model file `lama-2-7b-chat.Q5_K_M.gguf` inside the `models` folder.
   - The model can be downloaded from this page https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/tree/main

4. **Run the Application**:
   - In the root directory of the project, run the following command to start the Streamlit application:
     ```bash
     streamlit run app.py
     ```

The application should now be running on your local machine. Navigate to the URL provided in the terminal to access the Email Generator Application. From here, you can enter your desired parameters and generate emails with ease!

---