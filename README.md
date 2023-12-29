# Group People by Address WebApp

This web application allows users to group people living at identical addresses. Users can input data either by manual text entry through a UI or by uploading a .csv file. The results are displayed on the UI, and users can download the results as a .txt file.

## Usage

1. Install the required dependencies:

```bash
pip install flask

2. Run the application:
python app.py

3.Open a web browser and go to http://127.0.0.1:5000/

4.Input data through the UI or upload a .csv file.

5.View the grouped results on the UI and download the result as a .txt file.

Additional Information
The uploaded .csv file is temporarily stored in the 'uploads' folder and is removed after processing.
Ensure that the .csv file has a 'Name' and 'Address' column.
There are no library usage restrictions for this solution.
